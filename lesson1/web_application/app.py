from pprint import pprint
import json
from flask import Flask, render_template, url_for


app = Flask(__name__)
# asosiy sahifani ishga tushurish uchun
@app.route("/", methods=["GET", 'POST'])
def home():
    return render_template("index.html")

# talabalarni qo`shishni amalga oshirish uchun`
@app.route("/addstudent")
def add_students():
    return render_template("addstudent.html")

# o`qituvchilarni qo`shish uchun
@app.route("/addteacher")
def add_teacher():
    return render_template("addteacher.html")

# talabalar to`yxatini ko`rish uchun
@app.route("/student")
def students():
    students = []
    with open("DB/students.json", "r", encoding="utf-8") as f:
        students = json.loads(f.read())
        
        return render_template("talaba.html", talabalar=students)
    

# o`qituvchilar ruyxatini ko`rish uchun
@app.route("/teacher")
def teachers():
    teachers = []
    with open("DB/teachers.json", "r", encoding="utf-8") as f:
        teachers = json.loads(f.read())
        
        return render_template("teacher.html", teachers=teachers)


if __name__ == '__main__':
    app.run(debug=True)