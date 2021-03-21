from microbit import *
compass.calibrate()

while True:
    h=compass.heading()
    if h<45 and h>314:
        display.show('N')
    elif h>=46 and h<=134:
        display.show('e')
    elif h>=135 and h<=224:
        display.show('S')
    else:
        display.show('W')