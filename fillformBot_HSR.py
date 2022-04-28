from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\\chromedriver.exe")
url = r'https://irs.thsrc.com.tw/IMINT/?locale=tw&_ga=2.129051788.1001438124.1647866447-507111954.1647866447'
driver.get(url)
driver.find_element(By.ID, "btn-confirm").click()
ve = input("Please enter the verification code:")
start = driver.find_element(By.NAME, "selectStartStation")
end = driver.find_element(By.NAME, "selectDestinationStation")
# date = driver.find_element_by_id("toTimeInputField")
date = driver.find_element(By.NAME, "toTimeInputField")
time = driver.find_element(By.NAME, "toTimeTable")
ver = driver.find_element(By.ID, "securityCode")

'''
ticket type: 全票:0, 孩童票(6~11歲):1
            愛心票: 2 敬老票(65以上): 3
            大學生優惠: 4
'''

info = {"start":"新竹",
"end": "左營",
"date": "2022/04/05", # YYYY/MM/DD
"time": "19:00",
"quantity": "1",
"ticket_type": "0"} 
 
ticket = driver.find_element(By.NAME, "ticketPanel:rows:" + info["ticket_type"] + ":ticketAmount")
start.send_keys(info["start"])
end.send_keys(info["end"])
date.clear()
date.send_keys(info["date"]) # YYYY/MM/DD
time.send_keys(info["time"])
ticket.send_keys("0")
ticket.send_keys(info["quantity"]) # default: "blank" for 1
ver.send_keys(ve)
# ver.send_keys(Keys.RETURN);
