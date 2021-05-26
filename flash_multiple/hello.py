from flask import Flask, render_template, redirect, flash

app = Flask(__name__)

#Cross Site Request Forgery estämiseen
app.secret_key = "mikalegall"

@app.route('/')
def index():
	message = "Tämä viesti on etusivun Flashin jonopuskurista"
	flash(message)
	return render_template('index.html')

@app.route("/uudelleenohjaus")
def viestiKayttajalle():
    flash('"Uudelleeohjaus" linkistä tallennettu  Flash viesti käyttöliittymässä näytettäväksi, mutta sitä ei näytetä etusivulla')
    return redirect("/")

@app.route("/vilauta")
def vilauta():
	flash("KlikkaaMua kautta tulostettu viesti")
	return render_template("vilauta.html")

if __name__ == "__main__":
	app.run()
