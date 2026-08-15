"""Render a list of items loaded from a JSON file."""

import json
from pathlib import Path

from flask import Flask, render_template


BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=BASE_DIR / "templates")


@app.route("/items")
def items():
    """Render the items page with data from items.json."""
    with open(BASE_DIR / "items.json", encoding="utf-8") as file:
        data = json.load(file)

    return render_template("items.html", items=data.get("items", []))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
