from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class UserSignUpForm(FlaskForm):
    first = StringField("First Name", validators = [DataRequired()])
    last = StringField("Last Name", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    submit_button = SubmitField()
