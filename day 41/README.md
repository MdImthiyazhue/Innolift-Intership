# Day 41 — Connecting Frontend to Backend

Innolift Ventures | Crescent Batch 1 Internship

React frontend + Flask backend, connected via a REST API (`GET /api/students`).
No student data is hardcoded in React — everything is fetched live from Flask.

## Project structure

```
day41-frontend-backend/
├── backend/
│   ├── app.py              # Flask app with GET /api/students
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js      # proxies /api -> Flask on :5000
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── index.css
│       └── components/
│           └── StudentList.jsx   # fetch() + useEffect() + useState()
└── docs/
    └── day-41-api-flow.md  # Task 01: API flow write-up + architecture diagram
```

## How to run

### 1. Backend (Flask)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Runs on **http://localhost:5000**. Test it directly:

```bash
curl http://localhost:5000/api/students
```

You should get back a JSON array of 6 student records.

### 2. Frontend (React + Vite)

In a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Runs on **http://localhost:5173**. The Vite dev server proxies any `/api/*` request to the
Flask server on port 5000 (see `vite.config.js`), so `fetch('/api/students')` in React just
works with no CORS setup needed on the frontend side.

Open http://localhost:5173 in your browser — the student table should populate with data
coming straight from Flask.

## What to check while testing

- With Flask **stopped**, reloading the React app should show the error state
  ("Could not load students...") instead of crashing.
- With Flask **running**, the table should show 6 rows with ID, Name, Email, Course.
- Resize the browser below ~640px width — the table collapses into a stacked card layout.
- Open DevTools → Network tab → refresh — you should see a `GET /api/students` request
  returning a `200` status with a JSON payload.
