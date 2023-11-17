from flask_wtf import FlaskForm
from wtforms import StringField


class SearchForm(FlaskForm):
    search_term = StringField('Search')
    column = StringField('Column')
