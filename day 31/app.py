"""
Day 31 — Backend Technology
Portfolio website served with Flask.

Concepts covered here:
  - Creating a simple portfolio website with home / about / contact pages
  - Rendering HTML files (render_template)
  - Rendering CSS files (static folder)

Run:
    python app.py
Then open: http://127.0.0.1:5000/
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", active_page="home")


@app.route("/about")
def about():
    return render_template("about.html", active_page="about")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_sent = False

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # In a real app this would save to a DB or send an email.
        # For this exercise we just confirm it was received.
        if name and email and message:
            message_sent = True

    return render_template(
        "contact.html", active_page="contact", message_sent=message_sent
    )


if __name__ == "__main__":
    app.run(debug=True)
