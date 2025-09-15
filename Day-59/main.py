from flask import Flask,render_template
app = Flask(__name__)
import requests
response=requests.get("https://api.npoint.io/b7b256795de1c3c2ee88")
json=response.json()

@app.route('/')
def index():
    return render_template('index.html',posts=json)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    posts=next((post for post in json if post['id']==post_id), None)
    return render_template('post.html',post=posts)

if __name__ == '__main__':
    app.run(debug=True,port=5001)