import StudentList from "./components/StudentList.jsx";

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Day 41 — Frontend ↔ Backend Integration</h1>
        <p>Student data below is fetched live from the Flask API. Nothing is hardcoded.</p>
      </header>
      <StudentList />
    </div>
  );
}

export default App;
