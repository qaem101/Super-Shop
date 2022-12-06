from flask import Flask, render_template, url_for, redirect, request, jsonify, flash, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SECRET_KEY"] = "karan"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///e-commerce.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["WTF_CSRF_ENABLED"] = False


cors = CORS(app)
db = SQLAlchemy(app)
app.app_context().push()



# SQLALCHEMY TABLES


class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Integer, nullable=False)


# class User(db.Model, UserMixin):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     roll_no = db.Column(db.Integer, unique=True, nullable=False)
#     password = db.Column(db.String(50), nullable=False)






@app.route("/")
def home():
    # db.create_all()

    return render_template("mainPage.html")


# add product to cart
@app.route("/add")
def add():
    form_data = request.form.to_dict()
    print(form_data)

    # image_names = request.form["image_name"]
    # product_names = request.form["image_name"]
    # prices = request.form["image_name"]
    #  = request.form["image_name"]
    # image_name = request.form["image_name"]



    return render_template("cart.html")




# remove product from cart

@app.route("/remove")
def remove():
    product_name = request.form["product_name"]
    db.session.query(Cart).filter(Cart.product_name == product_name).delete()

    return render_template("cart.html")
    


if __name__ == "__main__":
    app.run(debug=True)
