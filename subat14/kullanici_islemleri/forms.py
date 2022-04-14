from django import forms
from django.forms import widgets
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label= "Kullanici Adi", widget=forms.TextInput(attrs={'placeholder': 'Kullamici Adi', 'class': 'form-control'}))
    password = forms.CharField(label= "Parola", widget=forms.PasswordInput(attrs={'placeholder': 'Parola', 'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, label = "Kullanici Adi")
    email = forms.EmailField(max_length = 100, label = "Email")
    password = forms.CharField(max_length = 20, label = "Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length = 20, label = "Parola Dogrula", widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        if User(username = username):
            raise forms.ValidationError("Kullanıcı adı kullanılmakta")
        values = {
            "username" : username,
            "password" : password,
            "email" : email
        }
        return values