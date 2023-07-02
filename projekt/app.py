import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = 'tajny_klucz_sessji'

# Połączenie z bazą danych
connection = mysql.connector.connect(
    host='mysql.agh.edu.pl',
    port=3306,
    user='iwozniak',
    password='yNUgtbVPUK9gefHt',
    database='iwozniak'
)


@app.route('/')
def logowanie():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('home'))

    error = False
    success = request.args.get('success')  # Sprawdzenie czy jest przekazany argument success
    return render_template("logowanie.html", error=error, success=success)


@app.route('/logowanie', methods=['POST'])
def zaloguj():
    username = request.form["username"]
    password = request.form["password"]

    # Sprawdzanie poprawności danych logowania
    cursor = connection.cursor()
    sql = "SELECT * FROM Użytkownicy WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    user = cursor.fetchone()
    cursor.close()

    if user:
        # Użytkownik poprawnie zalogowany
        # Zapisanie informacji o zalogowaniu do sesji
        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('home'))
    else:
        # Błąd logowania
        error = True
        return render_template("logowanie.html", error=error)


@app.route('/wyloguj')
def wyloguj():
    # Usunięcie informacji o zalogowaniu z sesji
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('logowanie'))


@app.route('/home')
def home():
    if 'logged_in' in session and session['logged_in']:
        return render_template('start.html')
    else:
        return redirect(url_for('logowanie'))


@app.route('/dodaj', methods=['GET', 'POST'])
def dodaj_przestepce():
    if 'logged_in' in session and session['logged_in']:
        if request.method == 'POST':
            imie = request.form["imie"]
            nazwisko = request.form["nazwisko"]
            wiek = request.form["wiek"]
            miejsce_zamieszkania = request.form["miejsce_zamieszkania"]
            data_przestepstwa = request.form["data_przestepstwa"]
            rodzaj = request.form["rodzaj"]
            miejsce = request.form["miejsce"]
            pora = request.form["pora"]
            bron = request.form["bron"]

            # Pobierz najwyższe istniejące ID przestępców
            cursor = connection.cursor()
            sql = "SELECT MAX(id) FROM Przestępstwa"
            cursor.execute(sql)
            max_id = cursor.fetchone()[0]
            cursor.close()

            # Przypisz kolejne ID na podstawie najwyższego istniejącego ID
            if max_id is None:
                przestepca_id = 1
            else:
                przestepca_id = max_id + 1

            # Dodaj dane przestępcy do tabeli Przestępstwa z nowym ID
            cursor = connection.cursor()
            sql = "INSERT INTO Przestępstwa (id, imie, nazwisko, wiek, miejsce_zamieszkania, data_przestepstwa, rodzaj, miejsce, pora, bron) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (przestepca_id, imie, nazwisko, wiek, miejsce_zamieszkania, data_przestepstwa, rodzaj, miejsce, pora, bron)
            cursor.execute(sql, val)
            connection.commit()

            cursor.close()

            return "Dziękujemy za przesłanie formularza! Przestępstwo zostało dodane do bazy danych."

        return render_template("dodaj.html")
    else:
        return redirect(url_for('logowanie'))



@app.route('/szukaj', methods=['GET', 'POST'])
def szukaj_przestepstwa():
    if 'logged_in' in session and session['logged_in']:
        if request.method == 'POST':
            rodzaj = request.form["rodzaj"]
            miejsce = request.form["miejsce"]
            pora = request.form["pora"]
            bron = request.form["bron"]
            #wagi do sortowania
            rodzaj_weight = 0.4
            miejsce_weight = 0.3
            pora_weight = 0.1
            bron_weight = 0.2
            # Wyszukiwanie pasujących przestępców
            cursor = connection.cursor()
            #ustawienie wartości jako relevance do sort by relevance
            sql = "SELECT Przestępstwa.imie, Przestępstwa.nazwisko, Przestępstwa.data_przestepstwa, " \
                  "(%s * (Przestępstwa.rodzaj = %s)) + " \
                  "(%s * (Przestępstwa.miejsce = %s)) + " \
                  "(%s * (Przestępstwa.pora = %s)) + " \
                  "(%s * (Przestępstwa.bron = %s)) AS relevance " \
                  "FROM Przestępstwa " \
                  "WHERE (Przestępstwa.rodzaj = %s OR Przestępstwa.miejsce = %s OR Przestępstwa.pora = %s OR Przestępstwa.bron = %s) " \
                  "ORDER BY relevance DESC"

            
            val = (rodzaj_weight, rodzaj,
                   miejsce_weight, miejsce,
                   pora_weight, pora,
                   bron_weight, bron,
                   rodzaj, miejsce, pora, bron)

            cursor.execute(sql, val)
            przestepcy = cursor.fetchall()
            cursor.close()
            return render_template("wyniki.html", przestepcy=przestepcy)

        return render_template("szukaj.html")
    else:
        return redirect(url_for('logowanie'))

