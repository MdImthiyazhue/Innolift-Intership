import { useState } from "react";

// Task 01 — Name Preview
// Concepts: useState · Controlled Components · onChange · Conditional Rendering
function NamePreview() {
  const [name, setName] = useState("");

  const handleChange = (e) => {
    setName(e.target.value);
  };

  return (
    <div className="card">
      <p className="card-label">Task 01</p>
      <h2 className="card-title">Name Preview</h2>

      <input
        type="text"
        placeholder="Type your name..."
        value={name}
        onChange={handleChange}
      />

      <p className="greeting">
        {name.trim() ? `Hello, ${name.trim()}!` : "Hello, Guest!"}
        <span className="emoji">{name.trim() ? " 👋" : " 👤"}</span>
      </p>
    </div>
  );
}

export default NamePreview;
