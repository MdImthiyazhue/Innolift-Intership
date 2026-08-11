# Day 41 — API Flow Documentation

## 1. What is the purpose of the `/api/students` endpoint?

`/api/students` is a **REST API endpoint** hosted by the Flask backend. Its job is to act
as the single source of truth for student data. When it receives a `GET` request, it looks
up the student records (in this exercise, an in-memory list — in a production system like
ShopIQ this would be a MySQL query) and sends them back to whoever asked, formatted as JSON.
The React frontend never stores or hardcodes student data itself — it only ever *asks* this
endpoint for the current data, which keeps the frontend and backend cleanly separated.

## 2. What is an HTTP Request?

An HTTP Request is a message sent from a client (the browser / React app) to a server
(Flask) asking it to do something. It has:

- A **method** — `GET` (fetch data), `POST` (create), `PUT`/`PATCH` (update), `DELETE` (remove)
- A **URL** — e.g. `/api/students`
- **Headers** — metadata like `Content-Type` or `Accept`
- An optional **body** — data sent with the request (used in POST/PUT, not needed for our GET)

In this project, React sends a `GET` request to `/api/students` with no body, because it's
only reading data, not sending any.

## 3. What is a JSON Response?

A JSON Response is the server's reply, with its body formatted as **JSON**
(JavaScript Object Notation) — a lightweight, language-independent text format for
representing structured data as key-value pairs and arrays. Flask's `jsonify()` function
converts a Python list of dictionaries into a JSON-formatted HTTP response and automatically
sets the `Content-Type: application/json` header, so the browser knows how to interpret it.

Example response body from `/api/students`:

```json
[
  { "id": 1, "name": "Mohamed Imthiyas", "email": "imthiyas@example.com", "course": "AI & Data Science" },
  { "id": 2, "name": "Aisha Fathima", "email": "aisha.fathima@example.com", "course": "Computer Science" }
]
```

## 4. How does data travel from Flask Backend → React Frontend?

1. The Flask server holds/queries the student data.
2. React's `useEffect()` runs on component mount and calls `fetch('/api/students')`.
3. The browser sends an HTTP GET request over the network to the Flask server.
4. Flask's route handler runs, builds the list of students, and returns it via
   `jsonify(STUDENTS)` — this serializes the Python objects into a JSON string and sends it
   back as the HTTP response body.
5. The browser receives the response. React calls `response.json()`, which parses the JSON
   text back into a JavaScript array of objects.
6. That array is passed into `setStudents(data)`, updating React state via `useState()`.
7. Because state changed, React re-renders the component, and the table/cards on screen
   now display the real backend data.

## Architecture / Data Flow Diagram

```
┌─────────────────────┐                         ┌──────────────────────┐
│   React Frontend     │                        │   Flask Backend       │
│   (localhost:5173)   │                        │   (localhost:5000)    │
│                       │                        │                       │
│  ┌─────────────────┐  │   1. GET request       │  ┌─────────────────┐  │
│  │  useEffect()     │──┼───────────────────────▶│  │ /api/students   │  │
│  │  runs on mount   │  │   fetch('/api/students')  │  route handler  │  │
│  └─────────────────┘  │                        │  └────────┬────────┘  │
│           ▲            │                        │           │           │
│           │             │                        │           ▼           │
│  ┌─────────────────┐  │   4. JSON response      │  ┌─────────────────┐  │
│  │  useState()      │◀─┼────────────────────────│  │  jsonify(data)  │  │
│  │  setStudents()   │  │   2. response.json()   │  │  builds JSON    │  │
│  └────────┬────────┘  │      (parses JSON)      │  └─────────────────┘  │
│           │             │                        │                       │
│           ▼             │                        │                       │
│  ┌─────────────────┐  │                        │                       │
│  │  React UI        │  │   3. state updates,    │                       │
│  │  (Table/Cards)    │  │      component re-     │                       │
│  │  renders data     │  │      renders           │                       │
│  └─────────────────┘  │                        │                       │
└─────────────────────┘                         └──────────────────────┘
```

### Step-by-step sequence

```
Flask API  →  JSON Response  →  React fetch()  →  response.json()  →  useState()  →  React UI
```

1. **Flask API** — `GET /api/students` route executes, gathers student records.
2. **JSON Response** — `jsonify()` serializes Python data into JSON, sent over HTTP.
3. **React fetch()** — `useEffect()` triggers `fetch('/api/students')` on component mount.
4. **response.json()** — Parses the raw JSON text into a usable JavaScript array.
5. **useState()** — `setStudents(data)` stores the parsed array in component state.
6. **React UI** — The table/card component maps over `students` and renders each row —
   with zero hardcoded data, entirely driven by what Flask returned.

## Today's Challenge — What actually happens end to end?

When the `StudentList` component mounts:

1. `useEffect(() => { ... }, [])` fires exactly once because its dependency array is empty.
2. `fetch('/api/students')` opens a network connection to the Flask server (via Vite's dev
   proxy, so no CORS issues locally).
3. While waiting, `loading` state is `true`, so the UI shows "Loading students...".
4. Flask's route handler builds the JSON array and returns it with a `200 OK` status.
5. The `fetch` promise resolves with a `Response` object; `.json()` reads and parses the
   body asynchronously (this itself returns a promise).
6. Once parsed, `setStudents(data)` and `setLoading(false)` are called.
7. React schedules a re-render because state changed.
8. On re-render, `loading` is now `false`, so instead of the loading message, the table
   renders — `students.map(...)` produces one `<tr>` per student, with each cell reading
   directly from the fetched data (`student.id`, `student.name`, etc.).
9. If the fetch fails (server down, network error, non-2xx status), the `.catch()` block
   sets `error` state instead, and the UI shows an error message rather than crashing.

This is the complete Frontend → Backend → API → JSON → Frontend loop.
