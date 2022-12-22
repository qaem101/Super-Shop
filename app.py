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


ID =0


@app.route("/button")
def about():
    # db.create_all()
    return render_template("button.html")


@app.route("/about")
def about():
    # db.create_all()
    return render_template("about.html")

@app.route("/shop1")
def shop1():
    # db.create_all()
    return render_template("shop1.html")

@app.route("/loginPage")
def loginPage():
    # db.create_all()
    return render_template("loginPage.html")

@app.route("/contact")
def contact():
    # db.create_all()
    return render_template("contact.html")

@app.route("/shop")
def shop():
    # db.create_all()
    return render_template("shop.html")


@app.route("/")
def home():
    # db.create_all()
    return render_template("mainPage.html")


@app.route("/cart")
def cart():
    # db.create_all()
    return render_template("cart.html")

# add product to cart
@app.route("/add")
def add():
    # data = eval(product_data)
    # print(data)
    # image_names = request.form["image_name"]
    product_name = request.args['pname']
    price = request.args['price']
    quant=request.args['quant']
    #  = request.form["image_name"]
    # image_name = request.form["image_name"]
    global ID
    ID=len(db.session.query(Cart).all())+2
    cart = Cart(id=ID,product_name=product_name, price=price,quantity=quant,subtotal=int(price)*int(quant))
    db.session.add(cart)
    db.session.commit()


    return render_template("cart.html")




# remove product from cart

@app.route("/remove")
def remove():
    id = request.args['pid']
    db.session.query(Cart).filter(Cart.id == id).delete()
    db.session.commit()
    return render_template("cart.html")

@app.route("/show-product/<product_name>")
def show_product(product_name):
    return render_template(f"{product_name}.html")
    
@app.route("/show")
def show():
    main={}
    temp={}
    all = db.session.query(Cart).all()

    # convert all variable to dictionary in less lines of code
    all = [i.__dict__ for i in all]
    # remove _sa_instance_state from all
    for i in all:
        i.pop("_sa_instance_state")

    print(all)


    # print(all) 
    # for keyd in range(1,len(all)):
    #     li=all[keyd]
    #     for key ,value in li.__dict__.items():
    #         if not key.startswith('_'):
    #             temp[key]=value
        
    #     main[keyd]=temp
        
    return jsonify(all)



if __name__ == "__main__":
    app.run(debug=True)

