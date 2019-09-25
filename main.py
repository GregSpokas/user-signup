from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_signup():

    return render_template('signup.html')

@app.route("/", methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "":
        username_error = "Please enter a username."
    if password == "":
        password_error = "Please enter a password."
    if verify_password == "":
        verify_error = "Please enter your password."
    if len(username) > 0:
        if len(username) < 3 or len(username) > 20 or re.search(r"\s",username):
            username_error = "Please enter a username between (3-20) characters or username contains spaces."
    if len(password) > 0:
        if len(password) < 3 or len(password) > 20 or re.search(r"\s",password):
            password_error = "Please enter a password between (3-20) characters or password contains spaces."
            password = ""
    
    if verify_password != password:
        verify_error = "Verify password does not match."
        verify_password = ""

    if len(email) > 0:

        if re.match(r"[^@\. ]{3,20}@[A-Za-z]+\.[A-Za-z]+",email):
            pass
        else:
            email_error = "Please enter an email between (3-20) characters and contains no spacing."
        

    if not username_error and not password_error and not verify_error and not email_error:

        return redirect('/valid-signup?username={0}'.format(username))

    else:
        return render_template('signup.html',
        username_error = username_error,
        password_error = password_error,
        verify_error = verify_error,
        email_error = email_error,
        username = username,
        password = password,
        verify = verify_password,
        email = email)

@app.route("/valid-signup")
def valid_signup():
    username = request.args.get('username')
    return render_template('sign_in_page.html', user_n=username)

app.run()