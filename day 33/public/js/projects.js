// Day 33 - Fetches project data from the backend (GET /api/projects)
// and dynamically renders it into the page. Demonstrates a JSON API
// endpoint plus client-side fetch() consuming it.
document.addEventListener("DOMContentLoaded", () => {
  const grid = document.getElementById("projects-grid");

  fetch("/api/projects")
    .then((res) => res.json())
    .then((projects) => {
      grid.innerHTML = "";
      projects.forEach((p) => {
        const card = document.createElement("div");
        card.className = "project-card";
        card.innerHTML = `
          <h3>${p.title}</h3>
          <p>${p.description}</p>
          <div>${p.tags.map((t) => `<span class="tag">${t}</span>`).join("")}</div>
        `;
        grid.appendChild(card);
      });
    })
    .catch(() => {
      grid.innerHTML = '<p class="skeleton">Could not load projects right now.</p>';
    });
});
