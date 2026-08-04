/**
 * Day 34 - REST API & Middlewares
 * Innolift Ventures - Full Stack AI Developer Internship
 *
 * New on Day 34:
 *  1. A full REST API for "projects" using all four core HTTP methods:
 *       GET     /api/projects       -> list all projects
 *       GET     /api/projects/:id   -> get a single project
 *       POST    /api/projects       -> create a new project
 *       PUT     /api/projects/:id   -> update an existing project
 *       DELETE  /api/projects/:id   -> remove a project
 *  2. Custom middlewares:
 *       - requestLogger   -> logs method, URL, and timestamp for every request
 *       - validateProject -> checks that POST/PUT bodies contain a title & description
 *       - notFoundHandler -> catches unmatched routes (404)
 *       - errorHandler    -> centralized error-handling middleware (4 args)
 */

const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// ---------------------------------------------------------------
// Built-in middleware: parse JSON and form bodies
// ---------------------------------------------------------------
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ---------------------------------------------------------------
// CUSTOM MIDDLEWARE #1: request logger
// Runs on every incoming request, then calls next() to continue.
// ---------------------------------------------------------------
function requestLogger(req, res, next) {
  const timestamp = new Date().toISOString();
  console.log(`[${timestamp}] ${req.method} ${req.originalUrl}`);
  next();
}
app.use(requestLogger);

// Serve static assets (CSS, JS, HTML pages) from /public
app.use(express.static(path.join(__dirname, "public")));

// ---------------------------------------------------------------
// In-memory "database" of projects
// ---------------------------------------------------------------
let projects = [
  {
    id: 1,
    title: "ShopIQ — Customer Churn Prediction",
    description:
      "Binary classification on the Telco Customer Churn dataset using Logistic Regression, Random Forest, and Gradient Boosting.",
    tags: ["Python", "scikit-learn", "ML"],
  },
  {
    id: 2,
    title: "Vehicle Image Classifier",
    description: "CNN-based vehicle image classification system built with TensorFlow/Keras on Google Colab.",
    tags: ["TensorFlow", "Keras", "CNN"],
  },
  {
    id: 3,
    title: "AwareScore Research",
    description:
      "Research framework evaluating situational and affective awareness in LLMs, presented at the BSACIST AI Summit.",
    tags: ["AI Research", "LLMs"],
  },
  {
    id: 4,
    title: "Portfolio + Express Backend",
    description: "This very site — a multi-page portfolio served with a Node.js/Express REST API backend.",
    tags: ["Node.js", "Express", "REST API"],
  },
];
let nextId = 5;

// ---------------------------------------------------------------
// CUSTOM MIDDLEWARE #2: validation, used only on POST/PUT routes
// ---------------------------------------------------------------
function validateProject(req, res, next) {
  const { title, description } = req.body;
  if (!title || !description) {
    return res.status(400).json({ error: "Both 'title' and 'description' are required." });
  }
  next();
}

// ---------------------------------------------------------------
// Plain TEXT response (kept from Day 32)
// ---------------------------------------------------------------
app.get("/api/greet", (req, res) => {
  res.send("Hello! This text response is coming live from the Express server 🚀");
});

// =================================================================
// REST API — /api/projects  (GET, POST, PUT, DELETE)
// =================================================================

// GET all projects
app.get("/api/projects", (req, res) => {
  res.json(projects);
});

// GET a single project by id
app.get("/api/projects/:id", (req, res) => {
  const project = projects.find((p) => p.id === Number(req.params.id));
  if (!project) {
    return res.status(404).json({ error: `Project with id ${req.params.id} not found.` });
  }
  res.json(project);
});

// POST -> create a new project
app.post("/api/projects", validateProject, (req, res) => {
  const { title, description, tags } = req.body;
  const newProject = {
    id: nextId++,
    title,
    description,
    tags: Array.isArray(tags) ? tags : [],
  };
  projects.push(newProject);
  res.status(201).json(newProject);
});

// PUT -> update an existing project
app.put("/api/projects/:id", validateProject, (req, res) => {
  const project = projects.find((p) => p.id === Number(req.params.id));
  if (!project) {
    return res.status(404).json({ error: `Project with id ${req.params.id} not found.` });
  }
  const { title, description, tags } = req.body;
  project.title = title;
  project.description = description;
  project.tags = Array.isArray(tags) ? tags : project.tags;
  res.json(project);
});

// DELETE -> remove a project
app.delete("/api/projects/:id", (req, res) => {
  const index = projects.findIndex((p) => p.id === Number(req.params.id));
  if (index === -1) {
    return res.status(404).json({ error: `Project with id ${req.params.id} not found.` });
  }
  const [removed] = projects.splice(index, 1);
  res.json({ message: "Project deleted.", project: removed });
});

// ---------------------------------------------------------------
// Page routes (GET) -> send HTML files
// ---------------------------------------------------------------
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "home.html"));
});

app.get("/about", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "about.html"));
});

app.get("/projects", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "projects.html"));
});

app.get("/contact", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "contact.html"));
});

// POST /contact -> handle the contact form submission
app.post("/contact", (req, res) => {
  const { name, email, message } = req.body;
  console.log("📩 New contact form submission:", { name, email, message });

  res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Message Sent | Mohamed Imthiyaz</title>
      <link rel="stylesheet" href="/style.css" />
    </head>
    <body>
      <header>
        <h1>Mohamed Imthiyaz</h1>
        <nav>
          <a href="/">Home</a>
          <a href="/about">About</a>
          <a href="/projects">Projects</a>
          <a href="/contact">Contact</a>
          <button id="theme-toggle">🌙 Dark Mode</button>
        </nav>
      </header>
      <main>
        <div class="card">
          <div class="success-box">✅ Thanks, ${name}! Your message has been received.</div>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Message:</strong> ${message}</p>
          <a class="btn" href="/">Back to Home</a>
        </div>
      </main>
      <footer>&copy; 2026 Mohamed Imthiyaz — Built with Node.js &amp; Express</footer>
      <script src="/js/theme.js"></script>
    </body>
    </html>
  `);
});

// ---------------------------------------------------------------
// CUSTOM MIDDLEWARE #3: 404 handler for unmatched routes
// ---------------------------------------------------------------
function notFoundHandler(req, res, next) {
  res.status(404).json({ error: `Route ${req.method} ${req.originalUrl} not found.` });
}
app.use(notFoundHandler);

// ---------------------------------------------------------------
// CUSTOM MIDDLEWARE #4: centralized error handler (4 args = Express
// recognizes this signature specifically for error handling)
// ---------------------------------------------------------------
function errorHandler(err, req, res, next) {
  console.error("🔥 Server error:", err.message);
  res.status(500).json({ error: "Something went wrong on the server." });
}
app.use(errorHandler);

app.listen(PORT, () => {
  console.log(`✅ Server is running at http://localhost:${PORT}`);
});
