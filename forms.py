from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, EqualTo
from wtforms import TextField, PasswordField

class SignUpForm(FlaskForm):
	email = TextField('Email Address', validators=[InputRequired()])