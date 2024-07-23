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
     if request.method == 'GET':
        return render_template("signup.html") 
     else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        fullname=request.form["Full_name"]
        try:
            login_session['user']=auth.create_user_with_email_and_password(email,password)
            id=login_session['user']['localid']
            user={"email":email,"password":password,"fullname":fullname}
            db.child("users").child(id).set(user)
            login_session['quotes']=[]
            return redirect(urlfor('home'))
        except:
            error="error"
            return render_template("signup.html",error=error)




@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("signin.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Error"
            return render_template("signin.html", error=error)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if login_session['user'] == None:
        return redirect(url_for('signup'))
    if request.method=='GET':
     return render_template("home.html")
    elif request.form['action'] == 'signout':
        login_session['user'] = None
        auth.current_user = None
        return redirect(url_for('login'))
    else:
        qoute = {"text":request.form['quote'],"said_by":request.form['speaker'],"uid":login_session['user']['localId']}
        db.child("Qoutes").push(qoute)
        return redirect(url_for('thanks'))

    
@app.route('/thanks', methods=['GET', 'POST'])
def thanks():
    if login_session['user'] == None:
        return redirect(url_for('signup'))
    if request.method == "GET":
        return render_template("thanks.html")

@app.route('/display', methods=['GET', 'POST'])
def display():
    if login_session['user'] == None:
        return redirect(url_for('signup'))
    if request.method == "GET":
        Qoutes=db.child("Qoutes").get().val()
        return render_template("display.html",qoutes=Qoutes)

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    login_session['user'] = None
    return render_template("signout.html")


if __name__ == '__main__':
    app.run(debug=True)