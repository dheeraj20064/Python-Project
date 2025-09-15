print("This is")
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, New Project!"

@app.route('/test')
def test():
    return "TEST ROUTE FROM NEW PROJECT 🚀"


if __name__ == '__main__':
    app.run(debug=True,port=5000)


