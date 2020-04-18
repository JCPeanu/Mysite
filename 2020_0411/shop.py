from flask import Flask, render_template
from flask import request, redirect
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

cart = [
  {"id": "sku01", "num": 5 },
  {"id": "sku02", "num": 3},
  {"id": "sku03", "num": 10}
]

@app.route("/")
def hello():
    title = 'Welcome to MyShop'
    subtitle = 'Made in 15 minutes'
    total = 0
    for item in cart:
        prod = products.get(item['id'])
        total += prod['price'] * item['num']
        #subtotal = 0
        subtotal = prod['price'] * item['num']
        item['subtotal'] = subtotal

    return render_template('shop.html', title = title, 
    subtitle = subtitle, products = products, cart = cart, total = total, subtotal = subtotal)

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)

@app.route('/product/<id>/edit', methods = ['GET', 'POST'])
def edit(id):
    prod = products[id]
    errors = {}
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            errors['name'] = 'Name should not be empty!'
        price = request.form['price']
        if not price:
            errors['price'] = 'Price should not be empty!'
        desc = request.form['desc']
        if not desc:
            errors['desc'] = 'Description should not be empty!'
        src = request.form['image']
        if not src:
            errors['src'] = 'Image should not be empty!'
        if len(errors) == 0:
            prod['name'] = name
            prod['price'] = int(request.form['price'])
            prod['desc'] = request.form['desc']
            prod['src'] = request.form['image']
            return redirect('/product/' + id)

    return render_template('product-edit.html', product=prod, errors = errors)
@app.route('/cart/edit', methods = ['GET', 'POST'])
def editcart():
    if request.method == "POST":
        pen = int(request.form['pen'])
        cart[0]['num'] = pen
        cup = int(request.form['cup'])
        cart[1]['num'] = cup
        notebook = int(request.form['notebook'])
        cart[2]['num'] = notebook
        return redirect('/')
    return render_template('cart-edit.html', cart = cart, product = {}, errors = {})