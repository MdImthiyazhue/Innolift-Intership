import { useEffect, useState } from "react";

const API_URL = "http://127.0.0.1:5000/api/students";

export default function StudentForm() {
  // ---- TASK 02: controlled form fields ----
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    course: "",
  });

  // ---- TASK 04: loading state ----
  const [loading, setLoading] = useState(false);

  // Feedback + data
  const [students, setStudents] = useState([]);
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  // Load the existing student list once on mount (GET, from Day 41)
  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => setStudents(data))
      .catch(() => setErrorMessage("Could not load existing students."));
  }, []);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  // ---- TASK 03: connect form to Flask with fetch() ----
  const handleSubmit = async (event) => {
    event.preventDefault(); // stop the default full-page form submission

    setErrorMessage("");
    setSuccessMessage("");
    setLoading(true); // TASK 04: show spinner / disable button

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const result = await response.json();

      if (!response.ok || !result.success) {
        setErrorMessage(result.message || "Something went wrong. Please try again.");
        return;
      }

      // ---- TASK 05: update UI after success ----
      setStudents((prev) => [...prev, result.student]); // add new student, no refresh
      setFormData({ name: "", email: "", course: "" }); // clear form fields
      setSuccessMessage(`✅ ${result.student.name} was added successfully!`);
    } catch (err) {
      setErrorMessage("Could not reach the server. Is Flask running on port 5000?");
    } finally {
      setLoading(false); // TASK 04: hide spinner / re-enable button
    }
  };

  return (
    <div className="container">
      <section className="card">
        <h2>Add a New Student</h2>

        <form onSubmit={handleSubmit} noValidate>
          <div className="field">
            <label htmlFor="name">Student Name</label>
            <input
              id="name"
              name="name"
              type="text"
              value={formData.name}
              onChange={handleChange}
              placeholder="e.g. Imthiyaz Ahmed"
              disabled={loading}
            />
          </div>

          <div className="field">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              name="email"
              type="email"
              value={formData.email}
              onChange={handleChange}
              placeholder="e.g. imthiyaz@example.com"
              disabled={loading}
            />
          </div>

          <div className="field">
            <label htmlFor="course">Course</label>
            <input
              id="course"
              name="course"
              type="text"
              value={formData.course}
              onChange={handleChange}
              placeholder="e.g. AI & Data Science"
              disabled={loading}
            />
          </div>

          <button type="submit" disabled={loading} className="submit-btn">
            {loading ? (
              <>
                <span className="spinner" aria-hidden="true"></span>
                Saving...
              </>
            ) : (
              "Add Student"
            )}
          </button>
        </form>

        {successMessage && <p className="success-msg">{successMessage}</p>}
        {errorMessage && <p className="error-msg">{errorMessage}</p>}
      </section>

      <section className="card">
        <h2>Student List ({students.length})</h2>
        {students.length === 0 ? (
          <p className="empty-state">No students yet. Add one using the form.</p>
        ) : (
          <ul className="student-list">
            {students.map((s) => (
              <li key={s.id} className="student-item">
                <span className="student-name">{s.name}</span>
                <span className="student-email">{s.email}</span>
                <span className="student-course">{s.course}</span>
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
}
