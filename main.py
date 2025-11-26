import datetime
import os

hi = ['hi', 'hello', 'hallo', 'h']
time = ['time', 'which time it is?', 'which time is it?', 'which time is it', 'which time it is', 'time?']
date = ['date', 'which date it is?', 'which date is it?', 'which date is it', 'which date it is', 'date?']
firefox = ['fire', 'firefox', 'open firefox', 'please open firefox']
while True:
    stdin = input("--> ")
    [print('Hi! How r u?') for i in hi if stdin == i]
    [print('It is', datetime.datetime.now().strftime("%H:%M")) for i in time if stdin == i]
    [print('Today is', datetime.datetime.now().strftime("%d %B of %y")) for i in date if stdin == i]
    [[print('No problem!'), os.system('firefox')] for i in firefox if stdin == i]
    [os.system('clear') if stdin == 'clear' or stdin == 'cls' else None]
    if stdin == 'exit':
        break
    if stdin == 'calc':
        print('entered the calc mode')
        print('to exit type "exit"')
        while True:
            stdinCalc = input("(calc)--> ")
            if stdinCalc == 'exit':
                print('U went to the regural mode')
                break
