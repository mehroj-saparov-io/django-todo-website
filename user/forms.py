from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Registration uchun form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # agar email kiritishni xohlasangiz

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Login uchun form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
