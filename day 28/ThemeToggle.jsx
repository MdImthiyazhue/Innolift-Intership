import { useState, useEffect } from "react";

// Task 02 — Theme Toggle
// Concepts: useState · Boolean State · Conditional Rendering · Dynamic Styling
function ThemeToggle() {
  const [isDark, setIsDark] = useState(false);

  // Apply/remove a "dark" class on <body> whenever isDark changes
  useEffect(() => {
    document.body.classList.toggle("dark", isDark);
  }, [isDark]);

  const toggleTheme = () => {
    setIsDark((prev) => !prev);
  };

  return (
    <div className="card">
      <p className="card-label">Task 02</p>
      <h2 className="card-title">Theme Toggle</h2>

      <div className="toggle-row">
        <span className="status-text">
          Currently in <strong>{isDark ? "Dark" : "Light"}</strong> mode
        </span>

        <button className="theme-btn" onClick={toggleTheme}>
          {isDark ? "☀️ Light Mode" : "🌙 Dark Mode"}
        </button>
      </div>
    </div>
  );
}

export default ThemeToggle;
