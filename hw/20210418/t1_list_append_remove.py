'''
讓使用者輸入一個str，當str有在list裡面，就移除該str
沒有str就加入list, 並顯示最後的list，list初使值為
["apple", "ball" ,"car"]
'''
l=['糖果' '冰棒' '蘋果']
a=int(input('輸入一樣東西:'))
for i in l:
    if i =='input':
        l.remove(i)
    else:
        l.append(i)
print(l)