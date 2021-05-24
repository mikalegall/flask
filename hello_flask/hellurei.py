from flask import Flask

#Flask-luokan main konstruktori
app = Flask(__name__)

@app.route("/")
def index():
    return "Hei Mika!"

if __name__ == "__main__":
	app.run(debug=True) # testing only
	#app.run(port=8888) # testing only
