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
mycart = {

}
@app.route("/")
def myshop():
  return render_template("shop.html", products = products)

@app.route("/product/<id>")
def productView(id):
    pd = products[id]
    return render_template("product.html", product = pd)

@app.route("/cart")
def cartView():
    total = 0
    for id, num in mycart.items():
        pd = products[id]
        total += pd['price'] * num
    return render_template("cart.html", mycart=mycart, products = products, total = total)

@app.route("/add-cart/<id>")
def addCart(id):
    mycart[id] = mycart.get(id, 0) + 1
    return redirect("/cart")

@app.route("/remove-cart/<id>")
def removeCart(id):
    del mycart[id]
    return redirect("/cart")

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