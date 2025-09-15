from flask import Flask,render_template
app = Flask(__name__, template_folder='templates', static_folder='static')
import random
from datetime import datetime

Api="d95bbe70a49b919b3790a17753f10570"
https://api.agify.io?name=michael

random_number = random.randint(1,10)
date=datetime.now()
year=date.year
name="Dheeraj"

@app.route('/')
def home():
    return render_template('index.html',num=random_number,year=year,name=name)

@app.route('/guess')
def guess():

if __name__ == '__main__':
    app.run(debug=True)