from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")

firebaseConfig = {
  "apiKey": "AIzaSyDoygXW5pSHsIRuhsYVThPul93ZfJd358s",
  "authDomain": "cslab-a1779.firebaseapp.com",
  "projectId": "cslab-a1779",
  "storageBucket": "cslab-a1779.appspot.com",
  "messagingSenderId": "594084613762",
  "appId": "1:594084613762:web:e4feee33a605244c88ee9b",
  "measurementId": "G-NGJ0S11QFY",
  "databaseURL":""
}

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)