# 🍋 Little Lemon Restaurant Web Application

A Django-based restaurant management web application developed as part of the Meta Back-End Developer Professional Certificate Capstone Project.

## 📌 Project Overview

Little Lemon is a restaurant web application that allows users to:

- Browse the restaurant menu
- View restaurant information
- Create and manage table reservations
- Access REST API endpoints built with Django REST Framework
- Authenticate users using Token Authentication

---

## 🚀 Features

- Django Framework
- Django REST Framework (DRF)
- Function-Based Views
- Class-Based API Views
- Menu API
- Reservation API
- Token Authentication
- Admin Dashboard
- SQLite Database
- Static Files Support
- Unit Testing

---

## 🛠️ Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite
- HTML
- CSS
- Git
- GitHub

---

## 📂 Project Structure

```
LittleLemon/
│
├── littlelemon/          # Django project
├── restaurant/           # Restaurant application
├── tests/                # Unit tests
├── manage.py
├── db.sqlite3
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/ravizare/LittleLemon.git
```

Navigate into the project

```bash
cd LittleLemon
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start the development server

```bash
python manage.py runserver
```

Open your browser

```
http://127.0.0.1:8000/
```

---

## 🔗 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/menu-items/` | List all menu items |
| `/menu-items/<id>` | Retrieve a single menu item |
| `/reservations/` | Reservation API |
| `/bookings` | Booking endpoint |
| `/api-token-auth/` | Obtain authentication token |

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 👨‍💻 Author

**Ravi Zare**

GitHub: https://github.com/ravizare

---

## 📄 License

This project was developed for educational purposes as part of the Meta Back-End Developer Professional Certificate.
