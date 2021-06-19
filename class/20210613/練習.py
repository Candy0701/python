alist=[]
while True:
    name=input('輸入學生:')
    subject=input('輸入科目:')
    try:
        score=int(input('輸入成績:'))
    except:
        print('wrong')
    else:
        for i in alist:
            if name in i:
                i.append([subject , score])
                print('已經輸入了喔！')
                break
        else:
            alist.append([name, [subject , score]])
        print(alist)



