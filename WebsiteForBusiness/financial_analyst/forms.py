from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
        Форма для входа пользователя:
        username - поле ввода имени пользователя (задана максимальная длина)
        password - поле ввода пароля с помощью виджета PasswordInput

    """
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(label='Введите пароль:', widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    """
        Форма для регистрации пользователя:
        - наследуется от встроенной формы UserCreationForm
        - добавляет дополнительное поле email к username и password
        - содержит класс
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
            Класс Meta - внутренний класс:
            model - модель пользователя User по умолчанию
            fields - поля, которые нужно включить в форму.

        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
