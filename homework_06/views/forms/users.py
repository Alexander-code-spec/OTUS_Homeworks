from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField("User name", validators=[DataRequired()])
    email = StringField("User email", validators=[DataRequired()])
    is_new = BooleanField("is new", default=False)
