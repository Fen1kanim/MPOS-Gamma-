import json
from subprocess import call

with open('./authentification/users.json', 'r') as js:
    users = json.load(js)

name = input('username: ')
password = input('password: ')
print('''0) Unix (Linux, Macos)
1) Windows
''')

os = input('choose your operation system(01): ')
if os == '1' or os == '0':
    users[name] = {"password": password, "os": os}
else:
    print("try again")
    call(['python', './authentification/add.py'])

with open('./authentification/users.json', 'w') as js:
    json.dump(users, js, indent = 4)
