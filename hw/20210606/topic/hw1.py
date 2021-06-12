'''
學校提供分數等第查尋，讓使用都輸入分數
90分以上含90為優等
80-89輸出為甲等
70-79輸出為乙等
60-69輸出為丙等
59以下輸出為不及格
請寫出以上程式
'''
a=int(input('輸入考試成績:'))
if a>=90:
    print('優等')
elif a>80 and a<89:
    print('甲等')
elif a>70 and a<79:
    print('乙等')
elif a>60 and a<69:
    print('丙等')
else:
    print('沒有及格')