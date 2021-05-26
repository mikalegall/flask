from flask import Flask, render_template, redirect, flash

app = Flask(__name__)

#Cross Site Request Forgery estämiseen
app.secret_key = "mikalegall"

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/uudelleenohjaus")
def viestiKayttajalle():
    flash("Tämä on Flash viesti käyttöliittymässä näytettäväksi")
    return redirect("/")

if __name__ == "__main__":
	app.run()
