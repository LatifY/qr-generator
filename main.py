from flask import Flask, url_for, render_template, request, redirect, flash
from flask_qrcode import QRcode
import time as t
import os
import warnings

warnings.catch_warnings()
warnings.simplefilter("ignore")

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

qrcode = QRcode(app)


@app.context_processor
def my_utility_processor():
    def getQR():
        qr = url_for("static", filename="img/qrcode.png")
        return qr

    return dict(getQR=getQR)

@app.route("/", methods=["GET","POST"])
def home():
    if(request.method == "GET" and request.args.get("data") != None):
        data = request.args.get("data")
        qr = qrcode(data)

        print(qr)

        return render_template('index.html', data=data,qr=qr)
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return (render_template('404.html'), 404)
