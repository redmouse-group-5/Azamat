from django import forms
from Student.models import StudentInfo


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    lat = forms.CharField(max_length=50, widget=forms.HiddenInput)
    lng = forms.CharField(max_length=50)

class LoginForm(forms.Form):
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

