import datetime

date = datetime.date(2026, 9, 30)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()



now = now.strftime("%I:%M:%S %d-%m-%Y")

target_datetime = datetime.datetime(2030, 2, 25, 12, 30, 0)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target has been passed")
else:
    print("Target date not passed")    

