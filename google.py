from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# import time

driver= webdriver.Chrome(r"C:\\chromedriver.exe")
url ='https://google.com'
driver.get(url)

# ver_code = input("Please enter verification code:")
account = driver.find_element(By.NAME, "q")
account.send_keys(input("Enter keywords:"))
account.send_keys(Keys.RETURN)
driver.maximize_window()
