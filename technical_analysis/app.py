#Docstring
"Stock and currency rate for technical analysis purposes"

from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, session # sudo apt install python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt install python3-flask-sqlalchemy
from flask_wtf import FlaskForm  # sudo apt install python3-wtforms
from wtforms.ext.sqlalchemy.orm import model_form # sudo apt install python3-flaskext.wtf

from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, validators

from services.analytics import analyze

app = Flask(__name__)
#Cross Site Request Forgery estämiseen
app.secret_key = "ofea8Aejesei9aeti7theiyieL5uch" # sudo apt install pwgen; pwgen 30 1
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///kyy'
db = SQLAlchemy(app)

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_time_saved = db.Column(db.DateTime, default=datetime.utcnow)
    last_time_edited = db.Column(db.DateTime, default=datetime.utcnow)
    family_name = db.Column(db.String)
    given_name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    telephone = db.Column(db.String)
    passwordHash = db.Column(db.String, nullable=False)
    record_deleted = db.Column(db.Boolean)

    def setPassword(self, password):
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.passwordHash, password)

# https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/
class RegisterLoginForm(FlaskForm):
    email = StringField("Email", validators=[validators.Email()])
    password = PasswordField("Password", validators=[validators.InputRequired()])

@app.before_first_request
def setUp_db():
    db.create_all()
    # dummyUser = User(family_name="FamilynameTest", given_name="GivennameTest",
    #                  email="test@test-eu", record_deleted=False)
    # dummyUser.setPassword("näkkileipä")
    # db.session.add(dummyUser)
    # dummyUser = User(family_name="SukunimiTesti", given_name="EtunimiTesti",
    #                  email="foo@bar.com", record_deleted=False)
    # dummyUser.setPassword("pöö")
    # db.session.add(dummyUser)

UserForm = model_form(User, base_class=FlaskForm, db_session=db.session)

def currentUser():
    try:
        uid = int(session["uid"])
    except:
        return None
    return User.query.get(uid)

app.jinja_env.globals["currentUser"] = currentUser # currentUser() can be used in templates

@app.errorhandler(404)
def custom404(e):
    # return render_template("404.html")
    flash("HTTP 404 Not Found")
    return redirect("/")

# https://flask.palletsprojects.com/en/1.0.x/quickstart/#http-methods
@app.route("/user/register", methods=["GET", "POST"])
def registerView():
    form = RegisterLoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if User.query.filter_by(email=email).first():
            flash("Account with that email already exist, just log in!")
            return redirect("/user/login")

        user = User(first_time_saved=datetime.utcnow(), email=email)
        user.setPassword(password)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(email=email).first()
        session["uid"] = user.id
        flash("Congratulations, you are logged in!")
        return redirect("/user/"+str(user.id)+"/modify")

    return render_template("register.html", form=form)


@app.route("/user/login", methods=["GET", "POST"])
def loginView():
    form = RegisterLoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Please, try again")
            return redirect("/user/login")
        if not user.checkPassword(password):
            flash("Please, try again")
            return redirect("/user/login")

        session["uid"] = user.id

        flash("Login successful")
        return redirect("/user/"+str(user.id)+"/modify")

    return render_template("login.html", form=form)


@app.route("/user/logout")
def logoutView():
    if not currentUser():
        return redirect("/")

    session["uid"] = None
    flash("Logged out")
    return redirect("/")

# Index.html "Oma profiili"
@app.route("/user/profile")
def profileRedirect():
    if currentUser():
        user = currentUser()
        return redirect("/user/"+str(user.id)+"/modify")
    return redirect("/")

@app.route("/user/<int:id>/modify", methods=["GET", "POST"])
def profileView(id):
    user = User.query.get_or_404(id)
    if user.record_deleted == True:
        flash("Something went wrong (could not find profile to modify)")
        return redirect("/")
    form = UserForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        user.last_time_edited = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        flash("Saved")
        return redirect("/user/"+str(user.id)+"/modify")

    return render_template("usermodify.html", form=form, user=user)

@app.route("/", methods=["GET"])
def get_index():
    title = "Automated technical financial analysis tool"

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
def rateView():
    if not currentUser():
        return redirect("/")

    title = "Results for analysis"
    return render_template('rate.html', title=title)

@app.route("/roadmap")
def roadmapView():
    return render_template('roadmap.html')

# Local server only for development environment purposes
if __name__ == "__main__":
    # app.run(debug=True, port=8888)
    app.run()
