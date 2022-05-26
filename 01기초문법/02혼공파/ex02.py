import datetime

n = datetime.datetime.now()

# print("{}년 {}월 {}일 {}시 {}분 {}초입니다.".format(n.year,n.month,n.day,n.hour,n.minute,n.second))

if n.hour < 12:
    print("현재시각은 {}시로 오전입니다.".format(n.hour))
else:
    print("현재시각은 {}시로 오후입니다.".format(n.hour))