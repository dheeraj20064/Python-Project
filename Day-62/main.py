from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators ,SelectField
from wtforms.validators import DataRequired,URL
import csv

'''
On Windows type:
python -m pip install -r requirements.txt
This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap=Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url=StringField('Location URL', validators=[DataRequired(),validators.URL()])
    opening_time=StringField('Opening time', validators=[DataRequired()])
    closing_time=StringField('Closing time', validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=[
        ("☕", "☕"),
        ("☕☕", "☕☕"),
        ("☕☕☕", "☕☕☕"),
        ("☕☕☕☕", "☕☕☕☕"),
        ("☕☕☕☕☕", "☕☕☕☕☕")
    ],
    validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Rating", choices=[
        ("💪", "💪"),
        ("💪💪", "💪💪"),
        ("💪💪💪", "💪💪💪"),
        ("💪💪💪💪", "💪💪💪💪"),
        ("💪💪💪💪💪", "💪💪💪💪💪")
    ],
    validators=[DataRequired()])

    power_rating = SelectField("Power Rating", choices=[
        ("🔌", "🔌"),
        ("🔌🔌", "🔌🔌"),
        ("🔌🔌🔌", "🔌🔌🔌"),
        ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
        ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")
    ],
    validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add',methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe= form.cafe.data
        url = form.url.data
        opening= form.opening_time.data
        closing= form.closing_time.data
        coffee= form.coffee_rating.data
        wifi = form.wifi_rating.data
        power = form.power_rating.data
        with open('cafe-data.csv','a',newline='',encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([cafe, url, opening,closing, coffee, wifi, power])
        return redirect(url_for("cafes"))

    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)
