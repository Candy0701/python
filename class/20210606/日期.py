import datetime
now = datetime.date.today()
my_birthday = input("請輸入今年的生日日期(格式月/日/年): ")
next = datetime.datetime.strptime(my_birthday, '%m/%d/%Y').date()
diff = (next-now)
print(diff)