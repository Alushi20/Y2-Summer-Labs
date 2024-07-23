from flask import Flask, render_template, request,url_for,redirect
import random
from flask import session as login_session 
app = Flask(__name__)
app.config['SECRET_KEY']="PASSWORD"

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template('loginhome.html')
    else:
        login_session["name"]=request.form["username"]
        login_session["birthday"]=request.form["birthday"]
        return redirect(url_for('fortune'))
        if name == 'admin':
            login_session["admin"] = True
        else:
            login_session["admin"] = False
        return redirect(url_for('home'))



@app.route('/loginadvfortune/<date>')
def fortune():
    fortunes = [
        "You'll have a bad day:(",
        "You'll have a phenomenal:D",
        "Expect the unexpected!",
        "Your dreams will come true!",
        "Good news are coming!",
        "You will achieve your goals.",
        "You will meet someone special.",
        "Today is your lucky day!",
        "a bird will poop on your head"


    ]
    if len(login_session["date"])>9:
        chosen_fortune = fortunes[len(date)]
        return render_template('loginadvfortune.html', fortune=chosen_fortune)
    else:
        random.choice(fortunes)
        chosen_fortune=random.choice(fortunes)
        return render_template('loginadvfortune.html', fortune=chosen_fortune)







if __name__ == '__main__':
    app.run(debug=True)