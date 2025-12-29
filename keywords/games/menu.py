from subprocess import call
from keywords.games.guess import guess
from keywords.games.rps import rps

def game():
    stdin = input('''
0. 2.5D labyrinth
1. guess a random number
2. pong
3. rock paper scissors
4. snake
5. tic tac toe\n
choose a game(012345): ''')

    call(['python', './keywords/games/labyrinth']) if stdin == '0' else None
    guess() if stdin == "1" else None
    call(["python", "./keywords/games/pong.py"]) if stdin == '2' else None
    rps() if stdin == '3' else None
    call(["python", "./keywords/games/snake.py"]) if stdin == '4' else None
    call(["python", "./keywords/games/tictactoe.py"]) if stdin == '5' else None
