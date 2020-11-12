from flask import render_template, request, redirect, url_for, session, escape
from os import environ
from app import app

#set my secret key
app.secret_key = "ghaifafa"
#create session object for log in
users = {"sally": ("sally", "1234")}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")



@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":

        fullname = request.form.get("fullname")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        
        return redirect(url_for('dashboard'))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username in users and users[username][1] == password:
            print("Wrong Credentials")
            return redirect('request.url')
        else:
            session["username"] = username
            return redirect(url_for("dashboard"))

        
        
    return render_template("login.html")




@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return redirect(url_for('home'))