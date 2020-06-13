import os
from flask import Flask, session, render_template, request, redirect, g
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER, 'static', 'upload')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.secret_key = b'should be a secret'

users_db = {
    'Joshua': {
        'username': 'Joshua',
        'password': 'curryisgood',
        'name': 'Joshua Chen',
        'email': 'JChen500@gmail.com'
    },
    'Dwight': {
        'username': 'Dwight',
        'password': 'Trashshshshsh',
        'name': 'Dwight Tils',
        'email': 'Dwight_Africanquality@gmail.com'
    }
}

items_db = [{
    'item_id': 0,
    'username': 'Joshua',
    'name': 'Pen',
    'price': 120,
    'desc': 'This is a pen that you could never get.',
    'filename': 'pen.jpg'
    },
    {
    'item_id': 1,
    'username': 'Dwight',
    'name': 'Finger_Skateboard',
    'price': 300,
    'desc': 'Dwight spent $NTD 300 on this trash.',
    'filename': 'Dwight.jpg'
    }
]

def get_user():
  user_id = session.get('user_id')
  if user_id:
    g.user = users_db.get(user_id)
  else:
    g.user = { 'username': None, 'name': 'Guest' }

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    get_user()
    return render_template('home.html', user = g.user, items = items_db, user_map = users_db)

@app.route('/login', methods = ['GET', 'Post'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return 'invalid input'
        
        user = users_db.get(username)
        if not user:
            return 'Wrong password or wrong username.'

        if user.get('password') != password:
            return 'Wrong password or wrong username.'
        
        session['user_id'] = username
        return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['user_id'] = None
    return redirect('/')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        conpassword = request.form.get('conpassword')

        if not username or not password or not email or not conpassword or not name:
            return 'invalid input'
        user = users_db.get(username)
        if user:
            return 'user exists'
        if password != conpassword:
            return render_template('signup.html', password_error = True)
        users_db[username] = {
            'username': username,
            'name': name,
            'email': email,
            'password': password
        }
        session['user_id'] = username
        return redirect('/')
    return render_template('signup.html')

@app.route('/profile')
def profile():
    get_user()
    return render_template('profile.html', user = g.user)

@app.route('/uploadfiles', methods = ['GET', 'POST'])
def uploadfiles():
    get_user()
    if not g.user or not g.user['username']:
        return redirect('/')

    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        desc = request.form.get('desc')
        if not name or not price or not desc:
            return 'invalid inputs'
        filename = None
        if 'picture' in request.files:
            pic = request.files['picture']
            if pic and allowed_file(pic.filename):
                filename = secure_filename(pic.filename)
                pic.save(os.path.join(UPLOAD_FOLDER, filename))
        item_id = len(items_db)
        items_db.append({
            'item_id': item_id,
            'username': g.user['username'],
            'name': name,
            'price': float(price),
            'desc': desc,
            'filename': filename
        })
        return redirect('/')
    return render_template('uploadfiles.html', user = g.user)

@app.route('/item/<item_id>')
def itemview(item_id):
    get_user()
    item = None
    for it in items_db:
        if str(it['item_id']) == item_id:
            item = it
            break
    return render_template("item.html", item = item, user = g.user)

@app.route('/items')
def viewitems():
    get_user()
    '''items = [it for it in items_db if it['username'] == g.user['username']]'''
    return render_template('items.html', user = g.user, items = items_db, user_map = users_db)

@app.route('/cart')
def cartview():
    get_user()
    total = 0
    item = None
    for id, num in mycart.items():
        it = items.id
        total += it['price'] * num
    return render_template('cart.html', mycart = mycart, total = total, item = item, user = g.user)

@app.route("/add-cart/<id>")
def addCart(id):
    mycart[id] = mycart.get(id, 0) + 1
    return redirect("/cart")


