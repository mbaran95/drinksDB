from django.urls import path
from . import views


app_name = 'shaker'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DrinksView.as_view(), name='drinks'),
    path('add/', views.AddDrinkView.as_view(), name='add'),
    path('list_drinks/', views.ListDrinksView.as_view(), name='list_drinks'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('search/', views.SearchView.as_view(), name='search'),
]