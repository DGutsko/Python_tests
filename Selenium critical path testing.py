import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standard_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("Input login")
user_pass = driver.find_element(By.XPATH, "//input[@id='password']")
user_pass.send_keys(password_all)
print("Password")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("Click login button")

'''INFO Product 1'''

product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click()
print('Select Product 1')


'''INFO Product 2'''

product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div")
value_price_product_2 = price_product_2.text
print(value_price_product_2)

select_product_2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
select_product_2.click()
print('Select Product 2')


cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()
print('Enter cart')


'''Info cart Product 1'''

cart_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)

assert value_product_1 == value_cart_product_1
print('INFO cart Product 1 GOOD')

cart_price_product_1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)

assert value_price_product_1 == value_cart_price_product_1
print('INFO cart PRICE Product 1 GOOD')



'''Info cart Product 2'''

cart_product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)

assert value_product_2 == value_cart_product_2
print('INFO cart Product 2 GOOD')

cart_price_product_2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_cart_price_product_2 = cart_price_product_2.text
print(value_cart_price_product_2)

assert value_price_product_2 == value_cart_price_product_2
print('INFO cart PRICE Product 2 GOOD')


checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print('Click checkout')

'''Select user info'''
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Daria')
print('INPUT First name')

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Gutsko')
print('INPUT Last name')

zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys('344018')
print('INPUT Zip')

button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Click Button continue')


'''INFO Finish Product 1'''

finish_product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)

assert value_finish_product_1 == value_cart_product_1
print('INFO FINISH cart Product 1 GOOD')

finish_price_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)

assert value_finish_price_product_1 == value_cart_price_product_1
print('INFO cart FINISH PRICE Product 1 GOOD')

'''INFO Finish Product 2'''

finish_product_2 = driver.find_element(By.XPATH, "//a[@id='item_1_title_link']")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)

assert value_finish_product_2 == value_cart_product_2
print('INFO FINISH cart Product 2 GOOD')

finish_price_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div")
value_finish_price_product_2 = finish_price_product_2.text
print(value_finish_price_product_2)

assert value_finish_price_product_2 == value_cart_price_product_2
print('INFO cart FINISH PRICE Product 2 GOOD')

res_prod_1 = value_finish_price_product_1.replace('$', '', 1)
print(res_prod_1)

res_prod_2 = value_finish_price_product_2.replace('$', '', 1)
print(res_prod_2)


summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print(value_summary_price)
res_summery = value_summary_price.lstrip('Item total: $')
result_summery = float(res_summery)


result_price = float(res_prod_1) + float(res_prod_2)
print(result_price)

assert result_summery == result_price
print("Result price is GOOD")