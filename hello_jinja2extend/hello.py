from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	lista = ["eka", "toka", "kolmas"]
	return render_template('base.html', nimi='Mika', list=lista)

@app.route('/kukkuu')
def uusi():
	return render_template('lorem.html')

if __name__ == "__main__":
	app.run(debug=True, port=8888)
