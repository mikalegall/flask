from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('base.html')

@app.route('/hae', methods=["GET"])
def index2():
        return render_template('form_get.html')

@app.route('/puske', methods=["GET", "POST"])
def index3():
        return render_template('form_post.html')

if __name__ == "__main__":
	app.run()
