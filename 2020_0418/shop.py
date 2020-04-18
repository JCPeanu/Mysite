from flask import Flask, render_template
from flask import request, redirect

import sqlite3  

import sqlite_test as mydb

app = Flask(__name__)

@app.route('/')
def hello():
    title = "Shop Website"

    conn = sqlite3.connect('myshop.db')
    pds = mydb.getProducts(conn)
    return render_template('shop.html', title = title, products = pds)