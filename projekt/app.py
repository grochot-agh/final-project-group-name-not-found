import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Połączenie z bazą danych
connection = mysql.connector.connect(
    host='mysql.agh.edu.pl',
    port=3306,
    user='iwozniak',
    password='yNUgtbVPUK9gefHt',
    database='iwozniak'
)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        rodzaj = request.form["rodzaj"]
        miejsce = request.form["miejsce"]
        pora = request.form["pora"]
        bron = request.form["bron"]

        # Dodanie danych do tabeli Przestępstwa
        cursor = connection.cursor()
        sql = "INSERT INTO Przestępstwa (rodzaj, miejsce, pora, bron) VALUES (%s, %s, %s, %s)"
        val = (rodzaj, miejsce, pora, bron)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()

        return "Dziękujemy za przesłanie formularza! Przestępstwo zostało dodane do bazy danych."

    return render_template("index.html")

@app.route('/szukaj', methods=['POST'])
def szukaj():
    rodzaj = request.form["rodzaj"]
    miejsce = request.form["miejsce"]
    pora = request.form["pora"]
    bron = request.form["bron"]

    # Wyszukiwanie pasujących przestępców
    cursor = connection.cursor()
    sql = "SELECT imie, nazwisko FROM Przestępstwa WHERE id IN (SELECT id FROM Przestępstwa WHERE rodzaj = %s AND miejsce = %s AND pora = %s AND bron = %s)"
    val = (rodzaj, miejsce, pora, bron)
    cursor.execute(sql, val)
    przestepcy = cursor.fetchall()
    cursor.close()

    return render_template("wyniki.html", przestepcy=przestepcy)

if __name__ == '__main__':
    app.run()
