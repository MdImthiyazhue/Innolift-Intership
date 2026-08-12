import StudentForm from "./StudentForm.jsx";

export default function App() {
  return (
    <div className="page">
      <header className="page-header">
        <h1>Day 42 — POST API &amp; Form Submission</h1>
        <p>React Form → fetch() → Flask API → JSON Response</p>
      </header>
      <StudentForm />
    </div>
  );
}
