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
    pora = SelectField('Pora dnia', choices=[('dzienna'), ('nocna'), ('zmierzch'), ('świt')])
    rodzaj=SelectField('Rodzaj przestępstwa', choices=[('Kradzież'), ('Napad'), ('Zabójstwo'), ('Przemoc Fizyczna')])
    miejsce=SelectField('Miejsce popełnienia przestępstwa', choices=[('na ulicy'), ('dom/mieszkanie'), ('miejsce publiczne')])
    bron=SelectField('czy sprawca był uzbrojony',choices=[('tak'),('nie')])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        rodzaj = form.rodzaj.data
        miejsce = form.miejsce.data
        pora = form.pora.data
        bron=form.bron.data

        cursor = db_connection.cursor()
        query = "INSERT INTO dane (rodzaj, miejsce, pora,bron) VALUES (%s, %s, %s, %s)"
        values = (rodzaj, miejsce, pora, bron)
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()

        print(f'rodzaj: {rodzaj}')
        print(f'miejsce: {miejsce}')
        print(f'Pora dnia: {pora}')
        print(f'Uzbrojenie: {bron}')
        return 'Dane zostały przesłane poprawnie!'
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
