from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[Length(min=2, max=32), DataRequired()]
    )
    submit = SubmitField('Greet')
