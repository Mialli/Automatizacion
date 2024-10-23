#Sitio: Poke Api (https://pokeapi.co/api/v2)
#Ejercicio 4
#CASO 1
#Hacer un get a berry/1
#Verificar que el size sea 20
#Verificar que el soil_dryness sea 15
#Verificar que en firmness, el name sea soft.

import requests

def test_berry_endpoint():
    url = "https://pokeapi.co/api/v2/berry/1"

    response = requests.get(url)
    print("Comenzando prueba")
    
    assert response.status_code == 200, f"Error: {response.status_code}. No se pudo acceder al endpoint."
    print("Codigo 200 recibido de la api")

    berry_data = response.json()

    assert berry_data['size'] == 20, f"El tamaño esperado es 20, pero se recibió {berry_data['size']}."
    print("El tamaño de berry es 20")

    assert berry_data['soil_dryness'] == 15, f"La sequedad del suelo esperada es 15, pero se recibió {berry_data['soil_dryness']}."
    print("El 'soil_dryness de berry es 15")

    assert berry_data['firmness']['name'] == "soft", f"El nombre de firmeza esperado es 'soft', pero se recibió '{berry_data['firmness']['name']}'."
    print("El firmness_name es 'soft'")
    print("Prueba finalizada")

if __name__ == "__main__":
    test_berry_endpoint()
