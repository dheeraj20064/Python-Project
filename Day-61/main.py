from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

''' 
On Windows type:
python -m pip install -r requirements.txt
'''

app = Flask(__name__)
app.secret_key = 'Dheeraj'

bootstrap = Bootstrap5(app)

class Loginform(FlaskForm):
    email=StringField("Email",validators=[DataRequired(),Email()])
    password=PasswordField("Password",[Length(min=8,max=32)])
    submit=SubmitField("Login")

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()

    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
