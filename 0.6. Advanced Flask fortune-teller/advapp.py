from flask import Flask, render_template, request,url_for,redirect
import random

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template('advhome.html')
    else:
        birthday=request.form["birthday"]
        return redirect(url_for('fortune',date=birthday))




@app.route('/fortune/<date>')
def fortune(date):
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
    if len(date)>9:
        chosen_fortune = fortunes[len(date)]
        return render_template('fortune.html', fortune=chosen_fortune)
    else:
        random.choice(fortunes)
        chosen_fortune=random.choice(fortunes)
        return render_template('fortune.html', fortune=chosen_fortune)







if __name__ == '__main__':
    app.run(debug=True)