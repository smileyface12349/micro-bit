from microbit import *
from random import choice, randint
from math import floor
from radio import on, off, send, receive
from gc import collect

p = 3

display.show('A')
on()

while True:
    if button_a.get_presses():
        send('s')
        h = True
        off()
        x = randint(0, 4)
        y = 1
        s = 25
        d = choice(['NE', 'SE', 'NW', 'SW'])
        f = 0
        l = -25
        break
    elif receive() == 's':
        h = False
        break

display.show(Image("00000:00000:00000:00000:00900"))
if h:
    display.set_pixel(x, y, 8)
sleep(650)

while True:
    collect()
    if h:
        if f-l >= s:
            l = f
            display.set_pixel(x, y, 0)
            if s < 1:
                s = 1
            if d == 'NW':
                if x == 4 and y == 0:
                    if randint(1, floor(s/4)+3) == 1:
                        d = choice(['SW', 'SE'])
                        if d == 'SW':
                            t = 1
                    else:
                        t = 1
                elif y == 0:
                    if randint(1, floor(s/4)+3) == 1:
                        d = choice(['SW', 'NE', 'SE'])
                        if d == 'SW':
                            t = 1
                    else:
                        t = 1
                elif x == 4:
                    d = 'SW'
            elif d == 'NE':
                if x == 4 and y == 3:
                    if display.get_pixel(x, y+1) == 0:
                        on()
                        send('w')
                        display.show(Image('00000:09090:00000:09990:90009'))
                        break
                    d = 'SW'
                    s -= s/20
                elif y == 3:
                    if display.get_pixel(x, y+1) == 0:
                        on()
                        send('w')
                        display.show(Image('00000:09090:00000:09990:90009'))
                        break
                    d = 'NW'
                    s -= s/20
                elif x == 4:
                    d = 'SE'
            elif d == 'SE':
                if x == 0 and y == 3:
                    if display.get_pixel(x, y+1) == 0:
                        on()
                        send('w')
                        display.show(Image('00000:09090:00000:09990:90009'))
                        break
                    d = 'NW'
                    s -= s/20
                elif y == 3:
                    if display.get_pixel(x, y+1) == 0:
                        on()
                        send('w')
                        display.show(Image('00000:09090:00000:09990:90009'))
                        break
                    d = 'SW'
                    s -= s/20
                elif x == 0:
                    d = 'NE'
            else:
                if x == 0 and y == 0:
                    if randint(1, floor(s/4)+3) == 1:
                        d = choice(['NW', 'NE'])
                        if d == 'NW':
                            t = 1
                    else:
                        t = 1
                elif y == 0:
                    if randint(1, floor(s/4)+3) == 1:
                        d = choice(['NW', 'NE', 'SE'])
                        if d == 'NW':
                            t = 1
                    else:
                        t = 1
                elif x == 0:
                    d = 'NW'
                    
            try:
                t
                del t
                display.set_pixel(x, y, 0)
                if d == 'NW':
                    x = 3-x
                    d = 'SE'
                else:
                    x = 5-x
                    d = 'NE'
                h = False
                on()
                send(str(x)+'|0|'+str(f)+'|'+str(l)+'|'+str(s)+'|'+str(d))
                del x
                del y
                del f
                del l
                del s
                del d
            except:
                if d == 'NW':
                    x += 1
                    y -= 1
                elif d == 'NE':
                    x += 1
                    y += 1
                elif d == 'SE':
                    x -= 1
                    y += 1
                else:
                    x -= 1
                    y -= 1
                    
                try:
                    display.set_pixel(x, y, 8)
                except:
                    display.scroll(str(x)+','+str(y))
                    break
                    
        try:
            f += 1
        except:
            pass
                
    else:
        m = receive()
        if m == 'w':
            display.show(Image('00000:09090:00000:90009:09990'))
            break
        elif m:
            off()
            collect()
            try:
                x, y, f, l, s, d = m.split('|')
                del m
                collect()
                x = int(x)
                y = int(y)
                f = int(f)
                l = int(l)
                s = float(s)
                d = str(d)
                display.set_pixel(x, y, 8)
                h = True
            except:
                on()
            
    if button_a.get_presses():
        p -= 1
        if p < 1:
            p = 5
        display.set_pixel(0, 4, 0)
        display.set_pixel(1, 4, 0)
        display.set_pixel(2, 4, 0)
        display.set_pixel(3, 4, 0)
        display.set_pixel(4, 4, 0)
        display.set_pixel(p-1, 4, 9)
            
    elif button_b.get_presses():
        p += 1
        if p > 5:
            p = 1
        display.set_pixel(0, 4, 0)
        display.set_pixel(1, 4, 0)
        display.set_pixel(2, 4, 0)
        display.set_pixel(3, 4, 0)
        display.set_pixel(4, 4, 0)
        display.set_pixel(p-1, 4, 9)
        
    
    sleep(25)