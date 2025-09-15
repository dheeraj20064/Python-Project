from flask import Flask,render_template
app = Flask(__name__)
import requests

@app.route('/')
def home():
    return "HELLO WORLD"

@app.route('/<name>')
def guess(name):
    response1=requests.get(f"https://api.agify.io?name={name}")
    response2=requests.get(f"https://api.genderize.io?name={name}")
    Age=response1.json()['age']
    Gender=response2.json()['gender']
    return render_template('index.html',name=name,age=Age,Gender=Gender)

@app.route('/blog')
def blog():
    response1=requests.get("https://api.npoint.io/451a31cc3269562475ac")
    data=response1.json()
    return render_template('blog.html',data=data)
if __name__ == '__main__':
    app.run(debug=True)