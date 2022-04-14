from microbit import *

while True:
    sleep(50)
    i = ""
    if pin0.is_touched():
        i += '1'
    else:
        i += '0'
    if pin1.is_touched():
        i += '1'
    else:
        i += '0'
    if pin2.is_touched():
        i += '1'
    else:
        i += '0'
    if pin8.read_digital():
        i += '1'
    else:
        i += '0'
    if i == '0000':
        continue
        
    display.scroll(i)