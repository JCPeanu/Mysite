from flask import Flask, render_template
from flask import request, redirect

import sqlite3
from flask import g

app = Flask(__name__)

products = {
  "sku01": { 
      "id": "sku01", 
      "name": "Pen", 
      "price": 15, 
      "desc": "This is a pen.", 
      'src': 'https://cdn11.bigcommerce.com/s-b17f1zdab8/images/stencil/1280x1280/products/227/586/111849_Founderie_AK47_inSitu__10117.1501636844.jpg?c=2&imbypass=on' },
  "sku02": { 
      "id": "sku02", 
      "name": "Cup", 
      "price": 80, 
      "desc": "This is a cup.",
      'src': 'https://www.ikea.com/us/en/images/products/vardagen-coffee-cup-and-saucer__0711051_PE727947_S5.JPG' },
  "sku03": { 
      "id": "sku03", 
      "name": "Notebook", 
      "price": 25, 
      "desc": "This is a notebook.",
      'src': 'https://www.staples-3p.com/s7/is/image/Staples/sp38165458_sc7?wid=512&hei=512' }
}

DATABASE = '/path/to/database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def hello():
    conn = get_db()
    return render_template('shop.html', title = title, products = products)
    
@app.route('/product/<id>')
def product(id):
    pd = products[id]
    return render_template("product.html", product=pd)

@app.route("/cart")
def cart():
  return render_template("cart.html")

@app.route("/add-cart/<id>")
def addCart(id):
  print(id)
  return redirect('/cart')

@app.route('/add-product', methods = ['GET', 'POST'])
def addProduct():
  if request.method == 'POST':
    name = request.form.get('name')
    price = request.form.get('price')
    products['sku' + str(len(products))] = { 
      'name': name, 
      'price': price
    }
    return redirect('/')

  return render_template('add-product.html')