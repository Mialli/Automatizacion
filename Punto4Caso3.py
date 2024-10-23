#Ejercicio 4
#Caso 3
#Hacer un get a pikachu (https://pokeapi.co/api/v2/pokemon/pikachu/)
#Verificar que su experiencia base es mayor a 10 y menor a 1000
#Verificar que su tipo es “electric”



import requests

def test_pikachu_endpoint():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu/"
    
    response = requests.get(url)
    
    assert response.status_code == 200, f"Error: {response.status_code}. No se pudo acceder al endpoint."
    print("Respuesta positiva de la API")

    pikachu_data = response.json()

    base_experience = pikachu_data['base_experience']
    assert 10 < base_experience < 1000, f"La experiencia base de Pikachu debe ser mayor a 10 y menor a 1000, pero se recibió {base_experience}."
    print('Experiencia base esta entre 10 y 1000' if 10 < base_experience < 1000 else 'Experiencia base no esta entre 10 y 1000')

    types = []
    for type_info in pikachu_data['types']:
        types.append(type_info['type']['name'])
    assert "electric" in types, f"Pikachu debe ser de tipo 'electric', pero se encontró: {types}."
    print("Su pokemon es tipo electrico" if "electric" in types else "Su pokemon no es tipo electrico")
    
if __name__ == "__main__":
    test_pikachu_endpoint()

