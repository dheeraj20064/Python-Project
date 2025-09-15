from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/post')
def home():
    response= requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    json_response = response.json()
    return render_template("index.html", posts=json_response)

@app.route('/post/<int:post_id>')
def detail(post_id):
    responses=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    json_response = responses.json()
    post=next((post for post in json_response if post['id'] == post_id), None)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
