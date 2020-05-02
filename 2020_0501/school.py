from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

students = {
    "sku01": {
        "name": "Joshua",
        "intro": "Hi, my name is Joshua, and I am a student in HIS.",
        "avatar": "/static/img/dwight.png" },
    "sku02": {
        "name": "Kristopher",
        "intro": "Hi, my name is Kristopher, and I am a student in HIS.",
        "avatar": "/static/img/image2.png" },
    "sku03": {
        "name": "Dwight",
        "intro": "Hi, my name is Dwight, and I am a student in HIS.",
        "avatar": "/static/img/image.png" },
    "sku04": {
        "name": "Max",
        "intro": "Hi, my name is Max, and I am a student in HIS.",
        "avatar": "/static/img/max.webp" },
    "sku05": {
        "name": "William",
        "intro": "Hi, my name is William, and I am a student in HIS.",
        "avatar": "/static/img/panda.png"
    }
}

@app.route('/')
def school():
    title = "School Website"
    return render_template("school.html", title = title, students = students)
@app.route('/student/<id>')
def student(id):
    student = students[id]
    return render_template("student.html", student = student)