from django import forms
from django.contrib.auth.models import User
from seller.models import UserProfile,Products
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]




class LoginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(max_length=200)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=["address","phone","profile_pic"]


class ProductForm(forms.ModelForm):
    class Meta:
        model=Products
        fields=["name","description","owner","condition","category","location","price","status","photo"]
