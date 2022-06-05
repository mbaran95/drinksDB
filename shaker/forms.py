from django import forms
from .models import Drinks, Ingredients, alcoholType


class DrinksForm(forms.Form):
    name_drink = forms.CharField(label='Name drink')
    desc_drink = forms.CharField(label='Short desc')
    alcohol_type = forms.ChoiceField(choices=alcoholType)
    pub_date = forms.DateTimeField(label='Date public', widget=forms.SelectDateWidget)


class IngredientForm(forms.Form):
    name_ingredient = forms.CharField(label='Name Ingredient')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_conf = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")