#sortowanie w wyniki.html    
@app.route('/sorting', methods=['GET', 'POST'])
def sorting():
    if 'logged_in' in session and session['logged_in']:
        if request.method == 'POST':
            sort = request.form["sort"]
            cursor = connection.cursor()
            sql = "SELECT Przestępstwa.imie, Przestępstwa.nazwisko, Przestępstwa.data_przestepstwa " \
                  "FROM Przestępstwa"
        #sortowanie wg kryteriów
            if sort == 'oldest':
                sql += " ORDER BY Przestępstwa.data_przestepstwa ASC"
            elif sort == 'newest':
                sql += " ORDER BY Przestępstwa.data_przestepstwa DESC"
            elif sort == 'alphabetical':
                sql += " ORDER BY Przestępstwa.nazwisko ASC"

            cursor.execute(sql)
            przestepcy = cursor.fetchall()
            cursor.close()
            return render_template("wyniki.html", przestepcy=przestepcy)
    return redirect(url_for('logowanie'))



@app.route('/rejestracja', methods=['GET', 'POST'])
def rejestracja():
    if 'logged_in' in session and session['logged_in']:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        # Sprawdzanie istnienia użytkownika w bazie danych
        cursor = connection.cursor()
        sql = "SELECT * FROM Użytkownicy WHERE username = %s"
        val = (username,)
        cursor.execute(sql, val)
        user = cursor.fetchone()

        if user:
            # Użytkownik o podanej nazwie już istnieje
            error = True
            return render_template("rejestracja.html", error=error)

        # Dodawanie nowego użytkownika do bazy danych
        sql = "INSERT INTO Użytkownicy (username, password) VALUES (%s, %s)"
        val = (username, password)
        cursor.execute(sql, val)
        connection.commit()
        cursor.close()

        # Przekierowanie do strony logowania po pomyślnej rejestracji
        return redirect(url_for('logowanie', success=True))

    return render_template("rejestracja.html")



def aktualizuj_id():
    cursor = connection.cursor()

    # Pobierz wszystkie przestępstwa posortowane według ID
    sql = "SELECT id FROM Przestępstwa ORDER BY id"
    cursor.execute(sql)
    przestepstwa = cursor.fetchall()

    # Zaktualizuj ID przestępców w kolejności rosnącej
    for i, przestepstwo in enumerate(przestepstwa, start=1):
        sql = "UPDATE Przestępstwa SET id = %s WHERE id = %s"
        val = (i, przestepstwo[0])
        cursor.execute(sql, val)

    connection.commit()
    cursor.close()






@app.route('/usun_przestepce', methods=['POST'])
def usun_przestepce():
    if 'logged_in' in session and session['logged_in']:
        if request.method == 'POST':
            przestepca_id = request.form["id"]

            # Usunięcie wiersza na podstawie przekazanego ID
            cursor = connection.cursor()
            sql = "DELETE FROM Przestępstwa WHERE id = %s"
            val = (przestepca_id,)
            cursor.execute(sql, val)
            connection.commit()
            cursor.close()

            # Aktualizuj ID przestępców
            aktualizuj_id()

            # Przekierowanie na stronę edytuj.html
            return redirect(url_for('usun'))
    else:
        return redirect(url_for('logowanie'))


#tutaj przycisk juz w edycji ktory bedzie edytowal
@app.route('/usun', methods=['GET'])
def usun():
    if 'logged_in' in session and session['logged_in']:
        cursor = connection.cursor()
        sql = "SELECT id, imie, nazwisko FROM Przestępstwa"
        cursor.execute(sql)
        przestepcy = cursor.fetchall()
        cursor.close()

        return render_template('usun.html', przestepcy=przestepcy)
    else:
        return redirect(url_for('logowanie'))


if __name__ == '__main__':
    app.run()
