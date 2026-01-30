from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators


class UserForms(Form):
    matricula = IntegerField('Matricula',
        [
            validators.DataRequired("Este campo es requerido"),
            validators.NumberRange(min=2,max=100,message="Ingresa un valor valido")
        ]
    )
    nombre = StringField('Nombre',
        [
            validators.DataRequired("Este campo es requerido"),
            validators.length(min=4,max=10,message="Ingresa un valor valido")
        ]
    )
    apaterno = StringField('A. Parterno',
        [
            validators.DataRequired("Este campo es requerido")
        ]
    )
    amaterno = StringField('A. Materno',
        [
            validators.DataRequired("Este campo es requerido")
        ]
    )
    email = EmailField('Email',
        [
            validators.Email("Ingrese un correo valido")
        ]
    )