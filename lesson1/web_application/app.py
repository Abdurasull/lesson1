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
    return render_template("talaba.html")

# o`qituvchilar ruyxatini ko`rish uchun
@app.route("/teacher")
def teachers():
    return render_template("teacher.html")

if __name__ == '__main__':
    app.run(debug=True)