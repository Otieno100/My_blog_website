from .import app
from flask import render_template
from .import quote
from .import request


@app.route('/')
def home():
    quote =[]
    for i in range(11):
        req = request()
        data = req.request('')
        quote.append(quote.Quote(data["id"],data["author"],data["quote"]))



    return render_template('',datum = quote)
