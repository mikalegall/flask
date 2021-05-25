from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	lista = ["eka", "toka", "kolmas"]
	return render_template('base.html', nimi='Mika', list=lista)

if __name__ == "__main__":
	app.run()
