import Header from "./components/Header";
import StudentCard from "./components/StudentCard";
import Footer from "./components/Footer";

function App() {
  return (
    <div className="container">

      <Header />

      <StudentCard
  name="Mohamed Imthiyas"
  department="Artificial Intelligence & Data Science"
  college="B.S. Abdur Rahman Crescent Institute"
  email="imthiyas@example.com"
  skills={["Python", "Machine Learning", "React", "SQL"]}
/>

<StudentCard
  name="Aisha Rahman"
  department="Computer Science"
  college="Anna University"
  email="aisha@example.com"
  skills={["Java", "HTML", "CSS", "JavaScript"]}
/>

<StudentCard
  name="Rahul Kumar"
  department="Information Technology"
  college="SRM University"
  email="rahul@example.com"
  skills={["C++", "React", "Node.js", "MongoDB"]}
/>

      <Footer />

    </div>
  );
}

export default App;