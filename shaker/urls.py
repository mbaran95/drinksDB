from django.urls import path
from . import views


app_name = 'shaker'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DrinksView.as_view(), name='drinks'),
    path('add/', views.AddDrinkView.as_view(), name='add'),
    path('list_drinks/', views.ListDrinksView.as_view(), name='list_drinks'),

]