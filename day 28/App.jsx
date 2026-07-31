import NamePreview from "./NamePreview";
import ThemeToggle from "./ThemeToggle";
import "./App.css";

function App() {
  return (
    <div className="page">
      <p className="eyebrow">Day 28 · Innolift Ventures</p>
      <h1>Hooks &amp; useState</h1>
      <p className="subtitle">
        Two small components, one core idea: state drives what the screen shows.
      </p>

      <NamePreview />
      <ThemeToggle />

      <footer>Built with useState · Controlled Components · Conditional Rendering</footer>
    </div>
  );
}

export default App;
