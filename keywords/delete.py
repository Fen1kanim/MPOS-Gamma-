import json

with open('./authentification/lastUser.json', 'r') as js:
    lastUser = json.load(js)
with open('./authentification/users.json', 'r') as js:
    users = json.load(js)

del users[lastUser["name"]]

with open('./authentification/users.json', 'w') as js:
    json.dump(users, js, indent = 4)
