from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/games")
def menu():
    return render_template("games.html")

@app.route("/cards")
def cards():
    return render_template("cards.html")

if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")