from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, IntegerField,
                            DateField, RadioField, SelectField,
                            SubmitField)
from wtforms.validators import DataRequired, equal_to, length
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed


class RegisterForm(FlaskForm):
    image = FileField(validators=[
        FileRequired(message="უეჭველი ატვირთე ფოტო"),
        FileSize(1024 * 1024 * 3, message="File Size restricted"),
        FileAllowed(["png", "jpg", "jpeg"])
    ])
    username = StringField("Enter Username", validators=[
        DataRequired()
    ])
    password = PasswordField("Enter Password", validators=[
        DataRequired(),
        length(min=6, max=24),
    ])
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(),
        equal_to("password", message="Passwords Do Not Match")
    ])
    mobile = IntegerField(validators=[
        DataRequired()
    ])
    birthdate = DateField()
    gender = RadioField(choices=["Male", "Female", "I am Groot"])
    country = SelectField(choices=["Choose Country", "Georgia", "USA", "Japan", "Turkey"])

    register = SubmitField("Register")

