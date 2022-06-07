from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic, View

from .forms import DrinksForm, IngredientForm, LoginForm, RegistrationForm, SearchForm
from .models import Drinks, Ingredients


class IndexView(View):

    def get(self, request):
        drinks_list = Drinks.objects.all()
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


class AddDrinkView(LoginRequiredMixin, View):

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
            )

        else:
            messages.error(request, 'Ops, we have a problem.')

        return HttpResponseRedirect(reverse('shaker:index'))


class DrinksView(View):

    def get(self, request, pk):
        form_ingredient = IngredientForm
        ingredient_list = Ingredients.objects.filter(drinks=pk)
        try:
            drinks = Drinks.objects.get(pk=pk)
        except Drinks.DoesNotExist:
            raise Http404("Drink does not exist")
        context = {
            'drinks': drinks,
            'form_ingredient': form_ingredient,
            'ingredient_list': ingredient_list,
        }
        # print(ingredient_list)
        return render(request, 'shaker/drinks.html', context)

    def post(self, request, pk):
        drinks = get_object_or_404(Drinks, pk=pk)
        form_ingredient = IngredientForm(request.POST)
        if form_ingredient.is_valid():
            Ingredients.objects.create(
                drinks=drinks,
                name_ingredient=form_ingredient.cleaned_data["name_ingredient"]
            )
        return HttpResponseRedirect(reverse('shaker:drinks', args=(drinks.id,)))


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'shaker/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                url = request.GET.get('next')
                if url:
                    return redirect(url)
                return HttpResponseRedirect(reverse('shaker:index'))
            messages.error(request, 'Username or password invalid')
            return HttpResponseRedirect(reverse('shaker:login'))
        messages.error(request, 'Form was not valid')
        return HttpResponseRedirect(reverse('shaker:login'))


class LogoutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('shaker:login'))


class RegistrationView(View):

    def get(self, request):
        form = RegistrationForm()
        context = {
            "form": form
        }
        return render(request, 'shaker/registration.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] == form.cleaned_data["password_conf"]:
                try:
                    User.objects.get(username=form.cleaned_data["username"])
                    messages.error(request, "User already exists")
                    return HttpResponseRedirect(reverse("polls:registration"))
                except User.DoesNotExist:
                    user = User.objects.create_user(
                        username=form.cleaned_data["username"],
                        password=form.cleaned_data["password"],
                        email=form.cleaned_data["email"]
                    )
                    login(request, user)
                    return HttpResponseRedirect(reverse("shaker:index"))
            else:
                messages.error(request, "Passwords are wrong!")
                return HttpResponseRedirect(reverse("shaker:registration"))


class SearchView(View):

    def get(self, request):
        form = SearchForm()
        context = {
            'form': form
        }
        return render(request, 'shaker/search.html', context)

    def post(self, request):
        form = SearchForm(request.POST)
        results = None
        if form.is_valid():
            results = Drinks.objects.filter(
                name_drink__contains=form.cleaned_data['name_drink']
            )
        context = {
            'form': form,
            'results': results
        }
        return render(request, 'shaker/search.html', context)