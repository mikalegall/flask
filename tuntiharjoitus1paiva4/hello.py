from flask import Flask, render_template, redirect # sudo apt install python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt install python3-flask-sqlalchemy

from flask_wtf import FlaskForm # sudo apt install python3-wtforms
from wtforms.ext.sqlalchemy.orm import model_form # sudo apt install python3-wtforms

app = Flask(__name__)
app.secret_key = 'ua7cheemoCietahlociethijieH9Ai' # sudo apt install pwgen; pwgen 30 1
db = SQLAlchemy(app)

class Kasvi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nimi = db.Column(db.Text, nullable=False)
    vari = db.Column(db.String, nullable=False)

@app.before_first_request
def alustaTietokanta():
        db.create_all()

        testiolio = Kasvi(nimi="TestiNimi", vari="TestiVari")
        db.session.add(testiolio)
        db.session.commit()

KasviLomake = model_form(Kasvi, base_class=FlaskForm, db_session=db.session)

@app.route("/", methods=["GET", "POST"])
def index():
    #return "hello"
    lomake = KasviLomake()
    if lomake.validate_on_submit():
        kasvi = Kasvi()
        lomake.populate_obj(kasvi)
        db.session.add(kasvi)
        db.session.commit()
        return redirect("/")
    kasvit = Kasvi.query.all()
    return render_template("index.html", lomake=lomake, kasvit=kasvit)

if __name__ == "__main__":
    app.run(debug=True)
