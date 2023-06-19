from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'klucz'


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

        
        print(f'Oświetlenie: {oswietlenie}')
        print(f'Pogoda: {pogoda}')
        print(f'Pora dnia: {pora}')
       

        return 'Dane zostały przesłane poprawnie!'
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run()
