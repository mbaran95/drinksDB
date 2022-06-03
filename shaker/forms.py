from django import forms
from .models import Drinks, Ingredients, alcoholType


class DrinksForm(forms.Form):
    name_drink = forms.CharField(label='Name drink')
    desc_drink = forms.CharField(label='Short desc')
    alcohol_type = forms.ChoiceField(choices=alcoholType)
    pub_date = forms.DateTimeField(label='Date public', widget=forms.SelectDateWidget)


class IngredientForm(forms.Form):
    name_ingredient = forms.CharField(label='Name Ingredient')
