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

select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_value("lohi")

prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
price_list = [float(price.text.replace('$', '')) for price in prices]
if price_list == sorted(price_list):
    print("Los productos están correctamente ordenados por precio de menor a mayor.")
else:
    print("Error: Los productos no están ordenados correctamente.")
driver.quit()