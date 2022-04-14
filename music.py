from microbit import *
import music
import speech

bpm = 180

music.set_tempo(bpm=bpm)

while True:
    if button_a.is_pressed():
        display.show('A')
        music.play(['b4:2', 'C4:2', 'd:4'], pin=pin0)
        music.play(['g3:2', 'f#:2', 'g3:4'], pin=pin2)
        music.play(['G4:4'], pin=pin1)
        music.play(['d3:4'], pin=pin0, wait=False)
        sleep(5)
        music.play(['a4:4'], pin=pin1, wait=False)
        sleep(5)
        music.play(['f#4:4'], pin=pin2, wait=True)
        music.stop(pin0)
        music.stop(pin1)
        music.play(['e4:2', 'f#4:2', 'd4:4'], pin=pin0, wait=True)
        music.play(['a3:2', 'b3:2', 'c4:4'], pin=pin1, wait=True)
        music.stop(pin2)
        music.play(['e3:2', 'f#3:2'], pin=pin2, wait=True)
        music.play(['d4:4'], pin=pin1, wait=True)
        music.play(['g2:2'], pin=pin0, wait=False)
        sleep(5)
        music.play(['d3:2'], pin=pin1, wait=False)
        sleep(5)
        music.play(['c4:2'], pin=pin2, wait=True)
        music.stop(pin0)
        music.stop(pin1)
        music.play(['b4:2', 'a4:2', 'b4:2', 'g3:4'], pin=pin1)
        music.play(['g4:2', 'f#4:2', 'e4:2', 'f#4:2', 'g4:2'], pin=pin2, wait=True)
        music.play(['d4:2', 'c#4:2'], pin=pin0, wait=True)
        music.play(['f#4:2', 'g4:2'], pin=pin2, wait=True)
        music.play(['b3:2', 'a3:2'], pin=pin0, wait=True)
        music.play(['f#4:2', 'g4:2'], pin=pin2, wait=True)
        music.play(['g3:2', 'f#3:2', 'a3:2', 'c#4:2', 'e4:2', 'a5:4'], pin=pin0, wait=True)
        music.play(['f#4:2', 'd4:2', 'a3:6', 'c#4:6', 'd4:4'], pin=pin1, wait=True)
        music.play(['a3:6', 'd3:6'], pin=pin1)
        
        display.clear()