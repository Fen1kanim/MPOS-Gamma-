import json
from keywords.calc import calc
from keywords.delete import delete
from keywords.help import help
from keywords.uranium import uranium
from keywords.games.menu import game
from keywords.whoami import whoami
from keywords.time import time
from keywords.date import date
from keywords.clear import clear

def keywords(name):
    #import databases
    with open('keywords.json', 'r') as js:
        keywords = json.load(js)
    with open('./auth/users.json', 'r') as js:
        users = json.load(js)

    #main loop
    while True:
        stdin = input("--> ") # as user for any commands

        game() if stdin in keywords["game"] else None # game

        uranium() if stdin in keywords['uranium'] else None # uranium

        help() if stdin in keywords['help'] else None # help

        whoami(name) if stdin in keywords['whoami'] else None # whoami

        print('Hi! How r u?')  if stdin in keywords['hi'] else None # hi

        time() if stdin in keywords['time'] else None # time

        delete() if stdin in keywords['delete'] else None # delete account

        date() if stdin in keywords['date'] else None # date

        clear() if stdin in keywords['clear'] else None # clear

        open() if stdin in keywords['open'] else None # open

        calc() if stdin in keywords['calc'] else None # calc

        # unknown command
        if stdin not in keywords['game'] \
        and stdin not in keywords['uranium'] \
        and stdin not in keywords['help'] \
        and stdin not in keywords['whoami'] \
        and stdin not in keywords['hi'] \
        and stdin not in keywords['time'] \
        and stdin not in keywords['delete'] \
        and stdin not in keywords['date'] \
        and stdin not in keywords['clear'] \
        and stdin not in keywords['open'] \
        and stdin not in keywords['calc'] \
        and stdin != 'reboot' \
        and stdin != 'exit':
            print('sorry, unknown command\ntry again')
        
        if stdin == 'reboot': # reboot
            return 'r'

        if stdin == 'exit': # exit
            return 'e'
