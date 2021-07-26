題目 (Ref 學生手冊 : 判斷式)
你設計了一個電影票收費的函式,票價的規則如下:
1. 5 歲以下 = 免費入場
2. 5 歲及以上的學生 = 60 元
3. 5 歲到 17 歲但不是學生 = 120 元
4. 17 歲以上但不是學生 = 180 元
你要如何完成這段程式碼?請在回答區選擇適當的程式碼片段。
def ticket_fee(age, school):
 fee = 0
 (1)
 fee = 60
 (2)
 (3)
 fee = 120
 else:
 fee = 180
 return fee
(a ) (1) A. if age >= 5 and school == True:
 B. if age >= 5 and school == False:
 C. if age <= 17
(c ) (2) A. if age >= 5 and school == True:
 B. if age >= 5 and school == False:
 C. if age <= 17
(B ) (3) A. if age >= 5 and school == True:
 B. if age >= 5 and school == False:
 C. if age <= 17
