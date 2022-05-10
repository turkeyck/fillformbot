import meetnoti_old as n_old
import meetrecord_old as old
import meetrecord_new as new

info = {
0: {"name": "新竹市陽光仁愛協會",
"come_date": "1110420", # 來文日期
"meet_date": "1110417", # 開會日期
"receive_date": "1110426", # 收文日期
"number": "1110068850", # 收文字號
"year": 15, # 屆
"num": 2, # 次
"meet_type": 1,  # 1: 會員大會, 2: 理監事, 7:理監事聯席
"data_type": 2,  # 1:會議通知, 2: 會議記錄
"time_hour": 10, # 會議時間(時)
"time_min": 10, # 會議時間(分)
"indow": "135", # 應到人數
"sdow": "72", # 實到人數
"waytou": "", # (含)委託__人數
"day_off": "", #請假人數
"start_date": "1110417", # 任期開始日期
"duration": "2", # 任期__年
"end_date": "1130416", # 任期結束日期
"place": "風采宴會館(新竹市中正路245號6樓)", # 會議地點
"staff": "李淑如",
"phone": "03-5352386#302"}
}
new_url = input("Please enter URL in new sys:")
new_acc = input("Please enter account in new sys:")
new_pw = input("Please enter password in new sys:")

old_url = input("Please enter URL in old sys:")
old_acc = input("Please enter account in old sys:")
old_pw = input("Please enter password in old sys:")
n_old.launch_old(old_url, old_acc, old_pw)
new.launch_new(new_url, new_acc, new_pw)
new.add_record(n=1, info = info)