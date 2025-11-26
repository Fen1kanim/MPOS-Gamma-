import datetime
import os

# keywords
hi = ['hi', 'hello', 'hallo', 'h']
time = ['time', 'which time it is?', 'which time is it?', 'which time is it', 'which time it is', 'time?']
date = ['date', 'which date it is?', 'which date is it?', 'which date is it', 'which date it is', 'date?']
firefox = ['fire', 'firefox', 'open firefox', 'please open firefox']
steam = ['steam', 'open steam', 'please open steam']

while True: # main cycle
    stdin = input("--> ")
    [print('Hi! How r u?') for i in hi if stdin == i] # hi
    [print('It is', datetime.datetime.now().strftime("%H:%M")) for i in time if stdin == i] # time
    [print('Today is', datetime.datetime.now().strftime("%d %B of %y")) for i in date if stdin == i] # date
    [[print('No problem!'), os.system('firefox')] for i in firefox if stdin == i] # open firefox
    [[print('No problem!'), os.system('steam')] for i in firefox if stdin == i] # open steam
    [os.system('clear') if stdin == 'clear' or stdin == 'cls' else None] # clear terminal
    if stdin == 'exit': # exit to terminal
        break
    if stdin == 'calc':
        print('entered the calc mode')
        print('to exit type "exit"')
        while True:
            stdinCalc = input("(calc)--> ")
            if stdinCalc == 'exit':
                print('U went to the regural mode')
                break
