# Day 33 – Backend Technology 3

**Innolift Ventures – Crescent Batch 1 | Full Stack AI Developer Internship**
**Student:** Mohamed Imthiyaz

## 📌 Objective
Extend the Day 32 portfolio site with more functionality and better CSS design, and finalize the backend framework (Node.js/Express vs Flask) to use for the final project.

## ✅ Tasks Covered
- [x] Added more functionality:
  - New **Projects** page (`/projects`) powered by a JSON API (`GET /api/projects`)
  - Working **Contact form** that submits via `POST /contact` and returns a confirmation page
  - **Dark mode toggle** (persisted with `localStorage`)
- [x] Added more CSS design:
  - CSS variables for light/dark themes
  - Sticky, animated navbar with active-link underline
  - Card-hover animations, project grid layout, fade-in page transitions
  - Responsive layout with a mobile breakpoint (`@media max-width: 640px`)
- [x] Chose a backend for the final project: **Node.js + Express** (reasoning in the Day 33 report)

## 📂 Project Structure
```
day33/
├── server.js              # Express server, routes, JSON API, form handling
├── package.json
├── public/
│   ├── home.html
│   ├── about.html
│   ├── projects.html        # NEW
│   ├── contact.html          # updated: real POST form
│   ├── style.css              # enhanced: dark mode, animations, responsive
│   └── js/
│       ├── theme.js            # dark mode toggle
│       └── projects.js          # fetches /api/projects
└── README.md
```

## ⚙️ How to Run

1. **Install dependencies:**
   ```bash
   npm install
   ```
2. **Start the server:**
   ```bash
   node server.js
   ```
   or
   ```bash
   npm start
   ```
3. **Open in your browser:**
   - Home: http://localhost:3000/
   - About: http://localhost:3000/about
   - Projects: http://localhost:3000/projects
   - Contact: http://localhost:3000/contact
   - Text response demo: http://localhost:3000/api/greet
   - JSON API: http://localhost:3000/api/projects
4. Try the **dark mode toggle** button in the navbar, and submit the **contact form** to see the POST route respond with a confirmation page.
5. Press `Ctrl + C` to stop the server.

## 🧩 Backend Decision: Node.js/Express vs Flask
For the final project, I'm going with **Node.js + Express**, because:
- I've already built the routing, static file serving, and API layer for this project in Express (Days 32–33), so continuing keeps momentum.
- JavaScript on both frontend and backend keeps the codebase in a single language.
- Express's middleware model (`express.static`, `express.urlencoded`, `express.json`) made it quick to add new features like the contact form and JSON API without extra setup.
- npm's ecosystem gives easy access to libraries I may need later (auth, database drivers, etc.).

## 🧠 What I Learned
- How to create a JSON API route with `res.json()` and consume it in the browser with `fetch()`.
- Handling form submissions on the backend with `express.urlencoded({ extended: true })` and `req.body`.
- Using CSS custom properties (`--variables`) to build a toggleable dark/light theme.
- Adding simple CSS animations/transitions (`@keyframes`, `transition`) for a more polished feel.
- Writing a mobile-responsive layout with a `@media` breakpoint.
- Weighing trade-offs between Node.js/Express and Flask for a final project decision.
