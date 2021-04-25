import random

def roll_dice(n):
    dice=[]
    for i in range(n):
        dice.append(random.randint(1,5))
    return dice
def who_win(user,system):
    user_s = sum(user)
    print(user_s)
    system_s = sum(system)
    print(system_s)
    if user_s>system_s:
       print('user win')
    elif user_s<system_s:
        print('system win')
    else:
        print('tie')


num_dice = int(input('輸入骰次數:'))
user = roll_dice(num_dice)
system = roll_dice(num_dice)
who_win(user,system)







