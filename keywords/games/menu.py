from subprocess import call

stdin = input('''
1. 2.5D labyrinth
2. guess a random number
3. pong
4. rock paper scissors
5. snake
6. tic tac toe
7. flappy birdo

choose a game(1234567): ''')

[call(["python", "./keywords/games/labyrinth.py"]) if stdin == "1" else None]
[call(["python", "./keywords/games/guess.py"]) if stdin == '2' else None]
[call(["python", "./keywords/games/pong.py"]) if stdin == '3' else None]
[call(["python", "./keywords/games/rps.py"]) if stdin == '4' else None]
[call(["python", "./keywords/games/snake.py"]) if stdin == '5' else None]
[call(["python", "./keywords/games/tictactoe.py"]) if stdin == '6' else None]
[call(["python", "./keywords/games/flappy_bird.py"]) if stdin == '7' else None]
