from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    tulosta = ""
    if "print_me" in request.form:
        tulosta = request.form["print_me"]
    return render_template('form_post.html', tulosta=tulosta)

if __name__ == "__main__":
    app.run()
