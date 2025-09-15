from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

'''
On Windows type:
python -m pip install -r requirements.txt
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies_list.db'
db=SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE

class Movies(db.Model):
    __tablename__ = 'movies'
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(60),unique=True)
    year:Mapped[int] = mapped_column(Integer,nullable=True)
    description:Mapped[str] = mapped_column(String,nullable=True)
    rating:Mapped[float] = mapped_column(Float,nullable=False,default=5)
    ranking:Mapped[float] = mapped_column(Float,nullable=True,default=0)
    review:Mapped[str] = mapped_column(String,nullable=True)
    img_url:Mapped[str] = mapped_column(String)

# new_movie= Movies(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
with app.app_context():
    db.create_all()

    # movies_to_add = [
    #     Movies(
    #         title="Inception",
    #         year=2010,
    #         description="A skilled thief who steals corporate secrets through dream-sharing technology is given a chance at redemption if he can successfully perform an inception.",
    #         rating=8.8,
    #         ranking=9,
    #         review="Mind-bending and visually stunning!",
    #         img_url="https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg"
    #     ),
    #     Movies(
    #         title="The Matrix",
    #         year=1999,
    #         description="A computer hacker learns about the true nature of reality and his role in the war against its controllers.",
    #         rating=8.7,
    #         ranking=8,
    #         review="Revolutionary in both story and special effects.",
    #         img_url="https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"
    #     ),
    #     Movies(
    #         title="Interstellar",
    #         year=2014,
    #         description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
    #         rating=8.6,
    #         ranking=7,
    #         review="A beautiful mix of science and emotion.",
    #         img_url="https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
    #     ),
    #     Movies(
    #         title="The Dark Knight",
    #         year=2008,
    #         description="Batman must accept one of the greatest psychological and physical tests when he faces the Joker, a criminal mastermind wreaking havoc on Gotham.",
    #         rating=9.0,
    #         ranking=6,
    #         review="Heath Ledger's Joker is unforgettable.",
    #         img_url="https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
    #     ),
    # ]

    # for movie in movies_to_add:
    #     if not Movies.query.filter_by(title=movie.title).first():
    #         db.session.add_all(movies_to_add)  # ✅ add them all at once
    #         db.session.commit()  # ✅ one commit for all

@app.route("/")
def home():
    all_movies = db.session.execute(db.select(Movies).order_by(Movies.rating.desc(),Movies.title.asc())).scalars().all()

    for index,movie in enumerate(all_movies,start=1):
        movie.ranking = index
    return render_template("index.html", movies=all_movies)

class EditingForm(FlaskForm):
    rating = FloatField('rating',validators=[DataRequired()])
    review = StringField('review',validators=[DataRequired()])
    submit = SubmitField('Done')

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movies.query.get(movie_id)
    form=EditingForm(obj=movie)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)

@app.route("/delete/<int:movie_id>",methods=["GET","POST"])
def delete(movie_id):
    delete_movie = db.session.execute(db.select(Movies).where(Movies.id == movie_id)).scalar()
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for("home"))


class Add_movie(FlaskForm):
    title = StringField('title',validators=[DataRequired()])
    submit = SubmitField('Add movie')

api_key = "d65c9b71"


@app.route("/add", methods=["GET", "POST"])
def add():
    form = Add_movie()
    if form.validate_on_submit():
        title = form.title.data
        url = f"http://www.omdbapi.com/?s={title}&apikey={api_key}"
        response = requests.get(url)
        data = response.json()
        movies=data.get('Search',[])
        return render_template('select.html',movies=movies)

    return render_template("add.html", form=form)


@app.route("/find<imdb>")
def find(imdb):
    url=f"http://www.omdbapi.com/?i={imdb}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['Response'] == 'True':
        new_movie = Movies(
            title=data['Title'],
            year=int(data['Year']) if data['Year'].isdigit() else None,
            description=data['Plot'],
            rating=float(data['imdbRating']) if data['imdbRating'] != "N/A" else None,
            ranking=None,  # You can update this later
            review="",  # Leave empty, user can edit it
            img_url=data['Poster']
        )

        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit",movie_id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True,port=5000)

