import json

def auth():
    with open("authentification/users.json", "r") as js:
        users = json.load(js)
    print()

    while True:
        name = input('Username: ')
        password = input('Password: ')

        if name in users and password == users[name]["password"]:
            print('you are as', name, 'authentificated\n')
            return name
        else:
            print('wrong password or username, try again')
