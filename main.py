import datetime
import os
import json
from subprocess import call
with open("keywords.json", "r") as jf:
    js = json.load(jf)

print("print help to list comands")
print()

while True: # main cycle
    stdin = input("--> ")
    [call(["python", "./python/help.py"]) if stdin == 'help' else None]
    [print('Hi! How r u?') for i in js["hi"] if stdin == i] # hi
    [print('It is', datetime.datetime.now().strftime("%H:%M")) for i in js["time"] if stdin == i] # time
    [print('Today is', datetime.datetime.now().strftime("%d %B of %y")) for i in js["date"] if stdin == i] # date
    [[print('No problem!'), os.system('firefox')] for i in js["firefox"] if stdin == i] # open firefox
    [[print('No problem!'), os.system('steam')] for i in js["steam"] if stdin == i] # open steam
    [os.system('clear') if stdin == 'clear' or stdin == 'cls' else None] # clear terminal
    if stdin == 'exit': # exit to terminal
        print("byeee")
        break
    if stdin == 'calc':
        call(["python", "./python/calc.py"])
