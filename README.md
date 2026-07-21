# 📚 Library Management System

A web-based **Library Management System** developed using **Django**. The system allows administrators to manage books and students to browse and issue books through a simple, user-friendly interface.

## 🚀 Features

### 👨‍💼 Admin

* Admin Login
* Add, Edit, and Delete Books
* Manage Book Categories
* View Issued Books
* Manage Student Accounts

### 👨‍🎓 Student

* Register and Login
* View Available Books
* Issue Books
* View Issued Books
* Profile Management

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
library_management/
│── accounts/
│── books/
│── templates/
│── static/
│── library_management/
│── manage.py
│── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/SubhashiniPD/library_management.git
cd library_management
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

### 6. Run the server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

## 📸 Screenshots

You can add screenshots here.

* Home Page
* Student Dashboard
* Admin Dashboard
* Book List
* Issue Book Page

---

## 📋 Future Improvements

* Book Return System
* Fine Calculation
* Email Notifications
* Search and Filter Books
* QR Code Based Book Issue
* REST API Support

---

## 👩‍💻 Author

**Subhashini P D**

* GitHub: https://github.com/SubhashiniPD
* LinkedIn: https://www.linkedin.com/in/subhashini-p-d-092299334/

---

## 📄 License

This project is created for educational and learning purposes.
