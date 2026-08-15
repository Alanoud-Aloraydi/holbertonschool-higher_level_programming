# Python Server-Side Rendering

This project explores server-side rendering with Python, Flask, and Jinja. It
starts with text-template substitution and progresses through reusable HTML
templates and dynamic product data loaded from JSON, CSV, and SQLite.

## Learning objectives

- Explain server-side rendering and its differences from client-side rendering.
- Render reusable HTML templates with Flask and Jinja.
- Use Jinja loops and conditions for dynamic content.
- Read structured data from JSON and CSV files.
- Query product data from a SQLite database.
- Validate query parameters and present useful error messages.

## Files

| Path | Description |
| --- | --- |
| `task_00_intro.py` | Generates personalized invitation files. |
| `template.txt` | Invitation template used by Task 0. |
| `task_01_jinja.py` | Serves home, about, and contact pages. |
| `task_02_logic.py` | Renders items loaded from JSON. |
| `task_03_files.py` | Displays and filters JSON or CSV products. |
| `task_04_db.py` | Adds SQLite as a product data source. |
| `items.json` | Item data used by Task 2. |
| `products.json` | JSON product data used by Tasks 3 and 4. |
| `products.csv` | CSV product data used by Tasks 3 and 4. |
| `products.db` | SQLite product database used by Task 4. |
| `templates/` | Reusable and dynamic Jinja templates. |

## Endpoints

| Application | Endpoint | Purpose |
| --- | --- | --- |
| `task_01_jinja.py` | `/`, `/about`, `/contact` | Render static pages with shared templates. |
| `task_02_logic.py` | `/items` | Display items or an empty-list message. |
| `task_03_files.py` | `/products?source=json|csv[&id=N]` | Display or filter file-based products. |
| `task_04_db.py` | `/products?source=json|csv|sql[&id=N]` | Display or filter products from three sources. |

## Running an application

Install Flask, then run the required task from this directory. For example:

```sh
python3 task_04_db.py
```

The Flask development server listens on port `5000`.
