from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	lista = ["viinirypäle", "mandariini", "kirsikka"]
	return render_template('base.html', list=lista)

if __name__ == "__main__":
	app.run()
