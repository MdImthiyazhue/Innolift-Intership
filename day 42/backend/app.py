"""
Day 42 - Innolift Ventures Internship
POST API & Form Submission

Flask backend exposing:
    GET  /api/students        -> list all students
    POST /api/students        -> create a new student (validated)

Run:
    pip install flask flask-cors
    python app.py
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow the React dev server (different port) to call this API

# --------------------------------------------------------------------------
# In-memory "database". Restarting the server resets this list.
# In a real project this would be a MySQL table (see Day 35 schema work).
# --------------------------------------------------------------------------
students = [
    {"id": 1, "name": "Aisha Rahman", "email": "aisha@example.com", "course": "AI & Data Science"},
    {"id": 2, "name": "Karthik Iyer", "email": "karthik@example.com", "course": "Computer Science"},
]
next_id = 3


@app.route("/api/students", methods=["GET"])
def get_students():
    """Return the current list of students."""
    return jsonify(students), 200


@app.route("/api/students", methods=["POST"])
def create_student():
    """
    Accept JSON from the frontend, validate required fields,
    create a new student record, and return it.
    """
    global next_id

    data = request.get_json(silent=True)

    # Basic guard: no body / not JSON at all
    if not data:
        return jsonify({"success": False, "message": "Request body must be JSON."}), 400

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    course = (data.get("course") or "").strip()

    # Field-level validation
    missing = [field for field, value in (("name", name), ("email", email), ("course", course)) if not value]
    if missing:
        return jsonify({
            "success": False,
            "message": f"Missing required field(s): {', '.join(missing)}"
        }), 400

    if "@" not in email or "." not in email:
        return jsonify({"success": False, "message": "Please provide a valid email address."}), 400

    new_student = {
        "id": next_id,
        "name": name,
        "email": email,
        "course": course,
    }
    students.append(new_student)
    next_id += 1

    return jsonify({
        "success": True,
        "message": "Student created successfully.",
        "student": new_student
    }), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
