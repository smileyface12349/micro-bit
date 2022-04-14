from microbit import *
from random import randint
from math import floor

h = 1
p = 0
r = False
f = 0
l = -25
s = 25
u = 0
g = 1
c = 3

i = Image('00000:00000:90000:00000:00000')
display.show(i)

while True:
    if button_a.get_presses() or button_b.get_presses():
        break

while True:
    if f-l >= s:
        l = f
        i = i.shift_left(1)
        if i.get_pixel(0,h) == 6:
            break
        if c == 1 and f > 90:
            p += 1
            s -= s/20
        i.set_pixel(0, h, 9)
        if c >= 2:
            c = 0
            n = randint(1, 4)
            if n == 1:
                i.set_pixel(4, 0, 0)
            else:
                i.set_pixel(4, 0, 6)
            if n in [1, 2]:
                i.set_pixel(4, 1, 0)
            else:
                i.set_pixel(4, 1, 6)
            if n in [2, 3]:
                i.set_pixel(4, 2, 0)
            else:
                i.set_pixel(4, 2, 6)
            if n in [3, 4]:
                i.set_pixel(4, 3, 0)
            else:
                i.set_pixel(4, 3, 6)
            if n == 4:
                i.set_pixel(4, 4, 0)
            else:
                i.set_pixel(4, 4, 6)
        else:
            c += 1
        display.show(i)
    if button_a.get_presses() or button_b.get_presses():
        u = f
        g = 1
        i.set_pixel(0, h, 0)
        h -= 1
        if h < 0:
            h = 0
        if i.get_pixel(0, h):
            break
        i.set_pixel(0, h, 9)
        display.show(i)
    if f-u > (s/2)*(2/g):
        u = f
        i.set_pixel(0, h, 0)
        h += 1
        g += 0.5
        if h > 4:
            break
        if i.get_pixel(0, h):
            break
        i.set_pixel(0, h, 9)
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