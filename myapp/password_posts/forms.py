from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PasswordPostForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    user_name = StringField('Username', validators=[DataRequired()])
    pword = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')