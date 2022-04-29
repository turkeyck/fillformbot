from distutils.spawn import find_executable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome(r"C:\\chromedriver.exe")
url ='https://group.moi.gov.tw/sgms/admin/admin!login.action?isLocal=1'
driver.get(url)
driver.maximize_window()

login = driver.find_element(By.ID, "normalLogin").click()
ver_code = input("Please enter verification code:")
account = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
veri = driver.find_element(By.NAME, "kaptcha")

account.send_keys("HC001")
password.send_keys("aaHC001")

veri.send_keys(ver_code)
veri.send_keys(u'\ue007')
time.sleep(1)


# After login...
#舒伃's & 淑如's 會議通知

info = {
0: {"name": "新竹市東門扶輪社",
"come_date": "1110414", # 來文日期
"meet_date": "1101210", # 開會日期
"receive_date": "1110421", # 收文日期
"number": "1110066915", # 收文字號
"year": 8, # 屆
"num": 1, # 次
"meet_type": 1,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 2,  # 1:會議通知, 2: 會議記錄 -----------理監事會end
# "time_hour": 16, # 會議時間(時)
# "time_min": 00, # 會議時間(分)
"indow": "25", # 應到人數
"sdow": "18", # 實到人數
"waytou": "", # (含)委託__人
"day_off": "7", #請假人數
"start_date": "1110701", # 任期開始日期
"duration": "1", # 任期__年
"end_date": "1120630", # 任期結束日期  -----------會員大會end
"place": "風采宴會館(新竹市中正路245號6樓)", # 會議地點 
"staff": "李淑如",
"phone": "03-5352386#302"},

1: {"name": "新興獅子會",
"come_date": "1110418", # 來文日期
"meet_date": "1110320", # 開會日期
"receive_date": "1110420", # 收文日期
"number": "1110066057", # 收文字號
"year": 32, # 屆
"num": 1, # 次
"meet_type": 1,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 2,  # 1:會議通知, 2: 會議記錄
# "time_hour": 11, # 會議時間(時)
# "time_min": 30, # 會議時間(分)
"indow": "21", # 應到人數
"sdow": "15", # 實到人數
"waytou": "", # (含)委託__人數
"day_off": "", #請假人數
"start_date": "1110701", # 任期開始日期
"duration": 1, # 任期__年
"end_date": "1120630", # 任期結束日期
"place": "風采宴會館(新竹市中正路245號6樓)", # 會議地點
"staff": "李淑如",
"phone": "03-5352386#302"},

2: {"name": "新興獅子會",
"come_date": "1110418", # 來文日期
"meet_date": "1110320", # 開會日期
"receive_date": "1110420", # 收文日期
"number": "1110066057", # 收文字號
"year": 32, # 屆
"num": 1, # 次
"meet_type": 2,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 2,  # 1:會議通知, 2: 會議記錄
# "time_hour": 11, # 會議時間(時)
# "time_min": 30, # 會議時間(分)
"indow": "21", # 應到人數
"sdow": "15", # 實到人數
"waytou": "", # (含)委託__人數
"day_off": "", #請假人數
"start_date": "1110701", # 任期開始日期
"duration": 1, # 任期__年
"end_date": "1120630", # 任期結束日期
"place": "風采宴會館(新竹市中正路245號6樓)", # 會議地點
"staff": "李淑如",
"phone": "03-5352386#302"},


3: {"name": "中正國際獅子會",
"come_date": "1110413", # 來文日期
"meet_date": "1110327", # 開會日期
"receive_date": "1110419", # 收文日期
"number": "1110065150", # 收文字號
"year": 42, # 屆
"num": 1, # 次
"meet_type": 2,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 2,  # 1:會議通知, 2: 會議記錄
# "time_hour": 11, # 會議時間(時)
# "time_min": 0, # 會議時間(分)
"indow": "", # 應到人數
"sdow": "", # 實到人數
"waytou": "", # (含)委託__人數
"day_off": "", #請假人數
"start_date": "", # 任期開始日期
"duration": 1, # 任期__年
"end_date": "", # 任期結束日期
"place": "風采宴會館(新竹市中正路245號6樓)", # 會議地點
"staff": "李淑如",
"phone": "03-5352386#302"},

4: {"name": "新竹市東大福德長青協會",
"come_date": "1110417", # 來文日期
"meet_date": "1110408", # 開會日期
"receive_date": "1110420", # 收文日期
"number": "1110065848", # 收文字號
"year": 6, # 屆
"num": 3, # 次
"meet_type": 1,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 2,  # 1:會議通知, 2: 會議記錄
"time_hour": 17, # 會議時間(時)
"time_min": 30, # 會議時間(分)
"indow": 142, # 應到人數
"sdow": 128, # 實到人數
"waytou": "", # (含)委託__人數
"day_off": 14, #請假人數
"start_date": "", # 任期開始日期
"duration": 3, # 任期__年
"end_date": "", # 任期結束日期
"place": "風采宴會館(新竹市中正路245號6樓)", # 會議地點
"staff": "李淑如",
"phone": "03-5352386#302"},
}
first_time_info = {
    0: {
        "boa_name": "范碧涵", #理事長姓名
        "boa_gender": 1, # 1:female, 2:male
        "boa_birth": "0720328", #理事長生日 YYYMMDD
        "boa_tel": "0986-169986", # 聯絡電話
        "sta_name": "吳明修",
        "sta_title": "秘書長",
        "sta_gender": 2,
        "sta_birth": "",
        "sta_tel": "0958-089101",
        "sta_address": "台北市中山區民權東路3段4號13樓"
    },
    1: {
        "boa_name": "徐文彬", #理事長姓名
        "boa_gender": 2, # 1:female, 2:male
        "boa_birth": "0650207", #理事長生日 YYYMMDD
        "boa_tel": "0910-295642", # 聯絡電話
        "sta_name": "孟憲群",
        "sta_title": "秘書",
        "sta_gender": 0,
        "sta_birth": "",
        "sta_tel": "0989-600193",
        "sta_address": "新竹市延平路3段335巷1弄30號2F"
    }
}
n = 4

