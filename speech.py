from microbit import *
import speech
import music

p2 = ['b4:2', 'c4b:2', 'd4:4', 'g3:2', 'f3:2', 'g3:4', 'g4b:4', 'f4#:4', 'e4:2', 'f4:2', 'd4:4', 'f3:2', 'e3:2', 'f3:4', 'd4:4', 'c4:2', 'b4:2', 'a4:2', 'b4:2', 'g3:4', 'g4:2', 'f4#:2',
'e4:2' 'f4#:2', 'g4:2', 'd4:2', 'c4#:2', 'f4#:2', 'g', 'b', 'a', 'f#', 'g', 'g3', 'f', 'a4', 'c#', 'e', 'a5:4','f4#:2', 'd4', 'a:6', 'c#', 'd4:4', 'a4:6', 'd3:6']

while True:
    if button_a.is_pressed():
        music.play(p2, pin=pin1, wait=False)
        sleep(1000)
        speech.say("Hello I am a computer that speaks through a passive buzzer")
        sleep(1000)