from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.html5 import TelField, EmailField
from wtforms.validators import DataRequired, Email


class TripSignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[Email(), DataRequired()])
    phone_number = TelField('Phone Number', validators=[DataRequired()])
    can_drive = BooleanField('Can Drive')
    submit = SubmitField('Submit')