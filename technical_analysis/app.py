"Stock and currency rate for technical analysis purposes"
import time
from flask import Flask, render_template
import atexit
import datetime
# https://bitbucket.org/kruutti/data-web-application/src/master/
#from apscheduler.schedulers.background import BackgroundScheduler
from analytics import analyze

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    title = "Technical analysis tool"
    return render_template('index.html', title=title)


@app.route("/rate")
def rate():
    title = "Results for analysis"
    return render_template('rate.html', title=title)


# For local development
if __name__ == "__main__":
    app.run()
