from flask import render_template

from app import app
@app.route('/')
def index():
    return("Welcome")

@app.route('/signup')
def signup():
    return render_template("signup.html")


@app.route('/login')
def login():
    return render_template("login.html")