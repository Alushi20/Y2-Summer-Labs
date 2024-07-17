from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/fortune')
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


    ]
    chosen_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=chosen_fortune)





if __name__ == '__main__':
    app.run(debug=True)