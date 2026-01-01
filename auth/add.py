import json

def addingNewUser():
    with open('./authentification/users.json', 'r') as js:
        users = json.load(js)
    name = input('\nusername: ')
    password = input('password: ')
    os = input('''0) Unix (Linux, Macos)
1) Windows\n\n
choose your operation system(01): ''')

    if os == '0':
        users[name] = {'password': password}
        with open('./authentification/users.json', 'w') as js:
            json.dump(users, js, indent = 4)
        return name
    elif os == '1':
        print("you are an idiot, that can`t use a computer\ntry again")
        addingNewUser()
    else:
        print("try again")
        addingNewUser()
