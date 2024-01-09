import datetime
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchWindowException

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class Test_1():
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print('Start test')

        password = "secret_sauce"
        login_list = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "error_user", "visual_user"]

        for i in login_list:
            try:
                user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
                user_name.send_keys(i)
                print("Input login")
                user_pass = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
                user_pass.send_keys(password)
                print("Password")
                button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
                button_login.click()
                print("Click login button")
                products_button = driver.find_element(By.XPATH, "//span[@class='title']")
                value_products_button = products_button.text
                assert value_products_button == "Products"
                print('Yes')
                menu = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
                menu.click()
                time.sleep(3)
                logout_cl = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
                logout_cl.click()

            except NoSuchElementException:
                driver.refresh()

        driver.close()








test = Test_1()
test.test_select_product()

