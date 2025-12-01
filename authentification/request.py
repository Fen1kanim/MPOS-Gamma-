from subprocess import call

print('''0) add new user
1) authentificate
''')

choose = input('choose something(01): ')

if choose == '0':
    call(['python', './authentification/add.py'])
elif choose == '1':
    call(['python', './authentification/authentification.py'])
else:
    print('try again')
    call(['python', './authentification/request.py'])
