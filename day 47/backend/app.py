import os
import re

from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import errorcode

from ml.model import load_model, predict_churn, InvalidPredictionInput

load_dotenv()  # reads variables from .env into the environment

app = Flask(__name__)

# ---------------------------------------------------------------------------
# CORS Configuration — supports local development and configured cloud frontend
# ---------------------------------------------------------------------------
allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
custom_frontend = os.getenv("FRONTEND_URL")
if custom_frontend:
    if custom_frontend.strip() == "*":
        CORS(app, origins="*")
    else:
        for url in custom_frontend.split(","):
            cleaned = url.strip().rstrip("/")
            if cleaned and cleaned not in allowed_origins:
                allowed_origins.append(cleaned)
        CORS(app, origins=allowed_origins)
else:
    # Default to local development origins
    CORS(app, origins=allowed_origins)

# ---------------------------------------------------------------------------
# Load the ML model ONCE at application startup — not per-request.
# If this fails, we want to know immediately rather than on the first
# prediction call, so we let the exception surface here.
# ---------------------------------------------------------------------------
load_model()
app.logger.info("ML model loaded successfully at startup.")

# ---------------------------------------------------------------------------
# Database configuration — pulled from environment variables, never hardcoded.
# Supports DB_* standard names and native Railway MYSQL* variable names.
# See .env.example for the variables this expects.
# ---------------------------------------------------------------------------
DB_CONFIG = {
    "host": os.getenv("DB_HOST") or os.getenv("MYSQLHOST", "localhost"),
    "port": int(os.getenv("DB_PORT") or os.getenv("MYSQLPORT", 3306)),
    "user": os.getenv("DB_USER") or os.getenv("MYSQLUSER", "root"),
    "password": os.getenv("DB_PASSWORD") or os.getenv("MYSQLPASSWORD", ""),
    "database": os.getenv("DB_NAME") or os.getenv("MYSQLDATABASE", "student_management"),
}

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def get_db_connection():
    """
    Opens a fresh MySQL connection for a single request.
    Raises mysql.connector.Error if the connection fails, which the
    calling route is responsible for catching.
    """
    return mysql.connector.connect(**DB_CONFIG)


# ---------------------------------------------------------------------------
# GET /api/students  ->  MySQL SELECT
# ---------------------------------------------------------------------------
@app.route("/api/students", methods=["GET"])
def get_students():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email, course FROM students ORDER BY id")
        students = cursor.fetchall()
        cursor.close()
        return jsonify(students), 200

    except mysql.connector.Error as db_err:
        app.logger.error(f"Database error on GET /api/students: {db_err}")
        return jsonify({
            "success": False,
            "message": "Unable to load students. Database connection failed."
        }), 500

    except Exception as err:
        app.logger.error(f"Unexpected error on GET /api/students: {err}")
        return jsonify({
            "success": False,
            "message": "Something went wrong while loading students."
        }), 500

    finally:
        if conn and conn.is_connected():
            conn.close()


# ---------------------------------------------------------------------------
# POST /api/students  ->  Validate -> MySQL INSERT
# ---------------------------------------------------------------------------
@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "message": "No data received. Send a valid JSON body."}), 400

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    course = (data.get("course") or "").strip()

    # ---- Validation ----
    if not name or not email or not course:
        return jsonify({"success": False, "message": "name, email and course are all required."}), 400

    if not EMAIL_PATTERN.match(email):
        return jsonify({"success": False, "message": "Please provide a valid email address."}), 400

    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
            (name, email, course),
        )
        conn.commit()
        new_id = cursor.lastrowid
        cursor.close()

        new_student = {"id": new_id, "name": name, "email": email, "course": course}
        return jsonify({
            "success": True,
            "message": "Student added successfully",
            "student": new_student,
        }), 201

    except mysql.connector.Error as db_err:
        # Duplicate email -> MySQL error 1062 (unique constraint violation)
        if db_err.errno == errorcode.ER_DUP_ENTRY:
            return jsonify({
                "success": False,
                "message": "A student with this email already exists."
            }), 409

        app.logger.error(f"Database error on POST /api/students: {db_err}")
        return jsonify({
            "success": False,
            "message": "Unable to save student. Database operation failed."
        }), 500

    except Exception as err:
        app.logger.error(f"Unexpected error on POST /api/students: {err}")
        return jsonify({
            "success": False,
            "message": "Something went wrong while saving the student."
        }), 500

    finally:
        if conn and conn.is_connected():
            conn.close()


# ---------------------------------------------------------------------------
# POST /api/predict  ->  Validate -> ML Model -> JSON Response
# Uses the model that was already loaded at startup (see load_model() above)
# — this route never reloads the model from disk.
# ---------------------------------------------------------------------------
@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"success": False, "error": "No data received. Send a valid JSON body."}), 400

    try:
        result = predict_churn(data)
        return jsonify({
            "success": True,
            "prediction": result["prediction"],
            "churn_probability": result["churn_probability"],
        }), 200

    except InvalidPredictionInput as val_err:
        return jsonify({"success": False, "error": str(val_err)}), 400

    except Exception as err:
        app.logger.error(f"Unexpected error on POST /api/predict: {err}")
        return jsonify({
            "success": False,
            "error": "Prediction failed due to a server error."
        }), 500


# ---------------------------------------------------------------------------
# Consistent JSON error responses for routing-level errors.
# Without these, Flask returns its default HTML error pages, which breaks
# the JSON contract that Postman/React expect from every response.
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "success": False,
        "message": "The requested endpoint does not exist."
    }), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "success": False,
        "message": "This HTTP method is not allowed for this endpoint."
    }), 405


@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "success": False,
        "message": "An unexpected server error occurred."
    }), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "0.0.0.0")
    debug = os.getenv("FLASK_DEBUG", "false").lower() in ("true", "1")
    app.run(host=host, port=port, debug=debug)

