import curses
import time
import platform
import sys

# --- SOUND SETUP ---
USE_WINSOUND = platform.system() == "Windows"
if USE_WINSOUND:
    import winsound

def sound_bounce():
    if USE_WINSOUND:
        winsound.Beep(300, 40)   # low short beep
    else:
        curses.beep()

def sound_score():
    if USE_WINSOUND:
        winsound.Beep(700, 120)  # higher, longer beep
    else:
        curses.beep()

# --- DEFAULT GAME SETTINGS ---
FPS = 30
BALL_MOVE_INTERVAL = 4
DEFAULT_PADDLE_HEIGHT = 4
DEFAULT_POINTS_TO_WIN = 5

# --- COMMAND LINE ARGUMENTS ---
try:
    POINTS_TO_WIN = int(sys.argv[1]) if len(sys.argv) >= 2 else DEFAULT_POINTS_TO_WIN
except ValueError:
    POINTS_TO_WIN = DEFAULT_POINTS_TO_WIN

try:
    PADDLE_HEIGHT = int(sys.argv[2]) if len(sys.argv) >= 3 else DEFAULT_PADDLE_HEIGHT
except ValueError:
    PADDLE_HEIGHT = DEFAULT_PADDLE_HEIGHT

# --- PONG LOGIC ---
def draw_paddle(win, x, y, color):
    for i in range(PADDLE_HEIGHT):
        win.addch(y + i, x, '|', curses.color_pair(color))

def erase_paddle(win, x, y):
    for i in range(PADDLE_HEIGHT):
        win.addch(y + i, x, ' ')

def victory_screen(stdscr, winner):
    height, width = stdscr.getmaxyx()
    stdscr.clear()

    msg1 = f"PLAYER {winner} WINS!"
    msg2 = "Press A to play again"
    msg3 = "Press ESC to quit"

    stdscr.addstr(height//2 - 1, width//2 - len(msg1)//2, msg1, curses.color_pair(4))
    stdscr.addstr(height//2 + 1, width//2 - len(msg2)//2, msg2)
    stdscr.addstr(height//2 + 3, width//2 - len(msg3)//2, msg3)

    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key in (ord('a'), ord('A')):
            return True   # restart
        if key == 27:
            return False  # quit

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    # COLORS
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)   # left paddle
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)     # right paddle
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # ball
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)    # score

    while True:
        height, width = stdscr.getmaxyx()

        # Paddle positions
        left_x = 2
        left_y = height // 2

        right_x = width - 3
        right_y = height // 2

        # Ball
        ball_x = width // 2
        ball_y = height // 2
        vel_x = 1
        vel_y = 1

        # Scores
        score_left = 0
        score_right = 0

        # Mode toggle
        two_player = False

        frame = 0
        last_time = time.time()
        frame_duration = 1 / FPS

        draw_paddle(stdscr, left_x, left_y, 1)
        draw_paddle(stdscr, right_x, right_y, 2)
        stdscr.clear()

        # --- MAIN GAME LOOP ---
        while True:
            now = time.time()
            if now - last_time < frame_duration:
                time.sleep(frame_duration - (now - last_time))
            last_time = time.time()

            # SCOREBOARD
            score_text = f"P1: {score_left} | P2: {score_right}   Mode: {'2P' if two_player else '1P'} (P to toggle)"
            stdscr.addstr(0, width//2 - len(score_text)//2, score_text, curses.color_pair(4))

            key = stdscr.getch()

            # Quit
            if key == 27:
                return

            # Toggle 2-player mode
            if key in (ord('p'), ord('P')):
                two_player = not two_player

            # Player 1 controls (arrows)
            if key == curses.KEY_UP and left_y > 1:
                erase_paddle(stdscr, left_x, left_y)
                left_y -= 1
                draw_paddle(stdscr, left_x, left_y, 1)

            if key == curses.KEY_DOWN and left_y < height - PADDLE_HEIGHT - 1:
                erase_paddle(stdscr, left_x, left_y)
                left_y += 1
                draw_paddle(stdscr, left_x, left_y, 1)

            # Player 2 or AI
            if two_player:
                if key == ord('w') and right_y > 1:
                    erase_paddle(stdscr, right_x, right_y)
                    right_y -= 1
                    draw_paddle(stdscr, right_x, right_y, 2)

                if key == ord('s') and right_y < height - PADDLE_HEIGHT - 1:
                    erase_paddle(stdscr, right_x, right_y)
                    right_y += 1
                    draw_paddle(stdscr, right_x, right_y, 2)
            else:
                # Simple AI
                erase_paddle(stdscr, right_x, right_y)
                if ball_y > right_y and right_y < height - PADDLE_HEIGHT - 1:
                    right_y += 1
                elif ball_y < right_y and right_y > 1:
                    right_y -= 1
                draw_paddle(stdscr, right_x, right_y, 2)

            # Ball movement
            if frame % BALL_MOVE_INTERVAL == 0:
                stdscr.addch(ball_y, ball_x, ' ')

                ball_x += vel_x
                ball_y += vel_y

                # Wall bounce
                if ball_y <= 1 or ball_y >= height - 2:
                    vel_y *= -1
                    sound_bounce()

                # Paddle bounces
                if ball_x == left_x + 1 and left_y <= ball_y < left_y + PADDLE_HEIGHT:
                    vel_x *= -1
                    sound_bounce()

                if ball_x == right_x - 1 and right_y <= ball_y < right_y + PADDLE_HEIGHT:
                    vel_x *= -1
                    sound_bounce()

                # Scoring
                if ball_x <= 0:
                    score_right += 1
                    sound_score()
                    ball_x = width // 2
                    ball_y = height // 2
                    vel_x = 1

                if ball_x >= width - 1:
                    score_left += 1
                    sound_score()
                    ball_x = width // 2
                    ball_y = height // 2
                    vel_x = -1

                # Victory check
                if score_left >= POINTS_TO_WIN:
                    if not victory_screen(stdscr, 1):
                        return
                    break

                if score_right >= POINTS_TO_WIN:
                    if not victory_screen(stdscr, 2):
                        return
                    break

                stdscr.addch(ball_y, ball_x, 'O', curses.color_pair(3))

            stdscr.refresh()
            frame += 1


if __name__ == "__main__":
    curses.wrapper(main)
