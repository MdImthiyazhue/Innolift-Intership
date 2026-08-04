// Day 33 - Dark mode toggle (persists using localStorage)
(function () {
  const root = document.documentElement;
  const stored = localStorage.getItem("theme");
  if (stored === "dark") {
    root.setAttribute("data-theme", "dark");
  }

  document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("theme-toggle");
    updateLabel();

    btn.addEventListener("click", () => {
      const isDark = root.getAttribute("data-theme") === "dark";
      if (isDark) {
        root.removeAttribute("data-theme");
        localStorage.setItem("theme", "light");
      } else {
        root.setAttribute("data-theme", "dark");
        localStorage.setItem("theme", "dark");
      }
      updateLabel();
    });

    function updateLabel() {
      const isDark = root.getAttribute("data-theme") === "dark";
      btn.textContent = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
    }
  });
})();
