
# README - Pokémon Analysis Project

## Overview

The Pokémon Analysis Project is a web application built using Django to analyze Pokémon data from the [PokeAPI](https://pokeapi.co/). The project allows users to explore various views of Pokémon data, including the first 50 Pokémon, Pokémon with specific characteristics, and more.

## Features

- **First 50 Pokémon:** View detailed information about the first 50 Pokémon, including their ID, name, types, height, and weight.

- **Weight Range Pokémon:** Explore Pokémon with weights between 30 and 80.

- **Grass Type Pokémon:** Discover all Pokémon of the Grass type.

- **Flying Type Pokémon with Height > 10:** Find Flying-type Pokémon with a height greater than 10.

- **Inverted Pokémon Names:** View Pokémon names in reverse order.

## Getting Started

To run the Pokémon Analysis Project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pokemon-analysis.git
cd pokemon-analysis
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **Windows:**
  ```bash
  .\venv\Scripts\activate
  ```

- **Unix or MacOS:**
  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to access the application.

## Project Structure

- **pokedex/:** Django project directory.
  - **pokemon_analysis/:** Django app directory.
    - **templates/:** HTML templates.

## Notes

- The project utilizes Django for server-side rendering.
- The `requirements.txt` file contains the necessary Python packages.
- Make sure to activate the virtual environment before running the project.
