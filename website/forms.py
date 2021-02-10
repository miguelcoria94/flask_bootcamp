from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField("Add Pup")


class DelForm(FlaskForm):
    id = IntegerField("Id Number of the Puppy to Remove: ")
    sumbit = SubmitField("Remove Pup")