from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "mikalegall"
db = SQLAlchemy(app)


class Vieraskirja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    viesti = db.Column(db.String, nullable=False)
    kirjoittaja = db.Column(db.String, nullable=False)


VieraskirjaLomake = model_form(Vieraskirja, base_class=FlaskForm, db_session=db.session)


@app.before_first_request
def alustus():
    db.create_all()


@app.route('/', methods=["GET", "POST"])
def index():

    lomake = VieraskirjaLomake()
    if "viesti" in request.form:
        viesti = request.form["viesti"]
        kirjoittaja = request.form["kirjoittaja"]
        merkinta = Vieraskirja(viesti=viesti, kirjoittaja=kirjoittaja)
        print("Merkintä = ", merkinta)
        db.session.add(merkinta)
        db.session.commit()
        return redirect("/")
    merkinnat = Vieraskirja.query.all()

    return render_template('index.html', lomake=lomake, merkinnat=merkinnat)

if __name__ == "__main__":
	app.run()
