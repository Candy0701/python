你在設計一個 Python 程式遊戲,讓參加的人從 1 到 100 間猜一個數字，最多有
三次機會。程式碼如下:
01 from random import randint
02 target = randint(1,100)
03 chance = 1
04 print("猜一個從 1 到 100 的整数。你將有 3 機會.")
05
06 guess=int(input("請输入一個整數:")
07 if guess > target:
08 print("數字太大了,低一點")
09 elif guess < target:
10 print("數字太小了,猜高一點")
11 else:
12 print("精對了!")
13
14
請將正確的程式碼片段填入 A、B、C 選項中：
A. while chance <= 3:
B. while chance < 3:
C. break
D. pass
E. chance += 1
F. while chance < 3
G. chance = 2
( a) 1.在 05 行你要使用哪個程式碼片段?
( c) 2.在 13 行你要使用哪個程式碼片段?
( d) 3.在 14 行你要使用哪個程式碼片段?