#Ejercicio 4
#CASO 2
#Hacer un get a berry/2
#Verificar que en firmness, el name sea super-hard
#Verificar que el size sea mayor al del punto anterior
#Verificar que el soil_dryness sea igual al del punto anterior

import requests

def test_berry_endpoints():
    url_1 = "https://pokeapi.co/api/v2/berry/1"
    response_1 = requests.get(url_1)
    assert response_1.status_code == 200, f"Error al acceder a berry/1: {response_1.status_code}."
    berry_1_data = response_1.json()

    url_2 = "https://pokeapi.co/api/v2/berry/2"
    response_2 = requests.get(url_2)
    assert response_2.status_code == 200, f"Error al acceder a berry/2: {response_2.status_code}."
    berry_2_data = response_2.json()

    assert berry_2_data['firmness']['name'] == "super-hard", f"El nombre de firmeza esperado es 'super-hard', pero se recibió '{berry_2_data['firmness']['name']}'."
    print(f"La firmeza de berry2 es {berry_2_data['firmness']['name']} y {'no ' if berry_2_data['firmness']['name'] != 'super-hard' else ''}es igual a 'super-hard'")

    assert berry_2_data['size'] > berry_1_data['size'], f"El size esperado para berry/2 debe ser mayor que {berry_1_data['size']}, pero se recibió {berry_2_data['size']}."
    print(f"El size de berry2 es {berry_2_data['size']} y {'' if berry_2_data['size'] > berry_1_data['size'] else 'no '}es mayor a berry1 que era {berry_1_data['size']}")

    assert berry_2_data['soil_dryness'] == berry_1_data['soil_dryness'], f"El soil_dryness de berry/2 debe ser igual a {berry_1_data['soil_dryness']}, pero se recibió {berry_2_data['soil_dryness']}."
    print(f"Suelo de berry2 es {berry_2_data['soil_dryness']} y {'' if berry_2_data['soil_dryness'] == berry_1_data['soil_dryness'] else 'no '}es igual al suelo de berry1 que es {berry_1_data['soil_dryness']}")
    print("Pokedex Actualizada con exito")
if __name__ == "__main__":
    test_berry_endpoints()