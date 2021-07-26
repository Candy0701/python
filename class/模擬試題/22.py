你設計一個 Python 程式來檢查使用者輸入的數字是 1 位數、2 位數還是 2 位數
以上,其中規定輸入的值必須是正整數。你要如何完成這段程式碼?
num = int(input("請输入一個正整數: "))
digits = "0"
if num > 0:
 (1)
 digits = "1"
 (2)
 digits = "2"
 (3)
 digits = ">2"
 print(digits + "位數.")
elif num == 0:
 print("輸入值為 0")
else:
 print("輸入值並不是正整數")
1. (a ) A. if num < 10: B. if num < 100: C. elif num < 100: D. else:
2. (c ) A. if num < 10: B. if num < 100: C. elif num < 100: D. else:
3. (d ) A. if num < 10: B. if num < 100: C. elif num < 100: D. else: