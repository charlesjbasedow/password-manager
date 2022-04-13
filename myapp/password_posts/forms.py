from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PasswordPostForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    user_name = TextAreaField('Username', validators=[DataRequired()])
    pword = TextAreaField('Password', validators=[DataRequired()])
    submit = SubmitField('Add')