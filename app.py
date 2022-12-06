from flask import Flask, render_template, url_for, redirect, request, jsonify, flash, abort
from flask_cors import CORS




app = Flask(__name__)
app.config["SECRET_KEY"] = "karan"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///exam.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["WTF_CSRF_ENABLED"] = False


cors = CORS(app)


@app.route("/")
def home():
    return render_template("mainPage.html")



if __name__ == "__main__":
    app.run(debug=True)
