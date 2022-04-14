from microbit import *
from random import randint
from math import floor

h = 2
p = 0
r = False
f = 0
l = -30
s = 30
u = 0
c = 0

i = Image('00000:00000:00000:00000:00900')
display.show(i)

while True:
    if button_a.get_presses():
        h -= 1
        break
    elif button_b.get_presses():
        h += 1
        break

while True:
    if f-l >= s:
        l = f
        i = i.shift_down(1)
        if i.get_pixel(h, 4) == 6:
            break
        if c == 0 and f > 150:
            p += 1
            s -= s/10
        i.set_pixel(h, 4, 9)
        if c >= 3:
            c = 0
            i.set_pixel(0, 0, 6)
            i.set_pixel(1, 0, 6)
            i.set_pixel(2, 0, 6)
            i.set_pixel(3, 0, 6)
            i.set_pixel(4, 0, 6)
            i.set_pixel(randint(0, 4), 0, 0)
        else:
            c += 1
        display.show(i)
    if button_a.get_presses():
        i.set_pixel(h, 4, 0)
        h -= 1
        if h < 0:
            h = 4
        if i.get_pixel(h, 4):
            break
        i.set_pixel(h, 4, 9)
        display.show(i)
    if button_b.get_presses():
        i.set_pixel(h, 4, 0)
        h += 1
        if h > 4:
            h = 0
        if i.get_pixel(h, 4):
            break
        i.set_pixel(h, 4, 9)
        display.show(i)
    
    
    f += 1
    sleep(25)

display.show(Image("00000:09090:00000:09990:90009"))
sleep(1000)
display.scroll(str(p)+" Points")
while True:
    sleep(50)
    if button_a.is_pressed():
        display.scroll(str(p)+" Points")
    if button_b.is_pressed():
        display.scroll("Speed: "+str(floor(s)))