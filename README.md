# 🛡️ Flask Login System with Database & Dashboard

A **beginner-friendly login & signup system** built with **Flask**, now enhanced with **database integration**, **hashed passwords**, and an **admin dashboard** to manage users.

> ⚡ **Update:** Previously, this project used a simple **text file** for storing user data. Now, I have implemented **SQLAlchemy with SQLite database**, added password hashing with **bcrypt**, and built a **dashboard** to manage all users.

---

## 🔑 Features

* ✅ User Sign Up with **username & password**
* ✅ User Login with credentials
* ✅ Passwords securely hashed using **bcrypt**
* ✅ **Dashboard** to view all registered users:

  * Shows **username** and **hashed password**
  * Admin can **delete users**
* ✅ Proper **form validation** & **error handling**
* ✅ Clean, beginner-friendly **code structure**

---

## 🛠️ Tech Stack

| Technology     | Purpose               |
| -------------- | --------------------- |
| Python (Flask) | Backend framework     |
| SQLAlchemy     | Database ORM (SQLite) |
| bcrypt         | Password hashing      |
| HTML / CSS     | Frontend templates    |
| Jinja2         | Template rendering    |

---

## 📂 Project Structure

```
flask-login-system-db/
│── app.py               # Main Flask app
│── templates/
│   ├── login.html       # Login form
│   ├── signup.html      # Signup form
│   ├── home.html        # User dashboard after login
│   └── dashboard.html   # Admin view of all users
│── static/
│   └── style.css        # Optional CSS styling
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

---

## 🚀 Getting Started

1. **Clone this repository**

```bash
git clone https://github.com/your-username/flask-login-system-db.git
cd flask-login-system-db
```

2. **Create Virtual Environment (recommended)**

```bash
python -m venv venv
```

Activate venv:

* **Windows (PowerShell)**

```powershell
venv\Scripts\activate
```

* **Linux/Mac**

```bash
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Flask app**

```bash
python app.py
```

5. **Open in Browser**

```
http://127.0.0.1:5000/
```

---

## 🧩 Skills Used

* Flask Basics → Routing, request handling, rendering templates
* SQLAlchemy → Database models, queries, CRUD operations
* Password Hashing → Secure storage with **bcrypt**
* HTML Forms → Signup & Login with POST/GET methods
* Session Management → Keeping users logged in
* Dashboard → Admin view for managing all users
* Error Handling → Username exists / Incorrect password
* Frontend Basics → HTML + CSS integration with Flask

---

## 📘 What I Learned

* How to **migrate from text file storage to a database**
* Implementing **hashed passwords** securely
* Building a **dynamic admin dashboard** to manage users
* Performing **CRUD operations** in Flask with SQLAlchemy
* Proper **session management** for user authentication
* Organizing Flask projects professionally
* Handling **form validation** and showing errors dynamically

---

## 💡 Notes

* This project is **beginner-friendly**, ideal for understanding **Flask authentication and database integration**.
* It demonstrates a **step-by-step evolution** from a **file-based login system** to a **fully functional database-backed application**.

---

⚡ **Beginner Friendly | Flask Authentication | SQLAlchemy Database | Bcrypt Passwords | Admin Dashboard**