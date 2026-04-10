# Simple Blog — Experiment 5

A Flask-based CRUD blog platform built for **Experiment-5**.

## Features
- Create, Read, Update, Delete blog posts
- In-memory post storage (no database required)
- Responsive dark-themed UI with Google Fonts
- Sticky navigation bar with Home and New Post links

## Setup & Run

```bash
# 1. Navigate to project folder
cd simple_blog

# 2. (Optional) Create & activate virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# 3. Install Flask
pip install flask

# 4. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Project Structure

```
simple_blog/
├── app.py                  # Main Flask application (routes & logic)
├── templates/
│   ├── base.html           # Base layout with nav, footer, CSS
│   ├── index.html          # Home page — lists all posts
│   ├── create.html         # Form to create a new post
│   └── edit.html           # Form to edit an existing post
├── static/
│   └── style.css           # Optional extra CSS
└── README.md
```

## References
- Flask Documentation: https://flask.palletsprojects.com/
- Jinja2 Templating: https://jinja.palletsprojects.com/
- Google Fonts: https://fonts.google.com/
