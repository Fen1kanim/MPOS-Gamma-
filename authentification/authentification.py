import json
from subprocess import call

with open("authentification/users.json", "r") as js:
    users = json.load(js)

print()

name = input('Username: ')
password = input('Password: ')

if name in users:
    if password == users[name]['password']:
        print('you are as', name, 'authentificated')
        print()
    else:
        print('wrong password, try again')
        call(['python', 'authentification/authentification.py'])
else:
    print('wrong username, try again')
    call(['python', 'authentification/authentification.py'])
