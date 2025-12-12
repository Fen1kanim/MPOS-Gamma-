from subprocess import call
import json
import datetime
import os

#import databases
with open('keywords.json', 'r') as js:
    keywords = json.load(js)
with open('./authentification/lastUser.json', 'r') as js:
    lastUser = json.load(js)
with open('./authentification/users.json', 'r') as js:
    users = json.load(js)

#main loop
while True:
    stdin = input("--> ") # as user for any commands

    [call(["python", "./keywords/games/menu.py"]) for i in keywords["game"] if stdin == i] # game

    [call(["python", "./keywords/uranium.py"]) for i in keywords["uranium"] if stdin == i] # uranium

    [call(["python", "./keywords/help.py"]) for i in keywords["help"] if stdin == i] # help

    [print('you are as', lastUser["name"], 'authorized') for i in keywords["whoami"] if stdin == i] # whoami

    [print('Hi! How r u?') for i in keywords["hi"] if stdin == i] # hi

    [print('It is', datetime.datetime.now().strftime("%H:%M")) for i in keywords["time"] if stdin == i] # time

    [call(['python', './keywords/delete.py']) for i in keywords["delete"] if stdin == i] # delete account

    [print('Today is', datetime.datetime.now().strftime("%d %B of %y")) for i in keywords["date"] if stdin == i] # date

    [os.system('clear') for i in keywords["clear"] if stdin == i] # clear

    [call(["python", "./keywords/open.py"]) for i in keywords["open"] if stdin == i] # open

    [call(["python", "./keywords/calc.py"]) for i in keywords["calc"] if stdin == i] # calc

    if stdin == 'exit': # exit to terminal
        print("byeee")
        break
