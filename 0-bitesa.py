#!/usr/bin/python3
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bite sa recipe finder'


class NameForm(FlaskForm):
    name = StringField('Add Ingredients', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return render_template('results.html', name=session.get('name'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
