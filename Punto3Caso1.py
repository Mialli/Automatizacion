#CASO1
#El usuario se loguea al sitio como usuario standard user
#Ordenar los elementos por “price (low to high)”
#Verificar que los elementos estén ordenados

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
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