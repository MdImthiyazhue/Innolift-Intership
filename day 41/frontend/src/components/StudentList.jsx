import { useEffect, useState } from "react";

/**
 * StudentList
 *
 * This component contains NO hardcoded student data.
 * All data is fetched from the Flask backend at GET /api/students.
 *
 * Flow:
 *   1. Component mounts -> useEffect runs once (empty dependency array)
 *   2. fetch('/api/students') sends an HTTP GET request to Flask
 *      (Vite's dev server proxies /api -> http://127.0.0.1:5000)
 *   3. Flask returns a JSON array of student objects
 *   4. response.json() parses that JSON into a JS array
 *   5. setStudents(...) stores it in React state via useState
 *   6. React re-renders the component, and the table below fills in
 */
function StudentList() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch("/api/students")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setStudents(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []); // empty array = run once, when the component first mounts

  if (loading) {
    return <p className="status">Loading students from the backend...</p>;
  }

  if (error) {
    return (
      <p className="status error">
        Could not load students: {error}. Is the Flask server running on port 5000?
      </p>
    );
  }

  return (
    <div className="table-wrapper">
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
          {students.map((student) => (
            <tr key={student.id}>
              <td data-label="ID">{student.id}</td>
              <td data-label="Name">{student.name}</td>
              <td data-label="Email">{student.email}</td>
              <td data-label="Course">{student.course}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default StudentList;
