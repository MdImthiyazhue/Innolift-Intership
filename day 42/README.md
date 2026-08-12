# Day 42 — POST API & Form Submission

Innolift Ventures | Crescent Internship

Full end-to-end flow: **React Form → fetch() → Flask API → JSON Response**

## Structure

```
day42-post-api/
├── backend/
│   ├── app.py            Flask app: GET/POST /api/students
│   └── requirements.txt
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── StudentForm.jsx   (all 5 tasks live here)
        └── index.css
```

## Run the backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```
Runs on http://127.0.0.1:5000

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```
Runs on http://127.0.0.1:5173

## What it does

1. **Flask POST API** (`POST /api/students`) — validates `name`, `email`, `course`
   are present and the email looks valid, then creates and returns the new student.
2. **React form** — controlled inputs (`useState` + `onChange`), submits with
   `onSubmit` and `event.preventDefault()`.
3. **fetch() connection** — sends the form data as JSON with
   `Content-Type: application/json` to `/api/students`.
4. **Loading state** — `loading` flag disables the submit button and shows a
   spinner while waiting for the Flask response.
5. **Post-success UI update** — shows a success message, clears the form, and
   appends the new student to the on-screen list with no page refresh.

Tested with `curl` against all four cases: valid submission, empty fields,
invalid email, and the resulting GET list — see backend/app.py docstring.
