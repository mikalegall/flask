from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Merkinnat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kommentti = db.Column(db.String, nullable=False)
    tekijä = db.Column(db.String, nullable=False)


@app.before_first_request
def alustus():
    db.create_all()

    kommentti = Merkinnat(kommentti="Kukkuu", tekijä="Minä")
    db.session.add(kommentti)

    kommentti = Merkinnat(kommentti="Huhuu", tekijä="Sinä")
    db.session.add(kommentti)

    db.session.commit()


@app.route('/')
def index():
	kyselytulokset = Merkinnat.query.all()
	return render_template('index.html', lista=kyselytulokset)


if __name__ == "__main__":
	app.run()
