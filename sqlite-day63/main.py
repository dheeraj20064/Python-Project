import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# db=sqlite3.connect('library_management.db')
# cursor=db.cursor()
# cursor.execute("""CREATE TABLE books(id INTEGER PRIMARY KEY , title varchar(70) NOT NULL UNIQUE,
#                 author varchar(60) NOT NULL , rating FLOAT NOT NULL)""")
# cursor.execute("INSERT INTO books VALUES(2,'Avenger','Dheeraj',9.9)")
# db.commit()

# cursor.execute("INSERT INTO books VALUES(1,'Avengers','Dheeraj',9.9)")
# db.commit()
# cursor.execute("INSERT INTO books VALUE(3, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/HP/PycharmProjects/sqlite-day63/new_library_management.db'
db.init_app(app)

class Book(db.Model):
    __tablename__ = 'books'
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    title:Mapped[str] = mapped_column(String(60),unique=True,nullable=False)
    author:Mapped[str] = mapped_column(String(60),nullable=False)
    rating:Mapped[float] = mapped_column(Float,nullable=False)

# with app.app_context():
#     db.create_all()
#     new_book = Book(id=1,title='Bondessan',author='Undissan',rating=3.0)
#     db.session.add(new_book)
#     db.session.commit()

# with app.app_context():
#     books=db.session.execute(db.select(Book).order_by(Book.id)).scalars().all()
#     for book in books:
#         print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Rating: {book.rating}")
#
# with app.app_context():
#     book_to_update=db.session.execute(db.select(Book).where(Book.title=="Bondessan")).scalar()
#     book_to_update.title="Mandessan"
#     db.session.commit()

with app.app_context():
    book_to_delete=db.session.execute(db.select(Book).where(Book.title=="Mandessan")).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()




