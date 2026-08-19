import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "http://localhost:5000/api/students";

function App() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [form, setForm] = useState({ name: "", email: "", course: "" });
  const [formError, setFormError] = useState("");
  const [successMsg, setSuccessMsg] = useState("");
  const [submitting, setSubmitting] = useState(false);

  // ---------- GET /api/students -> MySQL SELECT (via Flask) ----------
  const fetchStudents = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch(API_URL);
      const data = await response.json();

      if (!response.ok) {
        // Flask returns { success: false, message: "..." } on DB errors
        throw new Error(data.message || `Server responded with status ${response.status}`);
      }

      setStudents(data);
    } catch (err) {
      console.error("Fetch error:", err);
      setError("Unable to load students.");
    } finally {
      // Loading always stops, whether the request succeeded or failed
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // ---------- POST /api/students -> Validate -> MySQL INSERT (via Flask) ----------
  const handleSubmit = async (e) => {
    e.preventDefault();
    setFormError("");
    setSuccessMsg("");

    if (!form.name.trim() || !form.email.trim() || !form.course.trim()) {
      setFormError("All fields are required.");
      return;
    }

    setSubmitting(true);
    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });

      const result = await response.json();

      if (!response.ok || !result.success) {
        // Covers validation errors, duplicate email, and DB failures
        throw new Error(result.message || "Failed to add student.");
      }

      // Success: update list instantly, no page refresh needed
      setStudents((prev) => [...prev, result.student]);
      setSuccessMsg(result.message || "Student added successfully!");
      setForm({ name: "", email: "", course: "" });
    } catch (err) {
      console.error("Submit error:", err);
      setFormError(err.message || "Unable to save student. Please try again.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="container">
      <h1>Student Management</h1>

      {/* ---------------- Add Student Form ---------------- */}
      <form className="student-form" onSubmit={handleSubmit}>
        <h2>Add Student</h2>
        <input
          type="text"
          name="name"
          placeholder="Full Name"
          value={form.name}
          onChange={handleChange}
        />
        <input
          type="email"
          name="email"
          placeholder="Email Address"
          value={form.email}
          onChange={handleChange}
        />
        <input
          type="text"
          name="course"
          placeholder="Course"
          value={form.course}
          onChange={handleChange}
        />
        <button type="submit" disabled={submitting}>
          {submitting ? "Submitting..." : "Add Student"}
        </button>

        {formError && <p className="error-text">{formError}</p>}
        {successMsg && <p className="success-text">{successMsg}</p>}
      </form>

      {/* ---------------- Student List ---------------- */}
      <h2>Student List</h2>

      {loading && <p className="info-text">Loading students...</p>}

      {!loading && error && <p className="error-text">{error}</p>}

      {!loading && !error && students.length === 0 && (
        <p className="empty-text">No students found.</p>
      )}

      {!loading && !error && students.length > 0 && (
        <table className="student-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Email</th>
              <th>Course</th>
            </tr>
          </thead>
          <tbody>
            {students.map((s) => (
              <tr key={s.id}>
                <td>{s.id}</td>
                <td>{s.name}</td>
                <td>{s.email}</td>
                <td>{s.course}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}

      <button className="retry-btn" onClick={fetchStudents}>
        Refresh List
      </button>
    </div>
  );
}

export default App;
