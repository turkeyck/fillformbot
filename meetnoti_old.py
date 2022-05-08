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
#舒伃's & 淑如's 會議通知

info = {
0: {"name": "遊覽車客運商業",
"meet_date": "1110428",
"number": "1110062049",
"year": 14,
"Num": 1,
"meet_type": 1,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 1,  # 1:會議通知, 2: 會議記錄
"time_hour": 10,
"time_min": 30,
"place": "風采宴會館-維多利亞餐廳(新竹市中正路245號7樓)",
"staff": "李淑如",
"phone": "03-5352386#302"},

1: {"name": "世界客屬總會新竹市分會",
"meet_date": "1110411",
"number": "1110061793",
"year": 12,
"Num": 6,
"meet_type": 7,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 1,  # 1:會議通知, 2: 會議記錄
"time_hour": 17,
"time_min": 40,
"place": "風采宴會館(新竹市中正路245號6樓)",
"staff": "李淑如",
"phone": "03-5352386#302"},
2: {"name": "記帳及報稅代理人",
"number": "1110062013",
"year": 5,
"Num": 14,
"meet_type": 2,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 1,  # 1:會議通知, 2: 會議記錄
"meet_date": "1110422",
"time_hour": 15,
"time_min": 30,
"place": "本會會所",
"staff": "李淑如",
"phone": "03-5352386#302"},
3: {"name": "酒類商業",
"number": "1110062029",
"year": 5,
"Num": 5,
"meet_type": 7,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 1,  # 1:會議通知, 2: 會議記錄
"meet_date": "1110420",
"time_hour": 18,
"time_min": 20,
"place": "風采宴會館(新竹市中正路245號6樓)",
"staff": "李淑如",
"phone": "03-5352386#302"},
4: {"name": "記帳士公會",
"number": "1110062009",
"year": 4,
"Num": 11,
"meet_type": 2,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 1,  # 1:會議通知, 2: 會議記錄
"meet_date": "1110413",
"time_hour": 14,
"time_min": 00,
"place": "本會會所",
"staff": "李淑如",
"phone": "03-5352386#302"},
5: {"name": "關埔國小教師會",
"number": "1110061406",
"year": 1,
"Num": 2,
"meet_type": 1,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 1,  # 1:會議通知, 2: 會議記錄
"meet_date": "1110429",
"time_hour": 14,
"time_min": 00,
"place": "線上",
"staff": "李淑如",
"phone": "03-5352386#302"}
}

n = 5

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
for i in range(n):
    driver.switch_to.parent_frame()
    driver.switch_to.frame("mainframe")
    search = driver.find_element(By.NAME, "queryAll").click()
    search_name = driver.find_element(By.NAME, "q_civicName")
    search_name.click()
    search_name.send_keys(info[i]["name"])
    submit = driver.find_element(By.NAME, "querySubmit").click()

    meeting_noti = driver.find_elements(By.ID, "t2")[1]
    meeting_noti.click()
    insert = driver.find_element(By.ID, "spanInsert").click()

    #insert info...
    paper_num = driver.find_element(By.NAME, "offDoc").send_keys(info[i]["number"])

    data_type = Select(driver.find_element(By.NAME, "meetstep")).select_by_index(info[i]["data_type"])
    meet_type = Select(driver.find_element(By.NAME, "meetType")).select_by_index(info[i]["meet_type"]) #1: 會員大會, 2: 理監事, 7:理監事聯席
    meetDate = driver.find_element(By.NAME, "meetDate").send_keys(info[i]["meet_date"])

    year = driver.find_element(By.NAME, "expNum")
    year.clear()
    year.send_keys(info[i]["year"])
    Num = driver.find_element(By.NAME, "meetNum").send_keys(info[i]["Num"])
    hour = Select(driver.find_element(By.NAME, "meetTime_h")).select_by_index(info[i]["time_hour"])
    minite = Select(driver.find_element(By.NAME, "meetTime_m")).select_by_index(info[i]["time_min"] +1)
    location = driver.find_element(By.NAME, "location").send_keys(info[i]["place"])
    staff = driver.find_element(By.NAME, "undertaker").send_keys(info[i]["staff"])
    phone = driver.find_element(By.NAME, "undertaker_tel").send_keys(info[i]["phone"])
    confirm = driver.find_element(By.NAME, "confirm").click()


    # Reset
    alert = driver.switch_to.alert
    alert.accept()
    print(info[i]["name"] + "completed!")
    driver.switch_to.parent_frame()
    driver.switch_to.frame("menu")
    driver.find_element(By.ID, "sd4").click()


# #秀芬's 會議通知
# func2_1 = driver.find_element(By.ID, "jd1").click()
# func2_2 = driver.find_element(By.ID, "jd2").click()
# func2_3 = driver.find_element(By.ID, "sd4").click()

