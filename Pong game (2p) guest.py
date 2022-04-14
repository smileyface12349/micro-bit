from microbit import *
from random import choice, randint
from math import floor
from radio import on, off, send, receive

p = 3
display.show(Image("00000:00000:00000:00000:00900"))
sleep(500)

h = False

while True:
    if h:
        if f-l >= v[0]: # need to move the ball
            l = f
            display.set_pixel(x, y, 0)
            if v[0] < 1:
                v[0] = 1
            if v[1] == 'NW': # up right
                if x == 4 and y == 0: # top right pixel
                    v[1] = 'SW'
                    x = 5-x
                    s = 1
                elif y == 0: # hit the top
                    if randint(1, floor(v[0]/4)+2) == 1:
                        v[1] = 'SW'
                        x = 5-x
                        s = 1
                    x = 3-x
                    s = 1
                elif x == 4: # hit the right
                    v[1] = 'SW'
            elif v[1] == 'NE': # down right
                if x == 4 and y == 3: # bottom right pixel
                    if display.get_pixel(x, y+1) == 0: # game over
                        send('w')
                        display.show(Image('00000:09090:00000:09990:90009'))
                        break
                    v[1] = 'SW'
                    v[0] -= v[0]/10
                    s += 1
                elif y == 3: # hit the bottom
                    if display.get_pixel(x, y+1) == 0: # game over
                        send('w')
                        display.show(Image('00000:09090:00000:09990:90009'))
                        break
                    v[1] = 'NW'
                    v[0] -= v[0]/10
                    s += 1
                elif x == 4: # hit the right
                    v[1] = 'SE'
            elif v[1] == 'SE': # down left
                if x == 0 and y == 3: # bottom left pixel
                    if display.get_pixel(x, y+1) == 0: # game over
                        send('w')
                        display.show(Image('00000:09090:00000:09990:90009'))
                        break
                    v[1] = 'NW'
                    v[0] -= v[0]/10
                    s += 1
                elif y == 3: # hit the bottom
                    if display.get_pixel(x, y+1) == 0: # game over
                        send('w')
                        display.show(Image('00000:09090:00000:09990:90009'))
                        break
                    v[1] = 'SW'
                    v[0] -= v[0]/10
                    s += 1
                elif x == 0: # hit the left
                    v[1] = 'NE'
            else: # SW: up left
                if x == 0 and y == 0: # top left pixel
                    v[1] = 'NW'
                    x = 3-x
                    s = 1
                elif y == 0: # hit the top
                    if randint(1, floor(v[0]/4)+2) == 1:
                        v[1] = 'NW'
                        x = 3-x
                        s = 1
                    x = 5-x
                    s = 1
                elif x == 0: # hit the left
                    v[1] = 'NW'
                    
            if s:
                s = 0
                h = False
                send(str(x)+'|0|'+str(f)+'|'+str(l)+'|'+str(v))
                
            if v[1] == 'NW':
                x += 1
                y -= 1
            elif v[1] == 'NE':
                x += 1
                y += 1
            elif v[1] == 'SE':
                x -= 1
                y += 1
            else:
                x -= 1
                y -= 1
                
            try:
                display.set_pixel(x, y, 8)
            except:
                display.scroll(str(x)+", "+str(y))
                break
    else:
        m = receive()
        if m == 'w':
            display.show(Image('00000:09090:00000:90009:09990'))
            break
        elif m:
            h = True
            m = m.split('|')
            x = int(m[0])
            y = int(m[1])
            f = int(m[2])
            l = int(m[3])
            v = eval(m[4])
            display.set_pixel(x, y, 8)
            
    if button_a.get_presses():
        p -= 1
        if p < 1:
            p = 5
        if p == 1:
            display.set_pixel(0, 4, 9)
            display.set_pixel(1, 4, 0)
            display.set_pixel(2, 4, 0)
            display.set_pixel(3, 4, 0)
            display.set_pixel(4, 4, 0)
        elif p == 2:
            display.set_pixel(0, 4, 0)
            display.set_pixel(1, 4, 9)
            display.set_pixel(2, 4, 0)
            display.set_pixel(3, 4, 0)
            display.set_pixel(4, 4, 0)
        elif p == 3:
            display.set_pixel(0, 4, 0)
            display.set_pixel(1, 4, 0)
            display.set_pixel(2, 4, 9)
            display.set_pixel(3, 4, 0)
            display.set_pixel(4, 4, 0)
        elif p == 4:
            display.set_pixel(0, 4, 0)
            display.set_pixel(1, 4, 0)
            display.set_pixel(2, 4, 0)
            display.set_pixel(3, 4, 9)
            display.set_pixel(4, 4, 0)
        elif p == 5:
            display.set_pixel(0, 4, 0)
            display.set_pixel(1, 4, 0)
            display.set_pixel(2, 4, 0)
            display.set_pixel(3, 4, 0)
            display.set_pixel(4, 4, 9)
            
    elif button_b.get_presses():
        p += 1
        if p > 5:
            p = 1
        if p == 1:
            display.set_pixel(0, 4, 9)
            display.set_pixel(1, 4, 0)
            display.set_pixel(2, 4, 0)
            display.set_pixel(3, 4, 0)
            display.set_pixel(4, 4, 0)
        elif p == 2:
            display.set_pixel(0, 4, 0)
            display.set_pixel(1, 4, 9)
            display.set_pixel(2, 4, 0)
            display.set_pixel(3, 4, 0)
            display.set_pixel(4, 4, 0)
        elif p == 3:
            display.set_pixel(0, 4, 0)
            display.set_pixel(1, 4, 0)
            display.set_pixel(2, 4, 9)
            display.set_pixel(3, 4, 0)
            display.set_pixel(4, 4, 0)
        elif p == 4:
            display.set_pixel(0, 4, 0)
            display.set_pixel(1, 4, 0)
            display.set_pixel(2, 4, 0)
            display.set_pixel(3, 4, 9)
            display.set_pixel(4, 4, 0)
        elif p == 5:
            display.set_pixel(0, 4, 0)
            display.set_pixel(1, 4, 0)
            display.set_pixel(2, 4, 0)
            display.set_pixel(3, 4, 0)
            display.set_pixel(4, 4, 9)
    
    f += 1
    sleep(25)