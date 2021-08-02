你正在設計一個 python 程式去驗證產品編號。產品編號的格式必須為 dddddd,並且只包含數字和破折號。如果格式正確則程式必須列印 True,如果格式
不正確,則列印 False 你要如何完成這段程式碼?請在回答區選擇適當的程式碼片
段
__1__
parts = ""
__2__
 __3__
 product_no = input("輸入產品編號(dd-dddd):")
 parts = product_no.split('-')
 if len(parts) == 2:
 if len(parts[0]) == 2 and len(parts[1]) == 4:
 if parts[0].isdigit() and parts[1].isdigit():
 __(4)__
 print(valid)
1. ( ) A. product_no = "" B. product_no ="sentinel"
2. ( ) A. while product_no != "": B. while product_no != "sentinel":
3. ( ) A. valid = False B. valid = True
4. ( ) A. valid = False B. valid = True