import random

def guess():
    num = str(random.randint(0, 10))
    while True:
        stdin = input('guess the number: ')
        if stdin == num:
            print('the random number is',num,'!')
            break
        elif int(stdin) < int(num):
            print('the number is bigger')
        elif int(stdin) > int(num):
            print('the number is smaler')
        else:
            print('it is not a number')
