import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def formularz():
    if request.method == "POST":
        rodzaj = request.form["rodzaj"]
        miejsce = request.form["miejsce"]
        pora = request.form["pora"]
        bron = request.form["bron"]
        return f"Dziękujemy za przesłanie formularza! Wybrany rodzaj: {rodzaj}, miejsce: {miejsce}, pora: {pora}, broń: {bron}"
    return render_template("szablon.html")

@app.route('/tabela', methods=['POST'])
def x():
    return x

if __name__ == '__main__':
    app.run()

