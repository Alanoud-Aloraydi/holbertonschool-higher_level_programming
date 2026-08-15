# Python Server-Side Rendering

## About

Introduces server-side rendering with Flask and Jinja. It starts with plain
text-template substitution, moves to HTML pages built from reusable
templates, and ends by rendering product data pulled from JSON, CSV, and
SQLite sources.

## Technologies

- Python 3
- Flask, Jinja2
- `json`, `csv`, `sqlite3` (standard library)

## Files & Tasks

| File | Task |
| --- | --- |
| `task_00_intro.py` | Generate invitation files from `template.txt`. |
| `task_01_jinja.py` | Serve `/`, `/about`, `/contact` with a shared header/footer. |
| `task_02_logic.py` | Serve `/items`, rendering items from `items.json`. |
| `task_03_files.py` | Serve `/products`, reading from JSON or CSV. |
| `task_04_db.py` | Extend `/products` to also read from SQLite (`products.db`). |

Supporting data and templates: `template.txt`, `items.json`,
`products.json`, `products.csv`, `products.db`, and the `templates/`
folder.

## How to Run / Test

```sh
pip install flask
python task_04_db.py
```

Then visit `http://localhost:5000/products?source=sql` (or `source=json`
/ `source=csv`, optionally with `&id=<n>`). Each task file can also be run
on its own the same way, e.g. `python task_01_jinja.py`.

## Requirements

- Python 3.9+
- Flask
