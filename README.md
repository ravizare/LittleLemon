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


SCREENSHOTS of project work :-

1. HomePage
<img width="640" height="480" alt="127 0 0 1_8000_api_" src="https://github.com/user-attachments/assets/f37e2405-bef9-40cf-b4ed-34ab844baf77" />



2. API Auth page
<img width="640" height="480" alt="http127 0 0 18000Iapi-auth" src="https://github.com/user-attachments/assets/83e88b90-4e0c-4721-8c18-3162e4d88c32" />



3. Admin page
<img width="640" height="480" alt="2026-06-18 (7)" src="https://github.com/user-attachments/assets/9ceb8e3f-abb7-467b-8903-389926ec3dab" />



4. Table Bookings Screenshot
<img width="640" height="480" alt="2026-06-18 (11)" src="https://github.com/user-attachments/assets/08807c4f-5274-465f-b5e3-e6b509cf189a" />



5. LittleLemon Restaurant Menu items
<img width="640" height="480" alt="2026-06-18 (12)" src="https://github.com/user-attachments/assets/692b7e9b-effd-4859-a1df-70e34b965946" />



6. Token Creation
<img width="640" height="480" alt="2026-06-22 (8)" src="https://github.com/user-attachments/assets/c229495c-479e-443d-a866-f9aa0667b93d" />



7. Token Destroy screenshot
<img width="640" height="480" alt="2026-06-22 (10)" src="https://github.com/user-attachments/assets/93a9e791-7931-4a50-8199-31da112914b4" />




Insomnia testing applications Screenshots :-

1. api-token-auth with 200ok successful screenshot
<img width="640" height="480" alt="2026-06-22 (3)" src="https://github.com/user-attachments/assets/179d80bc-229e-4a4d-8747-8b47a87b4d91" />




2. Header setting with created Token in Insomnia app
<img width="640" height="480" alt="2026-06-22 (7)" src="https://github.com/user-attachments/assets/2f5751ab-160d-4ab4-a992-6c8916403c79" />




















## 👨‍💻 Author

**Ravi Zare**

GitHub: https://github.com/ravizare

---

## 📄 License

This project was developed for educational purposes as part of the Meta Back-End Developer Professional Certificate.



