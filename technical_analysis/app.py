#Docstring
"Stock and currency rate for technical analysis purposes"

import time
from flask import Flask, render_template, request, redirect
from services.analytics import analyze

#import atexit
#import datetime
# https://bitbucket.org/kruutti/data-web-application/src/master/
#from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
#Cross Site Request Forgery estämiseen
app.secret_key = "mikalegall"

@app.route("/", methods=["GET"])
def get_index():
    title = "Technical analysis tool"

    return render_template('index.html', title=title)

@app.route("/", methods=["POST"])
def post_index():

    target = ""
    short_rolling_mean = ""
    long_rolling_mean = ""

    if "target" in request.form:
        target = request.form["target"]
        short_rolling_mean = request.form["short_rolling_mean"]
        long_rolling_mean = request.form["long_rolling_mean"]
        results = analyze(target, short_rolling_mean, long_rolling_mean)
        print("Analyzes results = ", results)

    return redirect("/rate")


@app.route("/rate")
def rate():
    title = "Results for analysis"
    return render_template('rate.html', title=title)


# Local server only for development environment purposes
if __name__ == "__main__":
    # app.run(debug=True, port=8888)
    app.run()
