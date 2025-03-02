import pytest
from fastapi.testclient import TestClient
from main import app
import time

client = TestClient(app)

def test_pokemon_endpoints():
    # Test POST (création d'un Pokémon)
    pokemon_data = {
        "nom": "TestPokemon",
        "type": "TestType",
        "image_url": "test_url",
        "hp": 100,
        "attack": 50,
        "defense": 50,
        "speed": 60,
        "special_attack": 70,
        "special_defense": 80
    }
    response = client.post("/pokemon", json=pokemon_data)
    assert response.status_code == 200, f"Erreur POST: Code de statut attendu 200, obtenu {response.status_code}"
    assert response.json()["nom"] == "TestPokemon", f"Erreur POST: Données incorrectes: {response.json()}"
    print("POST: Pokémon créé avec succès.")

    # Récupérer l'ID du Pokémon créé
    created_pokemon_id = response.json()["id"]

    time.sleep(0.2)

    # Test GET (lecture du Pokémon créé)
    response = client.get(f"/pokemon/{created_pokemon_id}")
    assert response.status_code == 200, f"Erreur GET: Code de statut attendu 200, obtenu {response.status_code}"
    assert response.json()["nom"] == "TestPokemon", f"Erreur GET: Nom du Pokémon incorrect: {response.json()['nom']}"
    print("GET: Pokémon récupéré avec succès.")

    time.sleep(0.2)

    # Test PUT (mise à jour du Pokémon)
    updated_pokemon_data = {
        "nom": "UpdatedPokemon",
        "type": "UpdatedType",
        "image_url": "updated_url",
        "hp": 110,
        "attack": 60,
        "defense": 60,
        "speed": 70,
        "special_attack": 80,
        "special_defense": 90
    }
    response = client.put(f"/pokemon/{created_pokemon_id}", json=updated_pokemon_data)
    assert response.status_code == 200, f"Erreur PUT: Code de statut attendu 200, obtenu {response.status_code}"
    assert response.json()["nom"] == "UpdatedPokemon", f"Erreur PUT: Données incorrectes: {response.json()}"
    print("PUT: Pokémon mis à jour avec succès.")

    time.sleep(0.2)

    # Test GET après la mise à jour
    response = client.get(f"/pokemon/{created_pokemon_id}")
    assert response.status_code == 200, f"Erreur GET (après PUT): Code de statut attendu 200, obtenu {response.status_code}"
    assert response.json()["nom"] == "UpdatedPokemon", f"Erreur GET (après PUT): Nom du Pokémon incorrect: {response.json()['nom']}"
    print("GET (après PUT): Pokémon récupéré avec succès après la mise à jour.")

    time.sleep(0.2)

    # Test DELETE (suppression du Pokémon)
    response = client.delete(f"/pokemon/{created_pokemon_id}")
    assert response.status_code == 200, f"Erreur DELETE: Code de statut attendu 200, obtenu {response.status_code}"
    assert response.json() == {"message": "Pokemon deleted successfully"}, f"Erreur DELETE: Message de succès incorrect: {response.json()}"
    print("DELETE: Pokémon supprimé avec succès.")

    time.sleep(0.2)

    # Test GET après la suppression (vérifie que le Pokémon n'existe plus)
    response = client.get(f"/pokemon/{created_pokemon_id}")
    assert response.status_code == 404, f"Erreur GET (après DELETE): Code de statut attendu 404, obtenu {response.status_code}"
    print("GET (après DELETE): Pokémon non trouvé, suppression vérifiée.")