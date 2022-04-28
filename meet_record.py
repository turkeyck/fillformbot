from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver= webdriver.Chrome(r"C:\\chromedriver.exe")
url ='https://swis.hccg.gov.tw/hcss/'
driver.get(url)

ver_code = input("Please enter verification code:")
account = driver.find_element(By.NAME, "userID")
password = driver.find_element(By.NAME, "password")
veri = driver.find_element(By.NAME, "authRnd")

account.send_keys("010385")
password.send_keys("chA123456#")

veri.send_keys(ver_code)
veri.send_keys(u'\ue007')
time.sleep(1)


# After login...
#舒伃's & 淑如's 會議紀錄

info = {"name": "新竹市樹林頭長春會",
"meet_date": "1110415",
"number": "1111111111",
"year": 14,
"Num": 7,
"meet_type": 1,
"data_type": 0,
"time_hour": 17,
"time_min": 30,
"place": "晶采宴會館(新竹市中正路245號6樓)",
"staff": "楊舒伃",
"phone": "03-5352386#302"}


driver.switch_to.frame("fbody")
driver.switch_to.frame("menu")
# driver.switch_to.frame("")
func1_1 = driver.find_element(By.ID, "jd19")
func1_1.click()

# func = driver.find_element(By.XPATH, '//img[@id="jd19"]')
# func.click()
# func1_1 = driver.find_element(By.ID, "jd1")
# func1_1.click()
func1_2 = driver.find_element(By.ID, "jd1").click()
func1_3 = driver.find_element(By.ID, "jd2").click()
func1_3 = driver.find_element(By.ID, "sd4").click()

time.sleep(2)

driver.switch_to.parent_frame()
driver.switch_to.frame("mainframe")
search = driver.find_element(By.NAME, "queryAll").click()
search_name = driver.find_element(By.NAME, "q_civicName")
search_name.click()
search_name.send_keys(info["name"])
submit = driver.find_element(By.NAME, "querySubmit").click()

meeting_noti = driver.find_elements(By.ID, "t2")[1]
meeting_noti.click()
final_page = driver.find_element(By.PARTIAL_LINK_TEXT, '末頁').click()
pre_page = driver.find_element(By.PARTIAL_LINK_TEXT, '上一頁')
# if //*[@id="listTBODY"]/tr[9]:

driver.find_element(By.XPATH, '//*[@id="listTBODY"]/tr[10]').click()
meetDate = driver.find_element(By.NAME, "meetDate").get_attribute('value')
meet_type = driver.find_element(By.NAME, "meetType").get_attribute('value')
print(meetDate, meet_type)
if meet_type == "02" and meetDate == info["meet_date"]:
    driver.find_element(By.NAME, "update").click()
    driver.find_element(By.NAME, "offDoc").send_keys("/" + info["number"])
    driver.find_element(By.NAME, "confirm").click()
#搜尋"會議通知"
# try:
#     driver.find_element(By.LINK_TEXT, '1110108').click()
# except:
#     next_page.click()
#     insert = driver.find_element(By.ID, "spanInsert").click()

# //*[@id="listTBODY"]/tr[i]/td[3] 日期xpath
'''
insert = driver.find_element(By.ID, "spanInsert").click()

#insert info...
paper_num = driver.find_element(By.NAME, "offDoc").send_keys(info["number"])

data_type = Select(driver.find_element(By.NAME, "meetstep")).select_by_index(1)
meet_type = Select(driver.find_element(By.NAME, "meetType")).select_by_index(7) #1: 會員大會, 2: 理監事, 7:理監事聯席
meetDate = driver.find_element(By.NAME, "meetDate").send_keys(info["meet_date"])

year = driver.find_element(By.NAME, "expNum")
year.clear()
year.send_keys(info["year"])
Num = driver.find_element(By.NAME, "meetNum").send_keys(info["Num"])
hour = Select(driver.find_element(By.NAME, "meetTime_h")).select_by_index(info["time_hour"])
minite = Select(driver.find_element(By.NAME, "meetTime_m")).select_by_index(info["time_min"] +1)
location = driver.find_element(By.NAME, "location").send_keys(info["place"])
staff = driver.find_element(By.NAME, "undertaker").send_keys(info["staff"])
phone = driver.find_element(By.NAME, "undertaker_tel").send_keys(info["phone"])
confirm = driver.find_element(By.NAME, "confirm").click()


# Reset
alert = driver.switch_to.alert
alert.accept()
driver.switch_to.parent_frame()
driver.switch_to.frame("menu")
driver.find_element(By.ID, "sd4").click()

#----------------------------------------------------------------------#

#----------------------------------------------------------------------#
'''

