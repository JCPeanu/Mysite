from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    title = 'My Flask Website'
    subtitle = 'Made in 3 minutes'
    return render_template('hello.html', title = title, subtitle = subtitle)