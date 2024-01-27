from . import views
from django.urls import path
from django.shortcuts import redirect

urlpatterns = [
    path('', views.list_first_50_pokemon, name='list_first_50'), 
    path('weight_range/', views.pokemon_weight_range, name='pokemon_weight_range'), 
    path('grass_type/', views.grass_type_pokemon, name='grass_type_pokemon'),
    path('flying_tall/', views.flying_type_tall_pokemon, name='flying_type_tall_pokemon'),  
    path('inverted_names/', views.inverted_names, name='inverted_names'),  
]