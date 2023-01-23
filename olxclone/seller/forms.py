from django import forms
from django.contrib.auth.models import User
from seller.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]




class LoginForm(forms.Form):
    emailaddress=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)