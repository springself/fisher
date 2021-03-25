from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    # DataRequired()可以防止用户只传一个空格这种情况
    q = StringField(validators=[Length(min=1, max=30), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
