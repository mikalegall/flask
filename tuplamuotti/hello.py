from flask import Flask, render_template

app = Flask(__name__)


@app.route('/eka')
def eka():
    return render_template('eka.html')

@app.route('/toka')
def toka():
    return render_template('toka.html')

if __name__ == "__main__":
    app.run()
