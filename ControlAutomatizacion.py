#Ejercicio 3
#CASO 1
#El usuario se loguea al sitio como usuario standard user
#Ordenar los elementos por “price (low to high)”
#Verificar que los elementos estén ordenados

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

def test_ordenar_productos_por_precio():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    sorting_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(sorting_element)
    select.select_by_value("lohi")

    sorting_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
    select = Select(sorting_element)

    current_selection = select.first_selected_option
    current_selection_value = current_selection.get_attribute("value")

    assert current_selection_value == "lohi", f"El valor del filtro esperado era 'lohi' pero se obtuvo {current_selection_value}"

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_list = [float(price.text.replace('$', '')) for price in prices]

    if price_list == sorted(price_list):
        print("Los productos están ordenados de menor a mayor precio.")
    else:
        print("Los productos no están ordenados correctamente de menor a mayor.")

    driver.quit()

    print("El test fue realizado")

#Ejercicio 3
#CASO 2:
#El usuario se loguea al sitio como usuario standard user
#Incorporar al carrito todos los elementos
#Ir al carrito
#Verificar que todos los elementos están en el carrito
#Ir al checkout
#Ingresar nombre y clickear Continue
#Verificar que aparece el error “Error: Last Name is required”
#Ingresar un apellido y clickear Continue
#Verificar que aparece el error “Error: Postal Code is required”

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_agregar_todos_los_productos_al_carrito():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    items = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for item in items:
        item.click()

    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == len(items), "No todos los elementos están en el carrito."

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_input = driver.find_element(By.ID, "first-name")
    first_name_input.send_keys("Carina")
    continue_button = driver.find_element(By.CLASS_NAME, "btn_primary")
    continue_button.click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    errortext = error_message.find_element(By.TAG_NAME, "h3")
    assert errortext.text == "Error: Last Name is required", "El mensaje de error no es el mismo"

    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Saucedo")
    continue_button.click()

    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    errortext = error_message.find_element(By.TAG_NAME, "h3")
    assert errortext.text == "Error: Postal Code is required", "El mensaje de error no es el mismo."

    driver.quit()

    print("Proceso de compra completado con verificación")


#Ejercicio 3
#CASO 3
#El usuario se loguea al sitio como usuario standard user
#Agregar un elemento al carrito
#Ir al carrito
#Remover el artículo
#Verificar que el sitio no tiene artículos agregados
#Ir a Continue Shopping
#Agregar dos elementos
#Ir al carrito
#Verificar que los elementos existen
#Hacer el checkout
#Finalizar la compra
#Verificar que la compra fue realizada


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_cart_and_checkout():
    print("Comenzando test...")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")


    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    add_button = driver.find_element(By.CLASS_NAME, "btn_inventory")
    add_button.click()


    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


    driver.find_element(By.CLASS_NAME, "cart_button").click()

    cart_item_list = driver.find_elements(By.CLASS_NAME, "cart_itemr")
    assert len(cart_item_list) == 0, "El carrito no está vacío"


    driver.find_element(By.XPATH, "//button[text()='Continue Shopping']").click()

    add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    add_buttons[0].click()
    add_buttons[1].click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 2, "No se encontraron los artículos en el carrito"

    driver.find_element(By.CLASS_NAME, "checkout_button").click()

    driver.find_element(By.ID, "first-name").send_keys("Carina")
    driver.find_element(By.ID, "last-name").send_keys("Saucedo")
    driver.find_element(By.ID, "postal-code").send_keys(3656)
    driver.find_element(By.CLASS_NAME, "btn_primary").click()
    driver.find_element(By.ID, "finish").click()

    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header")
    assert "Thank you for your order!" in confirmation_message.text, "La compra no se realizo correctamente"
    driver.quit()
    print("La prueba finalizo con exito")

if __name__ == "__main__":
    test_cart_and_checkout()

#Ejercicio 4
#Sitio: Poke Api (https://pokeapi.co/api/v2)
#CASO 1
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
