
str = "00000:00000:00000:00000:00000"

#請使用list 分割及重組元素

'''
for loop show list value
"99999:00000:00000:00000:00000"  第一圈
"00000:99999:00000:00000:00000"  第二圈
"00000:00000:99999:00000:00000"  第三圈
"00000:00000:00000:99999:00000"  第四圈
"00000:00000:00000:00000:99999"  第五圈

只能用一個list個
'''
str = "00000:00000:00000:00000:00000"
str_list =str.split(':')
for i in range(len(str_list)):
    str_list[i] = '99999'
    str_list[i - 1] = '00000'
    str_ans = ':'.join(str_list)
    print(str_ans)
