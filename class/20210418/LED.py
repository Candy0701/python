from microbit import *
import time
hahaha = Image("09090:"
               "09090:"
               "09090:"
               "99999:"
               "09990:")
hahahi = Image("05050:"
               "05990:"
               "05090:"
               "95959:"
               "09390:")
hahaho = Image("05550:"
               "01230:"
               "04560:"
               "97959:"
               "02390:")

l=[hahaha,hahahi,hahaho]
s=0.2

while True:
    for i in l:
        display.show(i)
        time.sleep(s)

