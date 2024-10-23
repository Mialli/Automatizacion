import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test1(unittest.TestCase):
    def test_caso1(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.saucedemo.com/')
        self.driver.find_element(By.ID,'user-name').send_keys('standard_user')
        self.driver.find_element(By.ID,'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID,'login-button').click()
        self.driver.find_element(By.ID,'add-to-cart-sauce-labs-onesie').click()
        self.driver.find_element(By.ID,'add-to-cart-sauce-labs-fleece-jacket').click()
        self.driver.find_element(By.ID,'shopping_cart_container').click()
        self.driver.find_element(By.ID,'checkout').click()
        self.driver.find_element(By.ID,'first-name').send_keys('Micaela')
        self.driver.find_element(By.ID,'last-name').send_keys('Lirussi')
        self.driver.find_element(By.ID,'postal-code').send_keys('3656')
        self.driver.find_element(By.ID,'continue').click()
        self.assertEqual('Sauce Labs Onesie', self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')[0].text)
        self.assertEqual('Sauce Labs Fleece Jacket', self.driver.find_elements(By.CLASS_NAME,'inventory_item_name')[1].text)
        self.driver.find_element(By.ID,'finish').click()
        self.assertEqual('Thank you for your order!', self.driver.find_element(By.CLASS_NAME,'complete-header').text)
    test_caso1       
        



