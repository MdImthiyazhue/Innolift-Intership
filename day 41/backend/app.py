"""
Day 41 - Flask Backend
Exposes GET /api/students which returns a JSON array of student records.
This is the "source of truth" for student data - the React frontend
never hardcodes this data, it only ever reads it from this endpoint.
"""

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# CORS is required because React (http://localhost:5173) and Flask
# (http://localhost:5000) run on different origins during development.
# Without this, the browser blocks the fetch() call from React.
CORS(app)

# In a real project this would come from MySQL (see ShopIQ backend),
# but for this exercise we keep it in-memory to focus purely on the
# Flask -> React data flow.
STUDENTS = [
    {
        "id": 1,
        "name": "Mohamed Imthiyas",
        "email": "imthiyas@example.com",
        "course": "AI & Data Science",
    },
    {
        "id": 2,
        "name": "Aisha Fathima",
        "email": "aisha.fathima@example.com",
        "course": "Computer Science",
    },
    {
        "id": 3,
        "name": "Rahul Krishnan",
        "email": "rahul.krishnan@example.com",
        "course": "Information Technology",
    },
    {
        "id": 4,
        "name": "Sneha Priya",
        "email": "sneha.priya@example.com",
        "course": "Electronics & Communication",
    },
    {
        "id": 5,
        "name": "Arjun Prakash",
        "email": "arjun.prakash@example.com",
        "course": "Mechanical Engineering",
    },
    {
        "id": 6,
        "name": "Fathima Zahra",
        "email": "fathima.zahra@example.com",
        "course": "AI & Data Science",
    },
]


@app.route("/api/students", methods=["GET"])
def get_students():
    """
    Returns all student records as JSON.

    Flow:
      1. React calls fetch('/api/students')
      2. Flask runs this function
      3. jsonify() converts the Python list of dicts into a JSON
         HTTP response with Content-Type: application/json
      4. React receives the response and parses it with response.json()
    """
    return jsonify(STUDENTS), 200


@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Day 41 Flask API is running"}), 200


if __name__ == "__main__":
    # debug=True gives auto-reload + detailed error pages during development
    app.run(debug=True, port=5000)
