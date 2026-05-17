from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, IntegerField,
                            DateField, RadioField, SelectField,
                            SubmitField)
from wtforms.validators import DataRequired, equal_to, length
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed


class RegisterForm(FlaskForm):
    image = FileField(validators=[
        FileRequired(message="უეჭველი ატვირთე ფოტო"),
        FileSize(1024 * 1024 * 3, message="ფოტო უნდა იყოს ამა და ამ ზომის"),
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
        equal_to("password", message="პაროლები არ ემთხვევა")
    ])
    mobile = IntegerField(validators=[
        DataRequired()
    ])
    birthdate = DateField()
    gender = RadioField(choices=["Male", "Female", "I'm a mekanik"])
    country = SelectField(choices=["Choose Country", "Georgia", "USA", "Japan"])

    register = SubmitField("Register")

