from datetime import datetime 
from flask import Flask, render_template, redirect, flash, session # sudo apt install python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt install python3-flask-sqlalchemy
from flask_wtf import FlaskForm  # sudo apt install python3-wtforms
from wtforms.ext.sqlalchemy.orm import model_form

from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, validators


app = Flask(__name__)
app.secret_key = 'ua7cheemoCietahlociethijieH9Ai' # sudo apt install pwgen; pwgen 30 1
db = SQLAlchemy(app)

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
class User(db.Model):
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
    password = PasswordField("Password", validators=[
                             validators.InputRequired()])

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
class BookReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, nullable=False)
    review = db.Column(db.String(160), nullable=False)


@app.before_first_request
def setUp_db():
    db.create_all()
    dummyUser = User(family_name="FamilynameTest", given_name="GivennameTest",
                     email="test@test-eu", record_deleted=False)
    dummyUser.setPassword("näkkileipä")
    db.session.add(dummyUser)
    dummyUser = User(family_name="SukunimiTesti", given_name="EtunimiTesti",
                     email="foo@bar.com", record_deleted=False)
    dummyUser.setPassword("pöö")
    db.session.add(dummyUser)
    dummyReview = BookReview(book_name="Raamattu",
                             review="Aikamoinen luomiskertomus")
    db.session.add(dummyReview)
    dummyReview = BookReview(
        book_name='https://armas.btj.fi/request.php?id=f55f7189859e3777&pid=9780007438785&qtype=b   ', review="Standalone toteutus (Flask)")
    db.session.add(dummyReview)
    db.session.commit()


UserForm = model_form(User, base_class=FlaskForm, db_session=db.session)
BookReviewForm = model_form(
    BookReview, base_class=FlaskForm, db_session=db.session)


def currentUser():
    try:
        uid = int(session["uid"])
    except:
        return None
    return User.query.get(uid)

app.jinja_env.globals["currentUser"] = currentUser


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


# @app.route("/user/<int:id>/delete")
# def deleteUser(id):
#     user = User.query.get_or_404(id)

#     if user.record_deleted == True:
#         flash("Nothing to delete (already deleted earlier)")
#         return redirect("/")

#     user.record_deleted = True
#     db.session.add(user)
#     # db.session.delete(user) #This would actually delete record for real
#     db.session.commit()

#     flash("Deleted!")
#     return redirect("/")


@app.route("/", methods=["GET", "POST"])
def indexView():
    bookReview = BookReview()
    form = BookReviewForm(obj=bookReview)

    if form.validate_on_submit():
        form.populate_obj(bookReview)
        db.session.add(bookReview)
        db.session.commit()
        flash("Saved")
        return redirect("/")

    bookReviews = BookReview.query.all()
    return render_template("index.html", form=form, bookReviews=bookReviews)


# Local server only for development environment purposes
if __name__ == "__main__":
    # app.run(debug=True, port=8888)
    app.run()
