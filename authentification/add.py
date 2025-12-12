import json
from subprocess import call

with open('./authentification/users.json', 'r') as js:
    users = json.load(js)
with open('./authentification/lastUser.json', 'r') as js:
    lastUser = json.load(js)

name = input('\nusername: ')
password = input('password: ')
os = input('''0) Unix (Linux, Macos)
1) Windows

choose your operation system(01): ''')

if os == '0':
    users[name] = {"password": password, "os": os}
    del lastUser["name"]
    lastUser["name"] = name
elif os == '1':
    print("you are an idiot, that can`t use a computer\ntry again")
    call(['python', './authentification/add.py'])
else:
    print("try again")
    call(['python', './authentification/add.py'])

with open('./authentification/users.json', 'w') as js:
    json.dump(users, js, indent = 4)
with open('./authentification/lastUser.json', 'w') as js:
    json.dump(lastUser, js, indent = 4)
