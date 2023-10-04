from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__,static_folder='styles')
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Replace with a database for storing user credentials
users = {'username': 'password'}  # Insecure, for demonstration purposes only

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'username' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True, port=8001)
    
