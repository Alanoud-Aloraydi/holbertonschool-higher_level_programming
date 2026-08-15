"""Display products loaded from JSON, CSV, or SQLite."""

import csv
import json
from pathlib import Path
import sqlite3

from flask import Flask, render_template, request


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "products.db"
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


SEED_PRODUCTS = (
    (1, "Laptop", "Electronics", 799.99),
    (2, "Coffee Mug", "Home Goods", 15.99),
)


def init_db(file_path):
    """Create the Products table and seed it if needed.

    Safe to call on every run: the table is only created if it does
    not already exist, and the seed rows are inserted with their
    primary key so re-running never produces duplicate records.
    """
    connection = sqlite3.connect(file_path)
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
            """
        )
        connection.executemany(
            "INSERT OR IGNORE INTO Products (id, name, category, price) "
            "VALUES (?, ?, ?, ?)",
            SEED_PRODUCTS,
        )
        connection.commit()
    finally:
        connection.close()


def read_sql(file_path):
    """Return products stored in a SQLite database."""
    connection = sqlite3.connect(file_path)
    try:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            "SELECT id, name, category, price FROM Products"
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        connection.close()


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
        elif source == "sql":
            product_list = read_sql(DB_PATH)
        else:
            return render_template(
                "product_display.html", products=[], error="Wrong source"
            )
    except sqlite3.Error:
        return render_template(
            "product_display.html",
            products=[],
            error="Database error",
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


try:
    init_db(DB_PATH)
except sqlite3.Error as error:
    print(f"Error initializing {DB_PATH}: {error}")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
