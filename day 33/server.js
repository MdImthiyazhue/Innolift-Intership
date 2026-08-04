/**
 * Day 33 - Backend Technology 3
 * Innolift Ventures - Full Stack AI Developer Internship
 *
 * New on Day 33:
 *  1. Added more functionality to the site:
 *     - A "Projects" page backed by a JSON API route (GET /api/projects)
 *     - A working Contact form that POSTs data to the server
 *     - Dark mode toggle (client-side, CSS variables)
 *  2. More CSS design: sticky nav, hover/active states, card-grid layout,
 *     animations, and responsive layout for mobile.
 *  3. Backend choice for the final project: Node.js + Express (see README
 *     / Day 33 report for the reasoning).
 */

const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// Parse form-encoded data from the Contact form (POST)
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Serve static assets (CSS, JS, images) from /public
app.use(express.static(path.join(__dirname, "public")));

// ---------------------------------------------------------------
// Plain TEXT response (kept from Day 32)
// ---------------------------------------------------------------
app.get("/api/greet", (req, res) => {
  res.send("Hello! This text response is coming live from the Express server 🚀");
});

// ---------------------------------------------------------------
// JSON API route -> powers the Projects page via fetch()
// ---------------------------------------------------------------
const projects = [
  {
    title: "ShopIQ — Customer Churn Prediction",
    description:
      "Binary classification on the Telco Customer Churn dataset using Logistic Regression, Random Forest, and Gradient Boosting.",
    tags: ["Python", "scikit-learn", "ML"],
  },
  {
    title: "Vehicle Image Classifier",
    description: "CNN-based vehicle image classification system built with TensorFlow/Keras on Google Colab.",
    tags: ["TensorFlow", "Keras", "CNN"],
  },
  {
    title: "AwareScore Research",
    description:
      "Research framework evaluating situational and affective awareness in LLMs, presented at the BSACIST AI Summit.",
    tags: ["AI Research", "LLMs"],
  },
  {
    title: "Portfolio + Express Backend",
    description: "This very site — a multi-page portfolio served with a Node.js/Express backend (Day 32–33).",
    tags: ["Node.js", "Express"],
  },
];

app.get("/api/projects", (req, res) => {
  res.json(projects);
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

// ---------------------------------------------------------------
// POST /contact -> new functionality: handle the contact form
// submission and respond with a confirmation page
// ---------------------------------------------------------------
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
// Fallback 404 route
// ---------------------------------------------------------------
app.use((req, res) => {
  res.status(404).send("404 - Page Not Found");
});

app.listen(PORT, () => {
  console.log(`✅ Server is running at http://localhost:${PORT}`);
});
