from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
Bootstrap(app)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/shop_single')
def shop_single():
    return render_template("shop-single.html")


@app.route('/shop')
def shop():
    return render_template("shop.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)

