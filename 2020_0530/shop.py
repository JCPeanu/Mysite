from flask import Flask, session, render_template, request, redirect, g

app = Flask(__name__)

app.secret_key = b'should be a secret'

users_db = {
    'Joshua': {
        'username': 'Joshua',
        'password': 'curryisgood',
        'name': 'Joshua Chen',
        'email': 'JChen500@gmail.com'
    }
}

def get_user():
  user_id = session.get('user_id')
  if user_id:
    g.user = users_db.get(user_id)
  else:
    g.user = { 'username': None, 'name': 'Guest' }


@app.route('/')
def index():
    get_user()
    return render_template('home.html', user = g.user)

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


