"""
Chris Tison
CIS256 Spring 2025
Flask App
"""

from flask import Flask, render_template_string, request
import re # used to validate the user name and pw 
import bcrypt # Used to encrypt the pw after submit is hit.

app = Flask(__name__)

# Wrote my HTML template for login form and saved to a variable
login_form_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login Form</h2>
    <form method="POST" action="/login">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""
# Define a route /login to display a login form using HTML.
# The form requires atleast "username field", "password field" and "login button"
@app.route('/login', methods=['GET'])
def login_form():
    return render_template_string(login_form_html)


# Define a POST route /login to process the form submission. 
# Capture and display the username and password submitted via the form.
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Validation rules for username:
    # Using re.match, that checks patterns.  In this case patterns
    # restricts user name to A thru Z upper and lower case numbers 0 thru 9
    # and allows for underscore "_".
    if not re.match("^[A-Za-z0-9_]+$", username):
        return "Invalid username. Only letters, numbers, and underscores are allowed."
    
    # Validation for PW:
    # Checks that pw is at least 8 chars.  Contains only letters upper or lower
    # and lastly requires at least one digit...aka number
    if len(password) < 8 or not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
        return "Password must be at least 8 characters long and include both letters and numbers."

    # Hash the password using bcrypt.
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Using more HTML to show the user name and hashed pw if all validation
    # conditions are met.
    return f"""
    <h3>Login Successful</h3>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Hashed Password:</strong> {hashed_password.decode('utf-8')}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
