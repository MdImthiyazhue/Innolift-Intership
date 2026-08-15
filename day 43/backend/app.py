from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory student data (acts as our temporary database)
students = [
    {"id": 1, "name": "Arun Kumar", "roll_no": "23BAI001", "department": "AI & DS"},
    {"id": 2, "name": "Divya Sri", "roll_no": "23BAI002", "department": "AI & DS"},
    {"id": 3, "name": "Mohamed Imthiyaz", "roll_no": "23BAI003", "department": "AI & DS"},
]

next_id = 4


@app.route("/api/students", methods=["GET"])
def get_students():
    """
    Returns the full list of students.
    NOTE: To test the EMPTY STATE on the frontend, temporarily return
    jsonify([]) instead of jsonify(students).
    """
    return jsonify(students), 200


@app.route("/api/students", methods=["POST"])
def add_student():
    global next_id
    data = request.get_json(silent=True)

    # ---- Server-side validation ----
    if not data:
        return jsonify({"error": "No data received. Send a valid JSON body."}), 400

    name = data.get("name", "").strip()
    roll_no = data.get("roll_no", "").strip()
    department = data.get("department", "").strip()

    if not name or not roll_no or not department:
        return jsonify({"error": "name, roll_no and department are all required."}), 400

    new_student = {
        "id": next_id,
        "name": name,
        "roll_no": roll_no,
        "department": department,
    }
    students.append(new_student)
    next_id += 1

    return jsonify({"message": "Student added successfully", "student": new_student}), 201


if __name__ == "__main__":
    # Run on port 5000 -> matches the React fetch URLs below
    app.run(debug=True, port=5000)
