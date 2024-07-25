from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session
import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyB-XRkT6_I6O_oYE7gTozsp0E7WSBRa5WE",
  "authDomain": "project-a7cfa.firebaseapp.com",
  "projectId": "project-a7cfa",
  "storageBucket": "project-a7cfa.appspot.com",
  "messagingSenderId": "1089672582949",
  "appId": "1:1089672582949:web:0baa2162ec3adb514eeccc",
  "measurementId": "G-QM1FVTZMGC",
  "databaseURL":"https://project-a7cfa-default-rtdb.europe-west1.firebasedatabase.app/"
}
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()

@app.route('/')
def start():
    return render_template("start.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        username=request.form['username']
        try:
            login_session['user']=auth.create_user_with_email_and_password(email,password)
            id=login_session['user']['localId']
            user={"email":email,"password":password,"username":username}
            db.child("users").child(id).set(user)
            login_session["username"]=user["username"]
            return redirect(url_for('profile'))
        except Exception as e:
           return render_template("signup.html", error=e)
  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']

        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            login_session["username"]=db.child("users").child(login_session['user']["localId"]).child("username").get().val()
            return redirect(url_for('profile'))
        except Exception as e:
            return render_template("login.html", error=e)
        
@app.route('/signout', methods=['GET', 'POST'])
def signout():
    login_session['user'] = None
    return render_template("signout.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")




@app.route('/review',methods=["GET","POST"])
def review():
     if request.method == 'GET':
        return render_template("review.html") 
     else: #if the method is post
        title = request.form['title']
        rating = request.form['rating']
        review1=request.form['review']
        fav_quote = request.form['fav_quote']
        user=db.child("users").get().val()
        login_session["title"]=title
        login_session["rating"]=rating
        login_session["review"]=review1
        login_session["fav_quote"]=fav_quote
        review={"title":title,"rating":rating,"review":review1,"fav_quote":fav_quote}
        db.child("reviews").push(review)
        db.child("users").child(login_session["user"]["localId"]).child("reviews").push({"title":title,"review":review1,"rating":rating,"fav_quote":fav_quote})
        return render_template("profile.html",reviews=db.child("users").child(login_session["user"]["localId"]).child("reviews").get().val())

@app.route('/profile',methods=["GET","POST"])
def profile():
    return render_template("profile.html",username=login_session["username"],reviews=db.child("users").child(login_session["user"]["localId"]).child("reviews").get().val())

        

@app.route('/main')
def main():
    reviews=db.child("reviews").get().val()
    user=db.child("users").get().val()
    return render_template("main.html",reviews=reviews,user=user)




if __name__ == '__main__':
    app.run(debug=True)