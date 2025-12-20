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

    call(["python", "./keywords/games/menu.py"]) if stdin in keywords["game"] else None # game

    call(["python", "./keywords/uranium.py"]) if stdin in keywords['uranium'] else None # uranium

    call(["python", "./keywords/help.py"])  if stdin in keywords['help'] else None # help

    print('you are as', lastUser["name"], 'authorized') if stdin in keywords['whoami'] else None # whoami

    print('Hi! How r u?')  if stdin in keywords['hi'] else None # hi

    print('It is', datetime.datetime.now().strftime("%H:%M")) if stdin in keywords['time'] else None # time

    call(['python', './keywords/delete.py']) if stdin in keywords['delete'] else None # delete account

    print('Today is', datetime.datetime.now().strftime("%d %B of %y")) if stdin in keywords['date'] else None # date

    os.system('clear') if stdin in keywords['clear'] else None # clear

    call(["python", "./keywords/open.py"]) if stdin in keywords['open'] else None # open

    call(["python", "./keywords/calc.py"]) if stdin in keywords['calc'] else None # calc

    if stdin == 'exit': # exit to terminal
        print("byeee")
        break
