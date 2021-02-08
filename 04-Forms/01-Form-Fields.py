from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,RadioField, SelectField, TextField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired, data_required

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField("Has this dog been neatured?")
    mood = RadioField('Please choose your mood:', choices=[("mood_one", 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u'Pick your favorite food:', choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')