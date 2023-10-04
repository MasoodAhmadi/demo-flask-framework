from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Replace with a database for storing user credentials
users = {'username': 'password'}  # Insecure, for demonstration purposes only

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login
        flash('Login successful', 'success')
        return redirect(url_for('dashboard'))
    else:
        # Failed login
        flash('Login failed. Please check your credentials.', 'error')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
