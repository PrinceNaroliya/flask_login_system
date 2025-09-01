from flask import Flask, request, session, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)

app.secret_key = 'super_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    if 'name' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', name = session['name'])

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error_message = None
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(name = name).first()
        if user:
            error_message = '*Username is already exists*'
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            new_user = User(
                name=name,
                password=hashed_password.decode('utf-8')
            )

            db.session.add(new_user)
            db.session.commit()

            session['name'] = name
            return redirect(url_for('home')) 

    return render_template('signup.html',error_message = error_message)

@app.route('/dashboard')
def dashboard():
    all_users = User.query.all()
    return render_template('dashboard.html', all_users = all_users)

@app.route('/delete/<sno>', methods = ['GET','POST'])
def delete(sno):
    user = User.query.filter_by(sno = sno).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/login', methods = ['GET','POST'])
def login():
    error_message = None
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(name = name).first()
        
        if user:  
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):  
                session['name'] = user.name
                return redirect(url_for('home'))
            else:
                error_message = '*Password is Incorrect*'
        else:
            error_message = '*Username does not exist. Signup first*'
    return render_template('login.html', error_message = error_message)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)