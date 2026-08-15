"""Display products loaded from JSON or CSV data sources."""

import csv
import json
from pathlib import Path

from flask import Flask, render_template, request


BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=BASE_DIR / "templates")


def read_json(file_path):
    """Return the products stored in a JSON file."""
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)


def read_csv(file_path):
    """Return normalized products stored in a CSV file."""
    with open(file_path, newline="", encoding="utf-8") as file:
        products = []

        for row in csv.DictReader(file):
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"]),
            })

    return products


def filter_products(products, product_id):
    """Return products matching an optional numeric identifier."""
    if product_id is None:
        return products

    try:
        identifier = int(product_id)
    except (TypeError, ValueError):
        return []

    return [product for product in products if product["id"] == identifier]


@app.route("/products")
def products():
    """Render products selected by source and optional ID parameters."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        if source == "json":
            product_list = read_json(BASE_DIR / "products.json")
        elif source == "csv":
            product_list = read_csv(BASE_DIR / "products.csv")
        else:
            return render_template(
                "product_display.html", products=[], error="Wrong source"
            )
    except (OSError, csv.Error, json.JSONDecodeError, ValueError):
        return render_template(
            "product_display.html",
            products=[],
            error="Error reading data",
        )

    product_list = filter_products(product_list, product_id)

    if product_id is not None and not product_list:
        return render_template(
            "product_display.html",
            products=[],
            error="Product not found",
        )

    return render_template(
        "product_display.html", products=product_list, error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
