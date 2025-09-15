import requests
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
from sqlalchemy import column

'''
On Windows type:
python -m pip install -r requirements.txt
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafu.db?check_same_thread=False'

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name:getattr(self,column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result=db.session.execute(db.select(Cafe))
    all_cafes=result.scalars().all()
    random_cafe=random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result=db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes=result.scalars().all()
    return jsonify([cafe.to_dict() for cafe in all_cafes])

@app.route("/search/<cafe_location>")
def search_cafe(cafe_location):
    result=db.session.execute(db.select(Cafe).order_by(Cafe.name).where(Cafe.location==cafe_location))
    all_cafes=result.scalars().all()
    if all_cafes:
        return jsonify([cafe.to_dict() for cafe in all_cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# HTTP POST - Create Record
@app.route("/add_cafe",methods=["POST"])
def add_cafe():
    data = request.get_json()
    db.session.add(Cafe(**data))
    db.session.commit()
    return jsonify({"response":"success",
                   "data":data})


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<cafe_id>",methods=["PATCH"])
def update_price(cafe_id):
    try:
        cafe = Cafe.query.get(cafe_id)
        new_price = request.form.get("new_price")
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify({"response":"success"})
        else:
            return jsonify({"error":"Not Found"})
    except:
        return jsonify({"error":"Something went wrong"}), 404


# HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    print("Looking for cafe with ID:", cafe_id)
    cafe = Cafe.query.get(cafe_id)
    print("Found cafe:", cafe)
    api_key=request.form.get("api_key")
    if cafe :
        if  api_key=="TopSecretKey":
            db.session.delete(cafe)
            db.session.commit()
            return jsonify({"response": "success"}), 200
        else:
            return jsonify({"error":"You entered the wrong api"}), 401
    else:
        return jsonify({"error": "Not Found"}), 404




if __name__ == '__main__':
    app.run(debug=True)
