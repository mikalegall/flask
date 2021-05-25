from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	db_a = ['a', 'b', 'c']
	db_b = []
	return render_template('base.html', ekahaku=db_a, tokahaku=db_b)

if __name__ == "__main__":
	app.run()
