from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt

app = Flask(__name__)
app.secret_key = "any_random_secret_key" 

@app.route('/', methods=['GET', 'POST'])
def signup():
    error_message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        try:
            with open('data.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    u, h = line.strip().split('|')
                    if username == u:
                        error_message = '*Username already exists*'
                        return render_template('signup.html', error_message=error_message)
        except FileNotFoundError:
            pass

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with open('data.txt', 'a') as f:
            f.write(f"{username}|{hashed_password.decode()}\n")

        session['username'] = username
        return redirect(url_for('welcome'))

    return render_template('signup.html', error_message=error_message)


@app.route('/login', methods=['GET', 'POST'])
def login():

    error_message = None

    if request.method == 'POST':
        user_name = request.form.get('username')
        pass_word = request.form.get('password')

        login_success = False
        try:
            with open('data.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    u, h = line.strip().split('|')
                    if u == user_name:
                        if bcrypt.checkpw(pass_word.encode('utf-8'), h.encode()):
                            login_success = True
                            session['username'] = u
                            break
                        else:
                            error_message = '*password is incorrect*'
                    else:
                        error_message = '*username is incorrect*'

                    if user_name not in line:
                        error_message = '*username not found signup first*'

            if login_success:
                return redirect(url_for('welcome'))

        except FileNotFoundError:
            error_message =  "*No users found. Please sign up first.*"

    return render_template('login.html', error_message = error_message)

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
