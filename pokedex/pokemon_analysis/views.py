
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import requests
from django.shortcuts import render


CACHE_TIMEOUT = 3600

def get_results_data(url):
    cached_data = cache.get(url)
    if cached_data:
        return cached_data

    # if it`s not in cache - calls API and sets cache
    response = requests.get(url)
    data = response.json()
    cache.set(url, data, CACHE_TIMEOUT)
    return data

@cache_page(CACHE_TIMEOUT)
def list_first_50_pokemon(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    data = get_results_data(url)

    # Process the data to extract required information
    pokemon_list = []
    for result in data.get('results', []):
        pokemon_data = get_results_data(result['url'])
        pokemon_list.append({
            'id': pokemon_data['id'],
            'name': pokemon_data['name'],
             'types': [t['type']['name'] for t in pokemon_data['types']],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight']
        })

    return render(request, 'pokemon_analysis/pokemon_list.html', {'pokemon_list': pokemon_list})

@cache_page(CACHE_TIMEOUT)
def pokemon_weight_range(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    data = get_results_data(url)

    filtered_pokemon = []
    for result in data.get('results', []):
        pokemon_data = get_results_data(result['url'])
        weight = pokemon_data['weight']
        if 30 < weight < 80:
            filtered_pokemon.append({
                'name': pokemon_data['name'],
                'weight': weight
            })

    return render(request, 'pokemon_analysis/pokemon_weight_range.html', {'filtered_pokemon': filtered_pokemon})

@cache_page(CACHE_TIMEOUT)
def grass_type_pokemon(request):
    url = "https://pokeapi.co/api/v2/type/grass"
    data = get_results_data(url)

    grass_pokemon = []
    for pokemon in data.get('pokemon', []):
        pokemon_data = get_results_data(pokemon['pokemon']['url'])
        grass_pokemon.append({
            'name': pokemon_data['name']
        })

    return render(request, 'pokemon_analysis/grass_type_pokemon.html', {'grass_pokemon': grass_pokemon})

@cache_page(CACHE_TIMEOUT)
def flying_type_tall_pokemon(request):
    url = "https://pokeapi.co/api/v2/type/flying"
    data = get_results_data(url)

    flying_tall_pokemon = []
    for pokemon in data.get('pokemon', []):
        pokemon_data = get_results_data(pokemon['pokemon']['url'])
        if pokemon_data['height'] > 10:
            flying_tall_pokemon.append({
                'name': pokemon_data['name'],
                'height': pokemon_data['height']
            })

    return render(request, 'pokemon_analysis/flying_type_tall_pokemon.html', {'flying_tall_pokemon': flying_tall_pokemon})

@cache_page(CACHE_TIMEOUT)
def inverted_names(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    data = get_results_data(url)

    inverted_pokemon_names = []
    for result in data.get('results', []):
        name = result['name']
        inverted_name = name[::-1]
        inverted_pokemon_names.append({
            'original_name': name,
            'inverted_name': inverted_name
        })

    return render(request, 'pokemon_analysis/inverted_names.html', {'inverted_pokemon_names': inverted_pokemon_names})

