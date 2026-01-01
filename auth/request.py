from authentification.add import addingNewUser
from authentification.authentification import auth
def request():
    print('''0) add new user
1) authentificate
''')

    choose = input('choose something(01): ')

    if choose == '0':
        return addingNewUser()
    elif choose == '1':
        return auth()
    else:
        print('try again')
        request()
