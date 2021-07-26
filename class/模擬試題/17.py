你開發了一個 Python 應用程式,其中有一個名為 month 的清單儲所有的月份的
英文。你要分割這個清單,取得由第二個月份開始,每間隔一個值的月份名稱,
你應該使用哪個程式碼?
A. month[2:2]
B. month[::2]
C. month[1::2]
D. month[1:2]
Ans:B


你設計了一個函式來執行除法,因為除法的除數不能為零,所以在函式中必須要針
對這個重點進檢查。你要如何完成這段程式碼?請在回答區擇適當的程式碼段。
def safe_divide(numerator, denominator):
 __1__
 print("你少填了被除或除数")
 __2__
 print("除数為零會産生錯誤")
 else:
 return numerator / denominator
1. ( a)
A. if numerator is None or denominator is None:
B. if numerator is None and denominator is None:
C. if numerator = None or denominator = None:
D. if numerator = None and denominator = None:
2. ( a)
A. elif denominator == 0:
B. elif denominator = 0:
C. elif denominator != 0:
D. elif denominator in 0: