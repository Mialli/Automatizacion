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

driver = webdriver.Chrome()

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
input()

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
assert errortext.text == "Error: Postal Code is required", "El mensaje de error no es mismo."

driver.quit()

print("Proceso de compra completado con verificación")