from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "mikalegall"
db = SQLAlchemy(app)


class Merkinnat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kommentti = db.Column(db.String, nullable=False)
    tekija = db.Column(db.String, nullable=False)

MerkinnatLomake = model_form(Merkinnat, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def alustus():
    db.create_all()

    kommentti = Merkinnat(kommentti="Kukkuu", tekija="Minä")
    db.session.add(kommentti)

    kommentti = Merkinnat(kommentti="Huhuu", tekija="Sinä")
    db.session.add(kommentti)

    db.session.commit()


@app.route('/')
def index():
	kyselytulokset = Merkinnat.query.all()
	return render_template('index.html', lista=kyselytulokset)

@app.route("/ormform", methods=["GET", "POST"])
def addForm():
    lomake = MerkinnatLomake()
    print(request.form) #Kehityksen aikainen konsolituloste
    return render_template("ormform.html", form=lomake)

@app.route("/uudelleenohjaus")
def msgPage():
    flash("Flash viesti")
    return redirect("/ormform")

if __name__ == "__main__":
	app.run()
