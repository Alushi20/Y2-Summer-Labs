from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase

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

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])
def signup():
     print("eee222")
     if request.method == 'GET':
        return render_template("signup.html") 
     else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        print("ooooooo")
        login_session['user'] = auth.create_user_with_email_and_password(email, password)
        login_session["quotes"]=[]
        return redirect(url_for('home'))




@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        print("ooo")
        login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        login_session["quotes"]=[]
        return redirect(url_for('home'))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template("home.html")
    else:
        quote=request.form["quote"]
        login_session['quotes'].append(quote)
        login_session.modified = True
        return redirect(url_for('thanks'))
    
@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    return render_template("thanks.html")

@app.route('/display', methods=['GET', 'POST'])
def display():
    quote=login_session['quotes']
    print(quote)
    return render_template("display.html",quote=quote)

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    login_session['user'] = None
    return render_template("signout.html")


if __name__ == '__main__':
    app.run(debug=True)