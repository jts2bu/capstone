from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()] )
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Sign In')

class EntryForm(FlaskForm):
    universityID = StringField('University ID')
    submit = SubmitField('Go')

class AlternativeEntryForm(FlaskForm):
    computingID = StringField('Computing ID')
    birthday = DateField('Birthday')
    submit = SubmitField('Go')