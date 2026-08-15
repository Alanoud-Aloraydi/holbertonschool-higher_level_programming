"""Serve static pages rendered from reusable Jinja templates."""

from pathlib import Path

from flask import Flask, render_template


BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=BASE_DIR / "templates")


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Render the contact page."""
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
