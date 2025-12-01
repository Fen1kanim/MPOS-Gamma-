import json
from subprocess import call

with open("authentification/users.json", "r") as js:
    users = json.load(js)
with open("authentification/lastUser.json", "r") as js:
    lastUser = json.load(js)
print()

name = input('Username: ')
password = input('Password: ')

if name in users:
    if password == users[name]['password']:
        print('you are as', name, 'authentificated')
        print()
        del lastUser["last"]
        lastUser["last"] = {"name": name}
        with open('./authentification/lastUser.json', 'w') as js:
            json.dump(lastUser, js, indent = 4)
    else:
        print('wrong password, try again')
        call(['python', 'authentification/authentification.py'])
else:
    print('wrong username, try again')
    call(['python', 'authentification/authentification.py'])
