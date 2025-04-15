# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 15:48:20 2025

@author: third
"""

from flask import Flask, render_template_string, request
import bcrypt

app = Flask(__name__)

# HTML template as a string
login_form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login Form</h2>
    <form method="POST" action="/login">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" required><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        return f"""
        <h2>Form Submitted Successfully!</h2>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Hashed Password:</strong> {hashed_password.decode('utf-8')}</p>
        """
    
    return render_template_string(login_form_html)

if __name__ == '__main__':
    app.run(debug=True)