driver.switch_to.frame("menuFrame")
func1_1 = driver.find_elements(By.CLASS_NAME, "sum")[1]
func1_1.click()
time.sleep(1)
# func1_2 = driver.find_element(By.XPATH, '//*[@id="down"]/div/ul/li[2]/div[1]/a')
func1_2 = driver.find_element(By.LINK_TEXT, "會務運作管理")
func1_2.click()
# driver.find_element(By.XPATH, '//*[@id="down"]/div/ul/li[2]/div[2]/a').click()
# driver.find_element(By.XPATH, '//*[@id="down"]/div/ul/li[2]/div[3]/a').click()
# driver.find_element(By.XPATH, '//*[@id="down"]/div/ul/li[2]/div[4]/a').click()

for i in range(n):
    driver.switch_to.parent_frame()
    driver.switch_to.frame("mainFrame")

    search = driver.find_element(By.NAME, "pager.keyword")
    search.send_keys(info[i]["name"])
    search.send_keys(u'\ue007')
    driver.find_element(By.PARTIAL_LINK_TEXT, info[i]['name']).click()
    # open_menu = driver.find_element(By.ID, "menu1").click()
    #會務活動管理
    # driver.find_element(By.XPATH, '/html/body/div[3]/ul/li[2]/a')
    action = ActionChains(driver)

    #會員大會&理監事會
    premeet = driver.find_element(By.LINK_TEXT, '會務活動管理')
    meet = driver.find_element(By.XPATH, '//*[@id="menu1"]/ul/li[2]/div/ul/li[1]/a/span')
    bigmeet = driver.find_element(By.XPATH, '//*[@id="menu1"]/ul/li[2]/div/ul/li[1]/div/ul/li[1]/a')
    boardmeet = driver.find_element(By.XPATH, '//*[@id="menu1"]/ul/li[2]/div/ul/li[1]/div/ul/li[2]/a')

    if info[i]["meet_type"] == 1:
        #會員大會
        #(1)新增會議記錄
        action.move_to_element(premeet).perform()
        action.move_to_element(meet).perform()
        action.move_to_element(bigmeet).click().perform()
        add = driver.find_element(By.XPATH, '//*[@id="listForm"]/div[1]/div/input[1]').click()
        year = driver.find_element(By.ID, 'sessionTime').send_keys(info[i]["year"])
        num = driver.find_element(By.ID, 'sessionTime1').send_keys(info[i]["num"])
        come_date = driver.find_element(By.NAME, 'sogpCommMeet.meetforgDate').send_keys(info[i]["come_date"])
        meet_type = Select(driver.find_element(By.ID, 'meetType')).select_by_index(1)
        meet_date = driver.find_element(By.ID, 'meetDate').send_keys(info[i]["meet_date"])
        receive_date = driver.find_element(By.NAME, 'sogpCommMeet.receiveDate').send_keys(info[i]["receive_date"])
        paper_num = driver.find_element(By.ID, 'receiveDoc').send_keys(info[i]["number"])
        indow = driver.find_element(By.NAME, 'sogpCommMeet.attendCount')
        indow.clear()
        indow.send_keys(info[i]["indow"])
        sdow = driver.find_element(By.NAME, 'sogpCommMeet.attendActual').send_keys(info[i]["sdow"])
        waytou = driver.find_element(By.NAME, 'sogpCommMeet.attendDelegate').send_keys(info[i]["waytou"])
        day_off = driver.find_element(By.NAME, 'sogpCommMeet.attendDayoff').send_keys(info[i]["day_off"])
        save_record = driver.find_element(By.XPATH, '//*[@id="INFO"]/div/input[1]').click()
        alert = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/input')
        alert.click()
    #--------------------------------------------------------------------------------------------
        #(2)新增預算表
        pre_fi = driver.find_element(By.LINK_TEXT, '財務活動管理')
        fi = driver.find_element(By.XPATH, '//*[@id="menu1"]/ul/li[3]/div/ul/li[1]/a')
        action.move_to_element(pre_fi).perform()
        action.move_to_element(fi).click().perform()
        add_fi = driver.find_element(By.XPATH, '//*[@id="listForm"]/div[1]/div/input[2]').click()
        fi_year = driver.find_element(By.NAME, 'sogpFinancial.sessionTime').send_keys(info[i]["year"])
        fi_num = driver.find_element(By.NAME, 'sogpFinancial.sessionTime1').send_keys(info[i]["num"])
        fi_meet_type = Select(driver.find_element(By.NAME, 'sogpFinancial.conferenceName')).select_by_index(7) #7 for "會員大會"
        fi_come_date = driver.find_element(By.NAME, 'sogpFinancial.meetforgDate').send_keys(info[i]["come_date"])
        fi_receive_date = driver.find_element(By.NAME, 'sogpFinancial.receiveDate').send_keys(info[i]["receive_date"])
        fi_number = driver.find_element(By.NAME, 'sogpFinancial.receiveNo').send_keys(info[i]["number"])
        # fi_file = driver.find_element(By.NAME, 'file1').click()
        save_fi = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div[5]/input[1]').click()
        fi_alert = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/input')
        fi_alert.click()
        
        #(3)會員名冊
        pre_mem = driver.find_element(By.LINK_TEXT, '團體基本資料')
        mem = driver.find_element(By.XPATH, '//*[@id="menu1"]/ul/li[1]/div/ul/li[2]/a')
        action.move_to_element(pre_mem).perform()
        action.move_to_element(mem).click().perform()
        driver.switch_to.frame("tabIframe")
        # driver.find_element(By.XPATH, '//*[@id="tablist"]/li[1]/a').click()
        add_mem_list = driver.find_element(By.XPATH, '//*[@id="listForm"]/div[1]/div/input[1]').click()
        mem_year = driver.find_element(By.NAME, 'sogpNameList.nlPeriod').send_keys(info[i]['year'])
        mem_num = driver.find_element(By.NAME, 'sogpNameList.nlTimes').send_keys(info[i]['num'])
        list_type = driver.find_elements(By.NAME, 'sogpNameList.nlType')[2].click()
        start_date = driver.find_element(By.NAME, 'sogpNameList.termStartDate').send_keys(info[i]["start_date"])
        end_date = driver.find_element(By.NAME, 'sogpNameList.termStopDate').send_keys(info[i]["end_date"])
        driver.find_element(By.NAME, 'sogpNameList.historyYN').click()
        mem_submit = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div/input[1]').click()
        mem_alert = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/input')
        mem_alert.click()
        if info[i]["num"] == 1:
            #(5)理監事名冊上傳 & 理監事名冊 & 工作人員名冊
            #理監事名冊上傳
            add_boa_list = driver.find_element(By.XPATH, '//*[@id="listForm"]/div[1]/div/input[1]').click()
            boa_year = driver.find_element(By.NAME, 'sogpNameList.nlPeriod').send_keys(info[i]['year'])
            boa_num = driver.find_element(By.NAME, 'sogpNameList.nlTimes').send_keys(info[i]['num'])
            list_type = driver.find_elements(By.NAME, 'sogpNameList.nlType')[0].click()
            start_date = driver.find_element(By.NAME, 'sogpNameList.termStartDate').send_keys(info[i]["start_date"])
            end_date = driver.find_element(By.NAME, 'sogpNameList.termStopDate').send_keys(info[i]["end_date"])
            driver.find_element(By.NAME, 'sogpNameList.historyYN').click()
            boa_submit = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div/input[1]').click()
            boa_alert = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/input')
            boa_alert.click()
            #理監事名冊
            driver.switch_to.parent_frame()
            driver.find_element(By.XPATH, '//*[@id="tablist"]/li[2]/a').click()
            driver.switch_to.frame("tabIframe")
            driver.find_element(By.XPATH, '//*[@id="listForm"]/div[1]/div/input[2]').click()
            boa_year_1 = driver.find_element(By.NAME, 'sogpDirector.term').send_keys(info[i]["year"])
            boa_type = Select(driver.find_element(By.ID, 'titleType')).select_by_index("1")
            boa_number = driver.find_element(By.NAME, 'sogpDirector.certificateDoc').send_keys(info[i]["number"])
            boa_duration = driver.find_element(By.NAME, 'sogpDirector.termPeriod').send_keys(info[i]["duration"])
            boa_start_date = driver.find_element(By.NAME, 'sogpDirector.termStartDte').send_keys(info[i]["start_date"])
            action.send_keys(Keys.TAB)
            time.sleep(1)
            # boa_end_date = driver.find_element(By.NAME, 'sogpDirector.termEndtDte').send_keys("")
            
            boa_name = driver.find_element(By.NAME, 'sogpDirector.name').send_keys(first_time_info[i]["boa_name"])
            boa_gender = Select(driver.find_element(By.NAME, 'sogpDirector.sex')).select_by_index(first_time_info[i]["boa_gender"]) #1 for female, 2 for male
            boa_birth = driver.find_element(By.NAME, 'sogpDirector.birthDte').send_keys(first_time_info[i]["boa_birth"])
            boa_tel = driver.find_element(By.NAME, 'sogpDirector.tel').send_keys(first_time_info[i]["boa_tel"])
            boa_submit = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div/input[1]').click()
            boa_alert_1 = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/input')
            boa_alert_1.click()
            #工作人員名冊
            driver.switch_to.parent_frame()
            driver.find_element(By.XPATH, '//*[@id="tablist"]/li[3]/a').click()
            driver.switch_to.frame("tabIframe") 
            driver.find_element(By.XPATH, '//*[@id="listForm"]/div[1]/div/input[1]').click() #新增
            sta_year = driver.find_element(By.NAME, 'sogpEmp.term').send_keys(info[i]["year"])
            sta_duration = driver.find_element(By.NAME, 'sogpEmp.termPeriod').send_keys(info[i]["duration"])
            sta_start_date = driver.find_element(By.NAME, 'sogpEmp.termStartDte').send_keys(info[i]["start_date"])
            # sta_end_date = driver.find_element(By.NAME, 'sogpEmp.termEndtDte').send_keys("")
            action.send_keys(Keys.TAB)
            time.sleep(1)
            if first_time_info[i]["sta_title"] == "總幹事":
                sta_title = driver.find_elements(By.NAME, 'sogpEmp.category')[0].click()
            else:
                sta_title_other = driver.find_elements(By.NAME, 'sogpEmp.category')[1].click()
                sta_title_name = driver.find_element(By.ID, 'categoryOtherText').send_keys(first_time_info[i]["sta_title"])
            sta_type = driver.find_element(By.NAME, 'sogpEmp.titleType2').click() #專職

            sta_name = driver.find_element(By.NAME, 'sogpEmp.name').send_keys(first_time_info[i]["sta_name"])
            sta_gender = Select(driver.find_element(By.NAME, 'sogpEmp.sex')).select_by_index(first_time_info[i]["sta_gender"]) #1 for female, 2 for male
            sta_birth = driver.find_element(By.NAME, 'sogpEmp.birthDte').send_keys(first_time_info[i]["sta_birth"])
            sta_city = Select(driver.find_element(By.ID, 'connectCity')).select_by_index(6) # 5:竹縣, 6: 竹市
            sta_city = driver.find_element(By.NAME, 'sogpEmp.householdAddress').send_keys(first_time_info[i]["sta_address"])
            sta_tel = driver.find_element(By.NAME, 'sogpEmp.tel').send_keys(first_time_info[i]["sta_tel"])
            sta_submit = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div/input[1]').click()
            sta_alert = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/input')
            sta_alert.click()
            #(4)章程
            driver.switch_to.parent_frame() # to "mainFrame"
            pre_rule = driver.find_element(By.LINK_TEXT, '團體基本資料')
            rule = driver.find_element(By.XPATH, '//*[@id="menu1"]/ul/li[1]/div/ul/li[1]/a')
            action.move_to_element(pre_rule).perform()
            action.move_to_element(rule).click().perform()
            add_rule = driver.find_element(By.XPATH, '//*[@id="listForm"]/div[1]/div/input[2]').click()
            rule_year = driver.find_element(By.NAME, 'sogpRule.sessionTime').send_keys(info[i]["year"])
            rule_num = driver.find_element(By.NAME, 'sogpRule.sessionTime1').send_keys(info[i]["num"])
            rule_dur = driver.find_element(By.NAME, 'sogpRule.termPeriod').send_keys(info[i]["duration"])
            rule_sub = driver.find_element(By.XPATH, '//*[@id="inputForm"]/div/input[1]').click()
            rule_alert = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/input')
            rule_alert.click()
            # Restart
            driver.switch_to.parent_frame()
            driver.switch_to.parent_frame()
            driver.switch_to.frame("menuFrame")
            mem_func1_2 = driver.find_element(By.LINK_TEXT, "會務運作管理")
            mem_func1_2.click()
        elif info[i]["num"] != 1:
            driver.switch_to.parent_frame()
            driver.switch_to.parent_frame()
            driver.switch_to.frame("menuFrame")
            mem_func1_2 = driver.find_element(By.LINK_TEXT, "會務運作管理")
            mem_func1_2.click()

    elif (info[i]["meet_type"] == 2 or info[i]["meet_type"] == 7):
    #理監事會
        action.move_to_element(premeet).perform()
        action.move_to_element(meet).perform()
        action.move_to_element(boardmeet).click().perform()
        add = driver.find_element(By.XPATH, '//*[@id="listForm"]/div[1]/span/input').click()
        year = driver.find_element(By.ID, 'sessionTime').send_keys(info[i]["year"])
        Num = driver.find_element(By.ID, 'sessionTime1').send_keys(info[i]["num"])
        come_date = driver.find_element(By.NAME, 'sogpBoardMeet.meetforgDate').send_keys(info[i]["come_date"])
        meet_type = Select(driver.find_element(By.ID, 'meetType')).select_by_index(1)
        meet_date = driver.find_element(By.ID, 'meetingTime').send_keys(info[i]["meet_date"])
        receive_date = driver.find_element(By.NAME, 'sogpBoardMeet.receiveDate').send_keys(info[i]["receive_date"])
        paper_num = driver.find_element(By.NAME, 'sogpBoardMeet.receiveDoc').send_keys(info[i]["number"])
        save_record = driver.find_element(By.XPATH, '//*[@id="Meet"]/div[3]/input[1]').click()
        alert = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/input')
        alert.click()
        driver.switch_to.parent_frame()
        driver.switch_to.frame("menuFrame")
        mem_func1_2 = driver.find_element(By.LINK_TEXT, "會務運作管理")
        mem_func1_2.click()
    else:
        print("meet_type should be 1,2, or 7" + "but found")
        print(info[i]["meet_type"])

'''
#章程
pre_rule = driver.find_element(By.LINK_TEXT, '團體基本資料')
rule = driver.find_element(By.XPATH, '//*[@id="menu1"]/ul/li[1]/div/ul/li[1]/a')

action.move_to_element(pre_rule).perform()
action.move_to_element(rule).click().perform()
'''

#理監事會議board_meet!list
# smallmeet = driver.find_element(By.XPATH, '/html/body/div[3]/ul/li[2]/div/ul/li[1]/div/ul/li[1]/a')
# smallmeet.click()
'''
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

'''