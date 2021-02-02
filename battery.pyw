from pynotifier import Notification
import psutil
from datetime import datetime
import json
import datetime as dt

a = 0
td = dt.time(0, 59, 00)
diff_time = dt.time(0, 20, 00)
count = 1
flag = True
day_today = datetime.today().strftime('%A')
with open("timetable.json") as con_file:
    config = json.load(con_file)
timetable = config["TimeTable"]

while True:
    x = datetime.today().replace(microsecond=0)

    # day_schedule = config["TimeTable"]
    if x.minute >= 40 and flag==True:
        flag = False
        sub = td.minute - x.minute
        diff = diff_time.minute - sub
        y = x.replace(hour=x.hour+1, minute=diff, second=x.second+00)
        a = y
        print(f"From inside loop: {a}")
    else:
        if a == 0:
            flag=False
            y = x.replace(hour=x.hour, minute=x.minute + diff_time.minute, second=x.second+00)
            a = y
            print(f"From inside loop: {a}")
            
        else:
            pass

    delta_t = a - x
    print("Difference: ", delta_t)
    secs = delta_t.seconds
    # print("Seconds remaining: ", secs)
    import time


    time.sleep(1)
    while delta_t.seconds <= 3:
        flag=True
        a = 0
        # print(f"From inner while loop: {a}")
        battery = psutil.sensors_battery()
        Notification(f" Hi! We're doing {timetable[day_today]}\n",\
                     '\n'f"Don't Forget to drink Water\nTotal glasses drank: {count}\nBattery percentage : {battery.percent}\nPower Plugged in : {battery.power_plugged}").send()
        count += 1
        break
