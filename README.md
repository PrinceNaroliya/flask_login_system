# flask_login_system

🔐 Flask Login System

A simple Login & Signup system built with Flask
.
This project is perfect for beginners who want to understand user authentication in Flask.

📌 Features

* ✅ User Sign Up with username & password

* ✅ User Login with credentials

* ✅ Shows error if:

* Username already exists during signup

* Incorrect username or password during login

* ✅ Proper form validation

* ✅ Clean beginner-friendly code structure

🛠️ Tech Stack

* Python (Flask framework)

* HTML / CSS (basic templates for forms)

* SQLite (or dictionary for temp storage) – for user data storage

📂 Project Structure
flask-login-system/
│── app.py              # Main Flask app
│── templates/
│   ├── login.html      # Login form
│   ├── signup.html     # Signup form
│   └── home.html       # Home/dashboard after login
│── static/
│   └── style.css       # (Optional) CSS styling
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

🚀 Getting Started

Follow these steps to run the project locally:

1. Clone this repository
git clone https://github.com/your-username/flask-login-system.git
cd flask-login-system

2. Create Virtual Environment (recommended)
python -m venv venv


Activate venv:

Windows (PowerShell)

venv\Scripts\activate


Linux/Mac

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt


(Make sure Flask is installed. If not, manually install using)

pip install flask

4. Run the Flask app
python app.py

5. Open in Browser
http://127.0.0.1:5000/

🧩 Skills Used

* Flask Basics → Routes, request handling, rendering templates

* HTML Forms → Creating signup & login forms with POST/GET methods

* File Handling in Python → Writing & reading user data in users.txt

* Error Handling → Checking if username exists / wrong password

* Basic Authentication Logic → Simple login-signup workflow

* Frontend Basics → HTML + CSS integration with Flask

📘 What I Learned

* While building this project, I learned:

* How to create a Flask project from scratch

* How to handle GET & POST requests in Flask

* How to use Jinja2 templates for rendering HTML pages

* NBasics of file handling in Python (open, read, write, append)

* How to display error messages on forms

* Importance of organizing a Flask project structure

* First step towards building real authentication systems

⚡ Beginner Friendly | Flask Authentication | File Storage