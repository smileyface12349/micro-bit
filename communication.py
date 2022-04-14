from microbit import *
from radio import send, receive, on, config

config(channel=69, power=7)
on()
face_down = False
t = ""
message = '-'

while True:
    sleep(100)
    a = button_a.get_presses()
    b = button_b.get_presses()
    m = receive()
    if m:
        if m == '!':
            send('r!')
            for x in range(5):
                display.show(Image('99999:99999:99999:99999:99999'))
                sleep(100)
                display.clear()
                sleep(100)
            del x
            message = '!'
            t += m
        else:
            if len(m) == 1:
                send('r'+m)
                display.show(m)
                sleep(1000)
                display.clear()
                message = m
                t += m
        continue
            
    if accelerometer.was_gesture('face down'):
        display.show(Image('99999:99999:99999:99999:99999'))
        sleep(100)
        display.clear()
        face_down = True
    if accelerometer.was_gesture('face up') and face_down:
        display.show(message)
        sleep(1000)
        display.clear()
        face_down = False
        continue
    if face_down and a: 
        face_down = False
        if len(t) == 0:
            display.show('-')
            sleep(500)
            display.clear()
        else:
            display.scroll(t)
        continue
            
    if accelerometer.was_gesture('shake'):
        display.show('_')
        while True:
            if button_a.get_presses():
                send('_')
                sleep(50)
                if receive() == 'r_':
                    display.show(Image('00000:00000:00000:00000:09990'))
                    sleep(300)
                    display.show(Image('00000:00000:00000:00000:00900'))
                    sleep(300)
                else:
                    display.clear()
                break
            elif button_b.get_presses():
                break
        display.clear()
        continue
    if a and b:
        first = '+'
    elif a:
        first = 'A'
    elif b:
        first = 'B'
    elif pin0.is_touched():
        first = '0'
    elif pin1.is_touched():
        first = '1'
    elif pin2.is_touched():
        first = '2'
    else:
        continue
        
    display.show(first)
        
    while True:
        a = button_a.get_presses()
        b = button_b.get_presses()
        if a:
            second = 'A'
        elif b:
            second = 'B'
        elif pin0.is_touched():
            second = '0'
        elif pin1.is_touched():
            second = '1'
        elif pin2.is_touched():
            second = '2'
        else:
            continue
           
        
        if first == 'A':
            if second == 'A':
                char = 'A'
            elif second == 'B':
                char = 'C'
            elif second == '0':
                char = 'D'
            elif second == '1':
                char = 'E'
            else:
                char = 'F'
        if first == 'B':
            if second == 'A':
                char = 'G'
            elif second == 'B':
                char = 'B'
            elif second == '0':
                char = 'H'
            elif second == '1':
                char = 'I'
            else:
                char = 'J'
        elif first == '0':
            if second == 'A':
                char = 'K'
            elif second == 'B':
                char = 'L'
            elif second == '1':
                char = 'M'
            elif second == '0':
                continue
            else:
                char = 'N'
        elif first == '1':
            if second == 'A':
                char = 'O'
            elif second == 'B':
                char = 'P'
            elif second == '0':
                char = 'Q'
            elif second == '1':
                continue
            else:
                char = 'R'
        elif first == '2':
            if second == 'A':
                char = 'S'
            elif second == 'B':
                char = 'T'
            elif second == '0':
                char = 'U'
            elif second == '2':
                continue
            else:
                char = 'V'
        elif first == '+':
            if second == 'A':
                char = 'W'
            elif second == 'B':
                char = 'X'
            elif second == '0':
                char = 'Y'
            elif second == '1':
                char = 'Z'
            else:
                char = '!'
                
        display.show(char)
       
        while True:
           if button_a.get_presses():
               send(char)
               i = Image('99999:99999:99999:99999:99999')
               display.show(i)
               sleep(125)
               if receive() == 'r'+char:
                   c = 0
                   while True:
                       c += 1
                       if c == 1:
                           i.set_pixel(0, 0, 0)
                       elif c == 2:
                           i.set_pixel(1, 0, 0)
                       elif c == 3:
                           i.set_pixel(2, 0, 0)
                       elif c == 4:
                           i.set_pixel(3, 0, 0)
                       elif c == 5:
                           i.set_pixel(4, 0, 0)
                       elif c == 6:
                           i.set_pixel(4, 1, 0)
                       elif c == 7:
                           i.set_pixel(4, 2, 0)
                       elif c == 8:
                           i.set_pixel(4, 3, 0)
                       elif c == 9:
                           i.set_pixel(4, 4, 0)
                       elif c == 10:
                           i.set_pixel(3, 4, 0)
                       elif c == 11:
                           i.set_pixel(2, 4, 0)
                       elif c == 12:
                           i.set_pixel(1, 4, 0)
                       elif c == 13:
                           i.set_pixel(0, 4, 0)
                       elif c == 14:
                           i.set_pixel(0, 3, 0)
                       elif c == 15:
                           i.set_pixel(0, 2, 0)
                       elif c == 16:
                           i.set_pixel(0, 1, 0)
                       elif c == 17:
                           i.set_pixel(1, 1, 0)
                       elif c == 18:
                           i.set_pixel(2, 1, 0)
                       elif c == 19:
                           i.set_pixel(3, 1, 0)
                       elif c == 20:
                           i.set_pixel(3, 2, 0)
                       elif c == 21:
                           i.set_pixel(3, 3, 0)
                       elif c == 22:
                           i.set_pixel(2, 3, 0)
                       elif c == 23:
                           i.set_pixel(1, 3, 0)
                       elif c == 24:
                           i.set_pixel(1, 2, 0)
                       elif c == 25:
                           i.set_pixel(2, 2, 0)
                       else:
                           del c
                           break
                       
                       sleep(25)
                       display.show(i)
               else:
                   display.clear()
               break
           elif button_b.get_presses():
               display.clear()
               break
               
        break          