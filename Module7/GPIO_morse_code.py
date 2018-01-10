#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

morse_alphabet = {
    "a": ["dot", "dash"],
    "b": ["dash", "dot", "dot", "dot"],
    "c": ["dash", "dot", "dash", "dot"],
    "d": ["dash", "dot", "dot"],
    "e": ["dot"],
    "f": ["dot", "dot", "dash", "dot"],
    "g": ["dash", "dash", "dot"],
    "h": ["dot", "dot", "dot", "dot"],
    "i": ["dot", "dot"],
    "j": ["dot", "dash", "dash", "dash"],
    "k": ["dash", "dot", "dash"],
    "l": ["dot", "dash", "dot", "dot"],
    "m": ["dash", "dash"],
    "n": ["dash", "dot"],
    "o": ["dash", "dash", "dash"],
    "p": ["dot", "dash", "dash", "dot"],
    "q": ["dash", "dash", "dot", "dash"],
    "r": ["dot", "dash", "dot"],
    "s": ["dot", "dot", "dot"],
    "t": ["dash"],
    "u": ["dot", "dot", "dash"],
    "v": ["dot", "dot", "dot", "dash"],
    "w": ["dot", "dash", "dash"],
    "x": ["dash", "dot", "dot", "dash"],
    "y": ["dash", "dot", "dash", "dash"],
    "z": ["dash", "dash", "dot", "dot"]
}

def morse_code(string):
    lowered_string = string.lower()
    for letter in lowered_string:
        if letter in morse_alphabet:
            for signal in morse_alphabet[letter]:
                if signal == "dot":
                    GPIO.output(11, True)
                    time.sleep(1)
                    GPIO.output(11, False)
                if signal == "dash":
                    GPIO.output(11, True)
                    time.sleep(3)
                    GPIO.output(11, False)
                time.sleep(1)#1 unit of time for pause between signals
            time.sleep(2)#+2 (total 3) units of time for pause between letters
        else:
            time.sleep(3)#+3 (total 6) units of time for pause between words

morse_code('Hello World')

