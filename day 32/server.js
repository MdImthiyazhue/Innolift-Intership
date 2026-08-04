/**
 * Day 32 - Backend Technology 2
 * Innolift Ventures - Full Stack AI Developer Internship
 *
 * Topics covered in this file:
 *  1. Starting a first Express server using Node.js
 *  2. Sending plain text as a response
 *  3. Using the GET method to fetch a response from the server
 *  4. Sending an HTML file as a response
 *  5. Serving/rendering a CSS file (via Express static middleware)
 */

const express = require("express");
const path = require("path");

const app = express();
const PORT = 3000;

// ---------------------------------------------------------------
// Serve static assets (CSS, images, client JS) from the "public" folder.
// This is how the CSS file gets "rendered" in the browser -
// any file inside /public is automatically available, e.g. /style.css
// ---------------------------------------------------------------
app.use(express.static(path.join(__dirname, "public")));

// ---------------------------------------------------------------
// 1) Simple GET route that sends plain TEXT as a response
// ---------------------------------------------------------------
app.get("/api/greet", (req, res) => {
  res.send("Hello! This text response is coming live from the Express server 🚀");
});

// ---------------------------------------------------------------
// 2) GET route -> sends the Home page HTML file
// ---------------------------------------------------------------
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "home.html"));
});

// ---------------------------------------------------------------
// 3) GET route -> sends the About page HTML file
// ---------------------------------------------------------------
app.get("/about", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "about.html"));
});

// ---------------------------------------------------------------
// 4) GET route -> sends the Contact page HTML file
// ---------------------------------------------------------------
app.get("/contact", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "contact.html"));
});

// ---------------------------------------------------------------
// Fallback 404 route for any other path
// ---------------------------------------------------------------
app.use((req, res) => {
  res.status(404).send("404 - Page Not Found");
});

app.listen(PORT, () => {
  console.log(`✅ Server is running at http://localhost:${PORT}`);
});
