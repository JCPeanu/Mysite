from flask import Flask, render_template
app = Flask(__name__)

products = {
  "sku01": { "id": "sku01", "name": "Pen", "price": 15, 'src': 'https://cdn11.bigcommerce.com/s-b17f1zdab8/images/stencil/1280x1280/products/227/586/111849_Founderie_AK47_inSitu__10117.1501636844.jpg?c=2&imbypass=on' },
  "sku02": { "id": "sku02", "name": "Cup", "price": 80, 'src': 'https://www.ikea.com/us/en/images/products/vardagen-coffee-cup-and-saucer__0711051_PE727947_S5.JPG' },
  "sku03": { "id": "sku03", "name": "Notebook", "price": 25, 'src': 'https://www.staples-3p.com/s7/is/image/Staples/sp38165458_sc7?wid=512&hei=512' }
}

cart = [
  {"id": "sku01", "num": 5 },
  {"id": "sku03", "num": 3}
]

@app.route("/")
def hello():
    title = 'Welcome to MyShop'
    subtitle = 'Made in 15 minutes'
    total = 0
    for item in cart:
        prod = products.get(item['id'])
        total += prod['price'] * item['num']
    subtotal = 0
    subtotal += prod['price'] * item['num']

    return render_template('shop.html', title = title, 
    subtitle = subtitle, products = products, cart = cart, total = total, subtotal = subtotal)

@app.route("/product/<id>")
def product(id):
    p = products[id]
    return render_template("product.html", product=p)