from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View

from .forms import DrinksForm, IngredientForm
from .models import Drinks, Ingredients


class IndexView(View):

    def get(self, request):
        drinks_list = Drinks.objects.order_by('-pub_date')[:10]
        context = {
            'drinks_list': drinks_list,
        }
        return render(request, 'shaker/index.html', context)


class ListDrinksView(View):

    def get(self, request):
        drinks_list = Drinks.objects.all()
        context = {
            'drinks_list': drinks_list,
        }
        return render(request, 'shaker/list_drinks.html', context)


class AddDrinkView(View):

    def get(self, request):
        form = DrinksForm()
        context = {
            'form': form
        }
        return render(request, 'shaker/add.html', context)

    def post(self, request):
        form = DrinksForm(request.POST)
        if form.is_valid():
            Drinks.objects.create(
                name_drink=form.cleaned_data['name_drink'],
                desc_drink=form.cleaned_data['desc_drink'],
                alcohol_type=form.cleaned_data['alcohol_type'],
                pub_date=form.cleaned_data['pub_date'],
            )

        else:
            messages.error(request, 'Ops, we have a problem.')

        return HttpResponseRedirect(reverse('shaker:add'))


class DrinksView(View):

    def get(self, request, pk):
        drinks = get_object_or_404(Drinks, pk=pk)
        ingredients = get_object_or_404(Ingredients, pk=pk)
        context = {
            'drinks': drinks,
            'ingredients': ingredients
        }
        return render(request, 'shaker/drinks.html', context)

    def post(self, request):
        form_ingredient = IngredientForm(request.POST)
        if form_ingredient.is_valid():

            Ingredients.objects.create(
                name=form_ingredient.cleaned_data['name'],
                drink=form_ingredient.cleaned_data['drink'],
            )
        else:
            messages.error(request, 'Ops, we have a problem.')
        return HttpResponseRedirect(reverse('shaker:index'))