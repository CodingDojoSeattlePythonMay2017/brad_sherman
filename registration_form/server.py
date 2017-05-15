from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "secret"
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/process', methods=['POST'])
def formSubmit():
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']
    passwordConfirm = request.form['passwordconfirm']
    birthDate = request.form['birthday']

    # Empty fields check
    if len(email) < 1 or len(firstname) < 1 or len(lastname) < 1 or len(password) < 1 or len(passwordConfirm) < 1:
        flash("All fields must be completed.")
        return redirect ('/')

    # email validation
    if not EMAIL_REGEX.match(email):
        flash("Email is invalid.")
        return redirect ('/')

    # First/Last names containing numbers check
    if any(char.isdigit() for char in firstname) or any(char.isdigit() for char in lastname):
        flash("Name fields cannot contain numbers.")
        return redirect ('/')

    # Password more than 8 characters check
    if len(password) < 9 or len(passwordConfirm) < 9:
        flash("Password must be more than 8 characters.")
        return redirect ('/')

    if password != passwordConfirm:
        flash("Password must match confirmed password.")
        return redirect ('/')

    # Password must have one uppercase letter and 1 numeric value
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password):
        return redirect ('/')
    else:
        flash("Password must have at least one number and one capital letter.")
        return redirect('/')

    # Date validation



app.run(debug=True)




    # valid email check goes here
