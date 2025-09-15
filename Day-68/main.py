from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
login_manager.login_message = "Please log in to access this page."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# CREATE TABLE IN DB

class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=="POST":
        unsafe_password=request.form['password']
        wrong_email=request.form['email']
        check_email=User.query.filter_by(email=wrong_email).first()
        if check_email:
            flash("Email already registered")
            return redirect(url_for('register'))
        new_user=User(
            email=request.form['email'],
            name=request.form['name'],
            password=generate_password_hash(unsafe_password, method='pbkdf2:sha256', salt_length=8),

        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets",name=new_user.name))

    return render_template("register.html")


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=="POST":
        email=request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user :
            flash("User not found")
            return redirect(url_for("login"))

        if not check_password_hash(user.password, password):
            flash("Password incorrect")
            return redirect(url_for("login"))

        login_user(user)
        return redirect(url_for("secrets",name=user.name))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name = request.args.get('name')
    return render_template("secrets.html",name=name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(
        directory="static/files",   # folder
        path="cheat_sheet.pdf",     # file name
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True,port=5001)
