from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String,Integer,Float
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)

class Library(db.Model):
    __tablename__ = 'library'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_name:Mapped[str]=mapped_column(String(60),unique=True,nullable=False)
    book_author:Mapped[str]=mapped_column(String(60),nullable=False)
    rating:Mapped[float]=mapped_column(Float,nullable=False)

@app.route('/')
def home():
    all_books = Library.query.all()
    return render_template('index.html', all_books=all_books)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        book_rating = request.form['book_rating']

        with app.app_context():
            db.create_all()
            book=Library(book_name=book_name,book_author=book_author,rating=book_rating)
            db.session.add(book)
            db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True,port=8080)

