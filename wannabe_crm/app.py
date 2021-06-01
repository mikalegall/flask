from datetime import datetime
# sudo apt install python3-flask
from flask import Flask, render_template, redirect, flash
# sudo apt install python3-flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm  # sudo apt install python3-wtforms
from wtforms.ext.sqlalchemy.orm import # sudo apt install python3-flaskext.wtf

app = Flask(__name__)
# sudo apt install pwgen; pwgen 30 1
app.secret_key = 'ua7cheemoCietahlociethijieH9Ai'
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///kyy'
db = SQLAlchemy(app)

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_time_saved = db.Column(db.DateTime, default=datetime.utcnow)
    last_time_edited = db.Column(db.DateTime, default=datetime.utcnow)
    family_name = db.Column(db.String, nullable=False)
    given_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    telephone = db.Column(db.String)
    record_deleted = db.Column(db.Boolean)


@app.before_first_request
def setUp_db():
    db.create_all()
    #dummy = Customer(family_name="FamilynameTest", given_name="GivennameTest", email="test@test-eu", record_deleted=False)
    #db.session.add(dummy)
    #db.session.commit()


CustomerForm = model_form(Customer, base_class=FlaskForm, db_session=db.session)

# https://flask.palletsprojects.com/en/1.0.x/quickstart/#http-methods
@app.route("/<int:id>/edit", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index(id=None):  # optional
    customer = Customer()
    if id:
        customer = Customer.query.get_or_404(id)
        if customer.record_deleted == True:
            flash("Something went wrong (could not find any records to modify)")
            return redirect("/")

    form = CustomerForm(obj=customer)

    if form.validate_on_submit():
        form.populate_obj(customer)
        customer.last_time_edited = datetime.utcnow()
        db.session.add(customer)
        db.session.commit()
        flash("Saved")
        return redirect("/")

    all_customers = Customer.query.all()
    customers=[]
    for customer in all_customers:
        if not customer.record_deleted == True:
            customers.append(customer)
    return render_template("index.html", form=form, customers=customers)


@app.route("/<int:id>/delete")
def deleteCustomer(id):
    customer = Customer.query.get_or_404(id)

    if customer.record_deleted == True:
        flash("Nothing to delete (already deleted earlier)")
        return redirect("/")

    customer.record_deleted = True
    db.session.add(customer)
    # db.session.delete(customer) #This would actually delete record for real 
    db.session.commit()

    flash("Deleted!")
    return redirect("/")


# Local server only for development environment purposes
if __name__ == "__main__":
    # app.run(debug=True, port=8888)
    app.run()
