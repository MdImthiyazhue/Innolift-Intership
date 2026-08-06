# Day 35 – Basics of SQL: Portfolio Database + Backend Connection

This delivers the Day 35 task: a MySQL database for the student portfolio
website, with tables, seed data, and an Express backend connected to it.

## Folder structure

```
day35-sql/
├── sql/
│   ├── schema.sql       # CREATE DATABASE + CREATE TABLE statements
│   └── seed_data.sql    # INSERT statements (real portfolio content)
├── backend/
│   ├── config/db.js               # MySQL connection pool
│   ├── routes/portfolioRoutes.js  # REST API endpoints
│   ├── server.js                  # Express app entry point
│   ├── package.json
│   └── .env.example
└── README.md
```

## 1. Install MySQL Server

**Windows:** Download the MySQL Installer from
https://dev.mysql.com/downloads/installer/, run it, choose
"Server only" (or "Developer Default"), and set a root password
during setup.

**macOS:** `brew install mysql` then `brew services start mysql`

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo mysql_secure_installation
```

Verify it's running:
```bash
mysql -u root -p
```

## 2. Create the database and tables

From a terminal, in this folder:

```bash
mysql -u root -p < sql/schema.sql
mysql -u root -p < sql/seed_data.sql
```

Or, inside the MySQL shell:
```sql
SOURCE sql/schema.sql;
SOURCE sql/seed_data.sql;
```

This creates the `portfolio_db` database with 6 tables:
`profile`, `education`, `skills`, `projects`, `certifications`, `messages`.

Check it worked:
```sql
USE portfolio_db;
SHOW TABLES;
SELECT * FROM projects;
```

## 3. Connect the backend

```bash
cd backend
npm install
cp .env.example .env
```

Open `.env` and set your real MySQL password:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_actual_password
DB_NAME=portfolio_db
PORT=5000
```

Start the server:
```bash
npm start
```

You should see:
```
🚀 Server running at http://localhost:5000
✅ Connected to MySQL database: portfolio_db
```

## 4. Test the API

| Method | Endpoint             | Description                          |
|--------|-----------------------|---------------------------------------|
| GET    | `/api/profile`        | Get profile/about info                |
| GET    | `/api/education`      | Get education records                 |
| GET    | `/api/skills`         | Get all skills                        |
| GET    | `/api/projects`       | Get all projects                      |
| POST   | `/api/projects`       | Add a new project                     |
| GET    | `/api/certifications` | Get all certifications                |
| POST   | `/api/messages`       | Submit a contact form message         |
| GET    | `/api/messages`       | View submitted contact messages       |

Quick test:
```bash
curl http://localhost:5000/api/projects
```

## 5. Connecting this to the portfolio frontend

In `index.html` (Day 21/22 portfolio), the static content can gradually be
replaced with a `fetch()` call to this API, e.g.:

```javascript
fetch('http://localhost:5000/api/projects')
  .then(res => res.json())
  .then(projects => {
    // render project cards dynamically from the database
  });
```

And the contact form can POST to `/api/messages` instead of just
sitting there — this is exactly what "connect with your backend server"
in the task means: the portfolio's data now lives in MySQL instead of
being hardcoded in the HTML.
