# Day 34 – REST API & Middlewares

**Innolift Ventures – Crescent Batch 1 | Full Stack AI Developer Internship**
**Student:** Mohamed Imthiyaz

## 📌 Objective
Build a real REST API for the portfolio's Projects section using all four core HTTP methods (GET, POST, PUT, DELETE), and introduce custom Express middlewares for logging, validation, and error handling.

## ✅ Tasks Covered
- [x] Used different HTTP methods (GET, POST, PUT, DELETE) on the same resource (`/api/projects`)
- [x] Used **POST** to create new project data
- [x] Used **PUT** to update existing project data
- [x] Used **DELETE** to remove project data
- [x] Added custom **middlewares**: request logger, body validation, 404 handler, centralized error handler

## 🔌 REST API Reference — `/api/projects`

| Method | Route | Description |
|---|---|---|
| GET | `/api/projects` | List all projects |
| GET | `/api/projects/:id` | Get a single project by id |
| POST | `/api/projects` | Create a new project (`title`, `description`, `tags[]`) |
| PUT | `/api/projects/:id` | Update an existing project |
| DELETE | `/api/projects/:id` | Delete a project |

**Example — create a project:**
```bash
curl -X POST http://localhost:3000/api/projects \
  -H "Content-Type: application/json" \
  -d '{"title":"New Project","description":"Details here","tags":["Node.js"]}'
```

**Example — update a project:**
```bash
curl -X PUT http://localhost:3000/api/projects/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Title","description":"Updated details","tags":["Express"]}'
```

**Example — delete a project:**
```bash
curl -X DELETE http://localhost:3000/api/projects/1
```

## 🧩 Custom Middlewares
| Middleware | Purpose |
|---|---|
| `requestLogger` | Logs the timestamp, HTTP method, and URL of every incoming request |
| `validateProject` | Runs before POST/PUT — rejects requests missing `title` or `description` with a `400` |
| `notFoundHandler` | Catches any unmatched route and returns a JSON `404` |
| `errorHandler` | Centralized 4-argument error-handling middleware that catches thrown/forwarded errors and returns a `500` |

## 📂 Project Structure
```
day34/
├── server.js              # REST API routes + custom middlewares
├── package.json
├── public/
│   ├── home.html
│   ├── about.html
│   ├── projects.html        # updated: full CRUD UI (add/edit/delete)
│   ├── contact.html
│   ├── style.css
│   └── js/
│       ├── theme.js
│       └── projects.js        # GET/POST/PUT/DELETE via fetch()
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
3. **Open in your browser:** http://localhost:3000/projects
   - Fill in the "Add a New Project" form → sends a **POST** request
   - Click **Edit** on any project card → sends a **PUT** request
   - Click **Delete** on any project card → sends a **DELETE** request
   - The list itself loads via a **GET** request on page load
4. Watch the terminal — the `requestLogger` middleware prints every request as it comes in.
5. Press `Ctrl + C` to stop the server.

## 🧠 What I Learned
- The difference between GET, POST, PUT, and DELETE, and when to use each in a RESTful API.
- How Express middleware functions work: `(req, res, next)`, and how calling `next()` passes control to the next handler.
- Writing a validation middleware that can short-circuit a request with an error response before it reaches the route handler.
- The special 4-argument signature `(err, req, res, next)` that Express uses to recognize error-handling middleware.
- Building a 404 handler that runs only when no other route matched.
- Wiring a frontend (`fetch()` with different `method` values) to a REST backend for a full create/read/update/delete flow.
