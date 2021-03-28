a=int(input('輸入數字:'))
total=0
if a>1:
    for i in range(1,a+1):
        total+=i
    print(total)
else:
    print('error')