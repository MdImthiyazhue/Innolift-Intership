# Day 43 — API Response & Frontend-Backend Practice

Builds on the Day 41–42 Flask + React student project. Same project,
now with error handling, an empty-state UI, and a full GET → POST flow.

## Run the backend
```
cd backend
pip install -r requirements.txt
python app.py
```
Runs on http://localhost:5000

## Run the frontend
```
cd frontend
npm install
npm run dev
```
Runs on http://localhost:5173

## How to test each task

**Task 01 — Error handling**
Stop the Flask server, then reload the React app.
The fetch fails, `response.ok`/try-catch catches it, loading stops,
and the UI shows: `Unable to load students.`

**Task 02 — Empty state**
In `backend/app.py`, temporarily change the GET route to
`return jsonify([]), 200` and restart Flask.
The React table is hidden and the UI shows: `No students found.`

**Task 03 — Full flow**
1. Start Flask, then start React → GET /api/students runs on load → students display.
2. Fill the Add Student form and click Submit.
3. React POSTs JSON to /api/students.
4. Flask validates required fields and returns a JSON response.
5. On success, React shows the success message and appends the new
   student to the list immediately — no page refresh.
6. To test a failure case, submit the form with a field left blank,
   or stop Flask before submitting — the form shows an error message
   instead of crashing.

## What happens when you click Submit (walkthrough)
1. `handleSubmit` prevents the default page reload and validates the
   form fields client-side.
2. `fetch()` sends a POST request with the form data as JSON to Flask.
3. Flask receives the request, parses the JSON body, and validates
   that `name`, `roll_no`, and `department` are all present.
4. If validation fails, Flask returns a 400 status with an error
   message; React's `!response.ok` check throws, and the catch block
   shows that message in the form.
5. If validation passes, Flask appends the student and returns a 201
   status with the new student object.
6. React reads the JSON response, adds the new student to local state
   with `setStudents`, and React re-renders the table — the new row
   appears instantly, with no page refresh.
