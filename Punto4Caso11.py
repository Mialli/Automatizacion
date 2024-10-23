#Sitio: Poke Api (https://pokeapi.co/api/v2)
#CASO1
#Hacer un get a berry/1
#Verificar que el size sea 20
#Verificar que el soil_dryness sea 15
#Verificar que en firmness, el name sea soft.

import requests

def test_berry_endpoint():
    test_status = True
    url = "https://pokeapi.co/api/v2/berry/1"

    response = requests.get(url)
    print("Comenzando prueba")
    
    assert response.status_code == 200, f"Error: {response.status_code}. No se pudo acceder al endpoint."
    print("Respuesta positiva de la API")

    berry_data = response.json()
    
    print(f"El tamaño de la berry es: {berry_data['size']}")
    if berry_data['size'] != 20: test_status = False
    print(True if berry_data['size'] == 20 else False)

    print(f"La sequedad del suelo esperada es: {berry_data['soil_dryness']}")
    if berry_data['soil_dryness'] != 15: test_status = False
    print(True if berry_data['soil_dryness'] == 15 else False)

    print(f"La firmeza del suelo es: {berry_data['firmness']['name']}")
    if berry_data['firmness']['name'] != "soft": test_status = False
    print(True if berry_data['firmness']['name'] == "soft" else False)

    if test_status: print("Pokedex actualizada con exito")
    else: print("Prueba finalizada sin exito")

if __name__ == "__main__":
    test_berry_endpoint()