from flask import Flask, url_for, render_template, request, redirect, flash
from flask_qrcode import QRcode
import time as t
import os
import warnings
import werkzeug

warnings.catch_warnings()
warnings.simplefilter("ignore")

app = Flask(__name__)
app.config['SECRET_KEY'] = "key"

qrcode = QRcode(app)

@app.route("/", methods=["GET","POST"])
def home():
    tab = request.args.get("tab")
    if tab == None: tab = "text"
    data = ""
    if(tab == "text"):
        if(request.method == "POST" and request.form["data"] != None):
            data = request.form["data"]
            qr = qrcode(data)

            print(f"TAB: {tab} =====> DATA: {data}")
            return render_template("index.html", tab="text", data=data, qr=qr)
        return (render_template("index.html", tab="text"))
    elif(tab == "link"):
        if(request.method == "POST" and request.form["data"] != None):
            data = request.form["data"]
            if ("https://" not in data) and ("http://" not in data):
                data = "https://" + data
            qr = qrcode(data)

            print(f"TAB: {tab} =====> DATA: {data}")
            return render_template("index.html",tab="link", data=data, qr=qr)
        return (render_template("index.html", tab="link"))
    elif(tab == "sms"):
        if(request.method == "POST" and request.form["to"] != None and request.form["content"] != None):
            to = request.form["to"]
            content = request.form["content"]
            try:
                to = int(to)
            except ValueError:
                pass
            data = f"SMSTO:{to}:{content}"
            qr = qrcode(data)

            print(f"TAB: {tab} =====> DATA: {data}")
            return(render_template("index.html", tab="sms", to=to, content=content, qr=qr))
        return (render_template("index.html", tab="sms"))
    else:
        return (render_template('404.html'), 404)


@app.errorhandler(404)
def page_not_found(error):
    return (render_template('404.html'), 404)
