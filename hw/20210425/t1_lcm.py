'''
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''
a=int(input("數字1: "))
b=int(input("數字2: "))
def gcd(a,b):
    if a < b:
        temp = b
        b = a
        a = temp
    remainder = a % b
    if remainder == 0:
        return b
    else:
        return gcd(remainder,b)

def gys(a,b):
    remainder = gcd(a,b)
    print(a*b/remainder)
gys(a,b)