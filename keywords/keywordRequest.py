from subprocess import call
import json
import datetime
import os

with open('keywords.json', 'r') as js:
    keywords = json.load(js)
with open('./authentification/lastUser.json', 'r') as js:
    lastUser = json.load(js)
while True:
    stdin = input("--> ") # as user for any commands

    [call(["python", "./keywords/help.py"]) if stdin == 'help' else None] # help

    [print('you are as', lastUser["name"], 'authorized') if stdin == 'whoami' else None]

    [print('Hi! How r u?') for i in keywords["hi"] if stdin == i] # hi

    [print('It is', datetime.datetime.now().strftime("%H:%M")) for i in keywords["time"] if stdin == i] # time

    [call(['python', './keywords/delete.py']) for i in keywords["delete"] if stdin == i]

    [print('Today is', datetime.datetime.now().strftime("%d %B of %y")) for i in keywords["date"] if stdin == i] # date

    [os.system('clear') if stdin == 'clear' or stdin == 'cls' else None]

    [call(["python", "./keywords/open.py"]) for i in keywords["open"] if stdin == i] # open

    [call(["python", "./keywords/calc.py"]) for i in keywords["calc"] if stdin == i] # calc

    if stdin == 'exit': # exit to terminal
        print("byeee")
        break
