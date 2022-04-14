from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image('99999:99999:99999:99999:99999'))
        pin0.write_digital(1)
        while True:
            if not button_a.is_pressed():
                display.show(Image('00000:00000:00900:00000:00000'))
                pin0.write_digital(0)
                break