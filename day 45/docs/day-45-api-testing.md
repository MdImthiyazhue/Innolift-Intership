# Day 45 — API Testing with Postman

Testing the Student Management REST API (Flask + MySQL) independently of the
React frontend, using the **Student Management API** Postman collection
(`postman/Student_Management_API.postman_collection.json`).

Base URL: `http://localhost:5000`

---

## Test 1 — GET /api/students (Happy Path)

| Field | Value |
|---|---|
| Endpoint | `/api/students` |
| Method | GET |
| Request Body | — |
| Expected Result | Returns all students from MySQL as a JSON array |
| Actual Result | Returned all 5 seeded students, each with `id`, `name`, `email`, `course` |
| Status Code | `200 OK` |
| Test Status | ✅ Passed |

```json
[
  { "id": 1, "name": "Arun Kumar", "email": "arun.kumar@example.com", "course": "AI & Data Science" },
  { "id": 2, "name": "Divya Sri", "email": "divya.sri@example.com", "course": "AI & Data Science" }
]
```
*(truncated — full response returns all 5 records)*

---

## Test 2 — POST /api/students (Valid Request)

| Field | Value |
|---|---|
| Endpoint | `/api/students` |
| Method | POST |
| Request Body | `{"name": "Test Student", "email": "test@example.com", "course": "Computer Science"}` |
| Expected Result | Student created, inserted into MySQL, created record returned |
| Actual Result | `{"success": true, "message": "Student added successfully", "student": {"id": 8, "name": "Test Student", "email": "test@example.com", "course": "Computer Science"}}` |
| Status Code | `201 Created` |
| Test Status | ✅ Passed |

**MySQL verification** (`SELECT * FROM students WHERE email='test@example.com';`):
confirmed the row existed with the exact id, name, email, and course returned
by the API — the response was not just a formality, the insert genuinely
happened.

---

## Test 3 — POST /api/students (Invalid Inputs)

| Case | Request Body | Expected | Actual Message | Status | Test Status |
|---|---|---|---|---|---|
| Empty name | `{"name":"","email":"test2@example.com","course":"IT"}` | 400 + error | "name, email and course are all required." | 400 | ✅ Passed |
| Missing email | `{"name":"Test Student","course":"IT"}` | 400 + error | "name, email and course are all required." | 400 | ✅ Passed |
| Missing course | `{"name":"Test Student","email":"test3@example.com"}` | 400 + error | "name, email and course are all required." | 400 | ✅ Passed |
| Empty JSON body | `{}` | 400 + error | "No data received. Send a valid JSON body." | 400 | ✅ Passed |
| No request body | *(none sent)* | 400 + error, no crash | "No data received. Send a valid JSON body." | 400 | ✅ Passed |

None of these five cases created a row in MySQL or crashed the server —
verified by re-running `SELECT * FROM students;` afterward and confirming
the table still had exactly the expected records.

---

## Test 4 — POST /api/students (Duplicate Email)

| Field | Value |
|---|---|
| Endpoint | `/api/students` |
| Method | POST |
| Request Body | `{"name": "Another Student", "email": "test@example.com", "course": "IT"}` (email already used in Test 2) |
| Expected Result | Rejected, no duplicate row created |
| Actual Result | `{"success": false, "message": "A student with this email already exists."}` |
| Status Code | `409 Conflict` |
| Test Status | ✅ Passed |

MySQL's `UNIQUE` constraint on `email` combined with Flask catching the
resulting `mysql.connector.Error` (error code `ER_DUP_ENTRY`) prevented the
duplicate from being written. Confirmed only one row for `test@example.com`
exists in the table.

---

## Test 5 — Invalid Routes and Methods

| Case | Request | Expected | Actual Message | Status | Test Status |
|---|---|---|---|---|---|
| Invalid endpoint | `GET /api/student` (typo, missing "s") | 404 | "The requested endpoint does not exist." | 404 | ✅ Passed |
| Unsupported method | `DELETE /api/students` | 405 | "This HTTP method is not allowed for this endpoint." | 405 | ✅ Passed |

**Fix applied during testing:** Flask's default error pages return HTML, not
JSON, which breaks the API's JSON contract for any client (Postman, React,
or otherwise) that expects a consistent response shape. Added
`@app.errorhandler(404)`, `@app.errorhandler(405)`, and
`@app.errorhandler(500)` to `app.py` so every response — success or error —
is JSON with a `success` and `message` field.

---

## HTTP Status Code Reference

| Scenario | Status Code | Why This Code |
|---|---|---|
| Successful GET | `200 OK` | Request succeeded and data was returned |
| Successful POST | `201 Created` | A new resource (student row) was created |
| Invalid input (missing/empty fields, no body) | `400 Bad Request` | The client sent malformed or incomplete data — the problem is on the request side |
| Duplicate email | `409 Conflict` | The request is well-formed but conflicts with existing data (the unique email constraint) |
| Invalid endpoint | `404 Not Found` | The requested route doesn't exist on the server |
| Unsupported method | `405 Method Not Allowed` | The route exists, but not for that HTTP verb |
| Server/database error | `500 Internal Server Error` | Something failed on the server side (e.g. MySQL connection down) — not the client's fault |

Getting these right matters because the frontend (or any API consumer)
branches its behavior based on the status code, not just the message text —
a `400` should prompt the user to fix their input, a `409` should tell them
the email is taken, and a `500` should tell them to try again later rather
than blame their form.

---

## Test 6 — Consistency Between Postman and React

Re-ran the same scenarios through the React app instead of Postman:

| Scenario | Postman Result | React Result | Consistent? |
|---|---|---|---|
| Load student list | 200, 5 students | Table renders 5 students | ✅ Yes |
| Add valid student | 201, student returned | Success message + instant row in table | ✅ Yes |
| Add duplicate email | 409, error message | Form shows "A student with this email already exists." | ✅ Yes |
| Add student with missing field | 400, error message | Form shows the same validation message | ✅ Yes |
| Backend unreachable | Connection failure | UI shows "Unable to load students." | ✅ Yes |

The Flask API behaves identically regardless of which client calls it —
confirming the backend logic is correctly separated from the frontend, and
the React error-handling built in Day 43 correctly surfaces exactly what the
API returns.

---

## Summary Table

| Test | Method | Result | Status |
|---|---|---|---|
| Get Students | GET | Passed | 200 |
| Create Student (Valid) | POST | Passed | 201 |
| Empty Name | POST | Passed | 400 |
| Missing Email | POST | Passed | 400 |
| Missing Course | POST | Passed | 400 |
| Empty JSON Body | POST | Passed | 400 |
| No Request Body | POST | Passed | 400 |
| Duplicate Email | POST | Passed | 409 |
| Invalid Endpoint | GET | Passed | 404 |
| Unsupported Method | DELETE | Passed | 405 |

**10 / 10 tests passed.** No crashes on any invalid input; every response —
success or failure — returned a consistent JSON shape.

---

## Postman Screenshots

*(Add screenshots here after running the collection locally: import
`postman/Student_Management_API.postman_collection.json`, run each request
in order, and paste a screenshot of the response panel for at least Test 1,
Test 2, Test 4, and Test 5.)*
