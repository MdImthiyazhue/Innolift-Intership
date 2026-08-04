# Day 32 – Backend Technology 2

**Innolift Ventures – Crescent Batch 1 | Full Stack AI Developer Internship**
**Student:** Mohamed Imthiyaz

## 📌 Objective
Build a simple portfolio website (Home, About, Contact pages) and serve it using a Node.js + Express backend server.

## ✅ Tasks Covered
- [x] Create a simple portfolio website with Home, About, Contact pages
- [x] Start first Express server using Node.js
- [x] Pass text as a response (`/api/greet`)
- [x] Use GET method to get a response from the server
- [x] Send HTML file as a response (`res.sendFile`)
- [x] Render CSS file (via `express.static`)

## 📂 Project Structure
```
day32/
├── server.js          # Express server & routes
├── package.json        # Project metadata & dependencies
├── public/
│   ├── home.html        # Home page
│   ├── about.html        # About page
│   ├── contact.html      # Contact page
│   └── style.css          # Shared stylesheet
└── README.md
```

## ⚙️ How to Run

1. **Install dependencies** (only Express is required):
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

3. **Open the site in your browser:**
   - Home: http://localhost:3000/
   - About: http://localhost:3000/about
   - Contact: http://localhost:3000/contact
   - Text response demo: http://localhost:3000/api/greet

4. Press `Ctrl + C` in the terminal to stop the server.

## 🧠 What I Learned
- How to initialize a Node.js project and install Express (`npm init`, `npm install express`).
- How Express routes work with the GET method (`app.get(path, handler)`).
- The difference between `res.send()` (plain text/HTML string) and `res.sendFile()` (serving a full HTML file from disk).
- How `express.static()` middleware serves static assets like CSS files directly by their file path.
- Structuring a small multi-page site with a `public` folder convention.
