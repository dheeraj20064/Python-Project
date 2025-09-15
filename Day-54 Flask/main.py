from flask import Flask
app = Flask(__name__)

app=Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>'\

def make_bold(function):
    def bold_function():
        return "<b>"+function()+"</b>"
    return  bold_function

def make_italic(function):
    def italic_function():
        return "<i>"+function()+"</i>"
    return italic_function


def make_underline(function):
    def underline_function():
        return "<u>"+function()+"</u>"
    return underline_function



@app.route('/bye')
@make_bold
@make_italic
@make_underline
def bye():
    return 'bye'

@app.route('/<name>/<int:age>')
def username(name,age):
    return f"My name is {name} and i am {age} old"


if __name__=='__main__':
    app.run(debug=True)