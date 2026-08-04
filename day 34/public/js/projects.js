// Day 34 - REST API & Middlewares
// This script talks to the Express REST API at /api/projects using all
// four HTTP methods: GET (list), POST (create), PUT (update), DELETE (remove).

const grid = document.getElementById("projects-grid");
const form = document.getElementById("add-project-form");
const statusMsg = document.getElementById("status-msg");

function showStatus(text, type = "success") {
  statusMsg.innerHTML = `<div class="success-box ${type === "error" ? "error-box" : ""}">${text}</div>`;
  setTimeout(() => {
    statusMsg.innerHTML = "";
  }, 3000);
}

// ---------- GET: load and render all projects ----------
function loadProjects() {
  fetch("/api/projects")
    .then((res) => res.json())
    .then((projects) => {
      grid.innerHTML = "";
      if (projects.length === 0) {
        grid.innerHTML = '<p class="skeleton">No projects yet. Add one above!</p>';
        return;
      }
      projects.forEach(renderCard);
    })
    .catch(() => {
      grid.innerHTML = '<p class="skeleton">Could not load projects right now.</p>';
    });
}

function renderCard(p) {
  const card = document.createElement("div");
  card.className = "project-card";
  card.dataset.id = p.id;
  card.innerHTML = `
    <h3 class="p-title">${p.title}</h3>
    <p class="p-desc">${p.description}</p>
    <div class="p-tags">${p.tags.map((t) => `<span class="tag">${t}</span>`).join("")}</div>
    <div class="card-actions">
      <button class="btn-small edit-btn">✏️ Edit (PUT)</button>
      <button class="btn-small delete-btn">🗑️ Delete</button>
    </div>
  `;

  // ---------- DELETE ----------
  card.querySelector(".delete-btn").addEventListener("click", () => {
    if (!confirm(`Delete "${p.title}"?`)) return;
    fetch(`/api/projects/${p.id}`, { method: "DELETE" })
      .then((res) => {
        if (!res.ok) throw new Error("Delete failed");
        return res.json();
      })
      .then(() => {
        showStatus(`🗑️ "${p.title}" deleted.`);
        loadProjects();
      })
      .catch(() => showStatus("Failed to delete project.", "error"));
  });

  // ---------- PUT (inline edit) ----------
  card.querySelector(".edit-btn").addEventListener("click", () => {
    const newTitle = prompt("Edit title:", p.title);
    if (newTitle === null) return;
    const newDesc = prompt("Edit description:", p.description);
    if (newDesc === null) return;

    fetch(`/api/projects/${p.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: newTitle, description: newDesc, tags: p.tags }),
    })
      .then((res) => {
        if (!res.ok) throw new Error("Update failed");
        return res.json();
      })
      .then(() => {
        showStatus(`✏️ "${newTitle}" updated.`);
        loadProjects();
      })
      .catch(() => showStatus("Failed to update project.", "error"));
  });

  grid.appendChild(card);
}

// ---------- POST: add a new project ----------
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.getElementById("title").value.trim();
  const description = document.getElementById("description").value.trim();
  const tags = document
    .getElementById("tags")
    .value.split(",")
    .map((t) => t.trim())
    .filter(Boolean);

  fetch("/api/projects", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title, description, tags }),
  })
    .then((res) => {
      if (!res.ok) return res.json().then((err) => Promise.reject(err));
      return res.json();
    })
    .then(() => {
      showStatus(`✅ "${title}" added.`);
      form.reset();
      loadProjects();
    })
    .catch((err) => showStatus(err.error || "Failed to add project.", "error"));
});

loadProjects();
