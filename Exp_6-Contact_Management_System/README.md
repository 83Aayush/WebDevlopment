# 📒 Contact Management System — Django

**Experiment 6 | Python Web Development**

A beginner-friendly Contact Management System built with **Django** (Python web framework).  
Supports full **CRUD** operations: Create, Read, Update, Delete — plus search functionality.

---

## 🗂️ Project Structure

```
contact_management_system/
│
├── manage.py                         # Django management script
│
├── contact_management_system/        # Project-level settings
│   ├── __init__.py
│   ├── settings.py                   # All Django settings
│   ├── urls.py                       # Root URL configuration
│   └── wsgi.py
│
├── contacts/                         # Our contacts app
│   ├── __init__.py
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Contact database model
│   ├── views.py                      # All view functions (CRUD logic)
│   ├── forms.py                      # ContactForm with validation
│   ├── urls.py                       # URL patterns for contacts
│   ├── admin.py                      # Django admin registration
│   │
│   ├── migrations/                   # Database migration files
│   │   └── __init__.py
│   │
│   ├── templates/contacts/           # HTML templates
│   │   ├── base.html                 # Master layout template
│   │   ├── index.html                # Home — list all contacts
│   │   ├── add_contact.html          # Add new contact form
│   │   ├── edit_contact.html         # Edit contact form
│   │   ├── delete_confirm.html       # Delete confirmation page
│   │   └── contact_detail.html      # Single contact detail view
│   │
│   └── static/contacts/css/
│       └── style.css                 # Custom CSS styles
│
├── db.sqlite3                        # SQLite database (auto-created)
└── README.md                         # This file
```

---

## ⚙️ Setup & Run Instructions

### Step 1 — Create and activate a virtual environment (recommended)
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

### Step 2 — Install Django
```bash
pip install django
```

### Step 3 — Apply database migrations
```bash
cd contact_management_system
python manage.py makemigrations
python manage.py migrate
```

### Step 4 — (Optional) Create admin user
```bash
python manage.py createsuperuser
```

### Step 5 — Run the development server
```bash
python manage.py runserver
```

### Step 6 — Open in browser
```
http://127.0.0.1:8000/
```

Admin panel (if created superuser):
```
http://127.0.0.1:8000/admin/
```

---

## 🔧 Features Implemented

| Task | Feature | Status |
|------|---------|--------|
| Task 1 | Project setup & structure | ✅ Done |
| Task 2 | Flask → Django app initialization | ✅ Done |
| Task 3 | Add new contacts (Create) | ✅ Done |
| Task 4 | View all contacts (Read) | ✅ Done |
| Task 5 | Edit contacts (Update) | ✅ Done |
| Task 6 | Delete contacts (Delete) | ✅ Done |
| Task 7 | Search + CSS Styling (Bonus) | ✅ Done |

---

## 🌐 URL Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | `index` | Home — list all contacts |
| `/add/` | `add_contact` | Add new contact |
| `/edit/<id>/` | `edit_contact` | Edit existing contact |
| `/delete/<id>/` | `delete_contact` | Delete confirmation + delete |
| `/contact/<id>/` | `contact_detail` | View single contact details |
| `/admin/` | Django Admin | Admin panel |

---

## 📚 External References

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [Google Fonts — Poppins & Nunito](https://fonts.google.com/)

---

## 🛡️ Academic Integrity

This project was written independently as part of Experiment 6.  
All code is original. External libraries are cited above.
