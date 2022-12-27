from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome('/Users/petrnovikov/Desktop/ChromeDriver/chromedriver')
    base_url = 'https://www.saucedemo.com'
    driver.get(base_url)
    driver.maximize_window()
    login = 'standard_user'
    password_1 = 'secret_sauce'
    user_name = driver.find_element(By.ID, 'user-name')
    user_name.send_keys(login)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(password_1)
    button_login = driver.find_element(By.ID, 'login-button')
    button_login.click()
    time.sleep(5)
    num_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    num_1.click()
    num_2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    num_2.click()
    time.sleep(5)
    button_order = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    button_order.click()
    time.sleep(5)
    checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout.click()
    time.sleep(5)
    continue_1 = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_1.click()
    error = driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')
    error_1 = error.text
    assert error_1 == 'Error: First Name is required'
    print('YES')
    time.sleep(5)
    first_name = driver.find_element(By.ID, 'first-name')
    first_name.send_keys('Alexandr')
    last_name = driver.find_element(By.ID, 'last-name')
    last_name.send_keys('Grech')
    postal_code = driver.find_element(By.ID, 'postal-code')
    postal_code.send_keys('654987')
    time.sleep(5)
    continue_1 = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_1.click()
    finish = driver.find_element(By.ID, 'finish')
    finish.click()
    time.sleep(5)
    home = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
    home.click()

finally:
    time.sleep(5)
    driver.quit()
