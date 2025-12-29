import random

def rps():
    stdout = str(random.randint(0,3))
    stdin = input('''
    0. rock
    1. paper 
    2. scissors

    choose some thing(012): ''')
    print()

    # stdin == rock
    [print("I have scissors\nyou won") if stdin == '0' and stdout == '2' else None]
    [print("I have paper\nyou lose") if stdin == '0' and stdout == '1' else None]
    [print("we have the same\n") if stdin == '0' and stdout == '0' else None]
    # stdin == paper
    [print("I have scissors\nyou lose") if stdin == '1' and stdout == '2' else None]
    [print("we have the same\n") if stdin == '1' and stdout == '1' else None]
    [print("I have rock\nyou won") if stdin == '1' and stdout == '0' else None]
    # stdin == scissors
    [print("we have the same\n") if stdin == '2' and stdout == '2' else None]
    [print("I have paper\nyou won") if stdin == '2' and stdout == '1' else None]
    [print("I have rock\nyou lose") if stdin == '2' and stdout == '0' else None]
