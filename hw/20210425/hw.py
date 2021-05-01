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
