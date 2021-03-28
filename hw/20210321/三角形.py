a=int(input('邊1:'))
b=int(input('邊2:'))
c=int(input('邊3:'))
if a+b>c and a+c>b and b+c>a:
    p=(a+b+c)*0.5
    area=(p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("周長=", a+b+c)
    print("面積=",area)
else:
    print("不是三角形")
