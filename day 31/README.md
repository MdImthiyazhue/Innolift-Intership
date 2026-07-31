# Day 31 — Backend Technology (Flask)

## What's here
- **`hello_flask.py`** — the very first Flask server: one route, one plain-text response. Run this first to see Flask working at its simplest.
- **`app.py`** — the actual portfolio site: Home / About / Contact pages, rendered from HTML templates with a linked CSS file and a working contact form.
- **`templates/`** — `base.html` (shared layout/nav) + `home.html`, `about.html`, `contact.html`.
- **`static/style.css`** — styling, served and rendered via Flask's static file handling.

## Concepts covered
- Starting a Flask server
- Passing text as a response (`hello_flask.py`)
- Rendering HTML files with `render_template`
- Rendering a CSS file via `url_for('static', ...)`
- A simple multi-page site (home / about / contact) with routing
- A working POST form on the contact page

## How to run

```bash
pip install -r requirements.txt

# Step 1 — the warm-up server
python hello_flask.py
# visit http://127.0.0.1:5000/

# Step 2 — the full portfolio site (stop the warm-up server first, same port)
python app.py
# visit http://127.0.0.1:5000/
```

Then browse to `/`, `/about`, and `/contact` to see all three pages.
