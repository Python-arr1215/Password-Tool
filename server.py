from flask import Flask, render_template, request
import checkmypass
import create_password

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/check.html", methods=["GET", "POST"])
def checker_page():
    result = None
    if request.method == "POST":
        # HTMLから受け取る
        password = request.form["password"]
        # checker.py の main() 実行
        result = checkmypass.main(password)
    # HTMLへ返す
    return render_template(
        "check.html",
        result=result
    )


# Password Create
@app.route("/create.html", methods=["GET", "POST"])
def create_page():

    password = None

    if request.method == "POST":

        types = request.form.getlist("types")

        length = int(request.form["length"])

        password = create_password.main(
            types,
            length
        )

    return render_template(
        "create.html",
        password=password
    )

