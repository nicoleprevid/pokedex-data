from django.shortcuts import render
import requests

def get_pokemon_data(url):
    response = requests.get(url)
    return response.json()

def list_first_50_pokemon(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    data = get_pokemon_data(url)

    # Process the data to extract required information
    pokemon_list = []
    for result in data.get('results', []):
        pokemon_data = get_pokemon_data(result['url'])
        pokemon_list.append({
            'id': pokemon_data['id'],
            'name': pokemon_data['name'],
             'types': [t['type']['name'] for t in pokemon_data['types']],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight']
        })

    return render(request, 'pokemon_analysis/pokemon_list.html', {'pokemon_list': pokemon_list})

def pokemon_weight_range(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    data = get_pokemon_data(url)

    filtered_pokemon = []
    for result in data.get('results', []):
        pokemon_data = get_pokemon_data(result['url'])
        weight = pokemon_data['weight']
        if 30 < weight < 80:
            filtered_pokemon.append({
                'name': pokemon_data['name'],
                'weight': weight
            })

    return render(request, 'pokemon_analysis/pokemon_weight_range.html', {'filtered_pokemon': filtered_pokemon})

def grass_type_pokemon(request):
    url = "https://pokeapi.co/api/v2/type/grass"
    data = get_pokemon_data(url)

    grass_pokemon = []
    for pokemon in data.get('pokemon', []):
        pokemon_data = get_pokemon_data(pokemon['pokemon']['url'])
        grass_pokemon.append({
            'name': pokemon_data['name']
        })

    return render(request, 'pokemon_analysis/grass_type_pokemon.html', {'grass_pokemon': grass_pokemon})

def flying_type_tall_pokemon(request):
    url = "https://pokeapi.co/api/v2/type/flying"
    data = get_pokemon_data(url)

    flying_tall_pokemon = []
    for pokemon in data.get('pokemon', []):
        pokemon_data = get_pokemon_data(pokemon['pokemon']['url'])
        if pokemon_data['height'] > 10:
            flying_tall_pokemon.append({
                'name': pokemon_data['name'],
                'height': pokemon_data['height']
            })

    return render(request, 'pokemon_analysis/flying_type_tall_pokemon.html', {'flying_tall_pokemon': flying_tall_pokemon})

def inverted_names(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    data = get_pokemon_data(url)

    inverted_pokemon_names = []
    for result in data.get('results', []):
        name = result['name']
        inverted_name = name[::-1]
        inverted_pokemon_names.append({
            'original_name': name,
            'inverted_name': inverted_name
        })

    return render(request, 'pokemon_analysis/inverted_names.html', {'inverted_pokemon_names': inverted_pokemon_names})

# Add other views as per the requirements
