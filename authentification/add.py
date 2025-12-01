import json
from subprocess import call

with open('./authentification/users.json', 'r') as js:
    users = json.load(js)
with open('./authentification/lastUser.json', 'r') as js:
    lastUser = json.load(js)

name = input('username: ')
password = input('password: ')
print('''0) Unix (Linux, Macos)
1) Windows
''')

os = input('choose your operation system(01): ')
if os == '1' or os == '0':
    users[name] = {"password": password, "os": os}
    del lastUser["last"]
    lastUser["last"] = {"name": name}
else:
    print("try again")
    call(['python', './authentification/add.py'])

with open('./authentification/users.json', 'w') as js:
    json.dump(users, js, indent = 4)
with open('./authentification/lastUser.json', 'w') as js:
    json.dump(lastUser, js, indent = 4)
