from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'klucz'

# połączenie z bazą danych
db_connection = mysql.connector.connect(
    host='mysql.agh.edu.pl',
    port=3306,
    user='sylwestr',
    password='eFfkCL7mfnnV4BYz',
    database='sylwestr'
)

class MyForm(FlaskForm):
    oswietlenie=SelectField('Oświetlenie', choices=[('naturalne'), ('sztuczne'), ('dobre'), ('złe')])
    pogoda=SelectField('Warunki pogodowe', choices=[('słonecznie'), ('zachmurzenie'), ('deszcz'), ('śnieg'),('mgła')])
    pora = SelectField('Pora dnia', choices=[('dzienna'), ('nocna'), ('zmierzch'), ('świt')])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        oswietlenie = form.oswietlenie.data
        pogoda = form.pogoda.data
        pora = form.pora.data

        cursor = db_connection.cursor()
        query = "INSERT INTO dane (oswietlenie, pogoda, pora) VALUES (%s, %s, %s)"
        values = (oswietlenie, pogoda, pora)
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()

        print(f'Oświetlenie: {oswietlenie}')
        print(f'Pogoda: {pogoda}')
        print(f'Pora dnia: {pora}')

        return 'Dane zostały przesłane poprawnie!'
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
