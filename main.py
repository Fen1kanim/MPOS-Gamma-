import datetime
import os
import json
from subprocess import call

# opening databases
with open("keywords.json", "r") as jf:
    keywords = json.load(jf)

with open('./authentification/lastUser.json', 'r') as js:
    lastUser = json.load(js)

with open('./authentification/users.json', 'r') as js:
    users = json.load(js)
# opening authentification request
call(["python", "./authentification/request.py"])

# the main programm opens
print("print help to list comands")
print()

while True: # main cycle
    stdin = input("--> ") # as user for any commands

    [call(["python", "./python/help.py"]) if stdin == 'help' else None] # help

    [print('Hi! How r u?') for i in keywords["hi"] if stdin == i] # hi

    [print('It is', datetime.datetime.now().strftime("%H:%M")) for i in keywords["time"] if stdin == i] # time

    [print('Today is', datetime.datetime.now().strftime("%d %B of %y")) for i in keywords["date"] if stdin == i] # date
                                                                # clear 0/1
    [os.system('clear') if users[lastUser["name"]]["os"] == '0'\
    else None if stdin == 'clear' or stdin == 'cls' else None] # clear 1/1

    [call(["python", "./python/open.py"]) for i in keywords["open"] if stdin == i] # open

    [call(["python", "./python/calc.py"]) for i in keywords["calc"] if stdin == i] # calc

    if stdin == 'exit': # exit to terminal
        print("byeee")
        break
