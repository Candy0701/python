'''
電影分及制:讓使用者輸入
年齡18歲以上，顯示為"限制級"
年齡13歲以上但不滿18歲，顯示為"輔導級"
年齡12歲以下，顯示為"普通級"
其他則是，顯示"未知"
'''
a=int(input('輸入年齡:'))
if a>=18:
    print('限制級')
elif a>13 and a<18:
    print('輔導級')
elif a<12:
    print('普級')
else:
    print('不知')