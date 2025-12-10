import math
import curses
import time
import random

MAP = [
    "111111111111111111111111111111111111111111111111111111111111111111111111",
    "1            1                                                         1",
    "1    22   1  1  111111111112211111111111111211111111111111  121   111  1",
    "1         1     1                                           121   111  1",
    "1  11111111111  1  111111112211111111111111111111111111111             1",
    "1  1         1  1  1                                     112222222211  1",
    "1  11111111  1  1  1         11111111111111122111111111  1          1  1",
    "1            1  1  11111111  1                        1  1          1  1",
    "1            1  1  1         1  111111111111122111111                  1",
    "11111111111  1  1  111  111111  1  1111111111221111111111111111111111111",
    "1         1  1  1       1       1  1                      22     1     1",
    "1  11111  1  1  111111111  111  1  1                             1  1  1",
    "1  2      1  1  1  1       111  1  11111111111111  111111111111111  1  1",
    "1  11111111  1  1  1  11111111  1  1                             1  1  1",
    "1            1  1  1  1      1  1  1111111111111111112111111  1  1  1  1",
    "1  11111211111  2  1  11111  1  2  1                          1  1  1  1",
    "1                  1         1  1  1111111111111111112111111111  1  1  1",
    "1  111111111111122111111111111  1  1                                1  1",
    "1  1                         1  2  1111111111111111112111111111111111  1",
    "1  1  111111111111111111111  1  1                                      1",
    "1  1  1          22       1  1  2  1111111111111111112111111111111111111",
    "1  1  1                      1  1                                      1",
    "1  1  1  1 1111111112111111111  1  1  1111111111111112111111111111111  1",
    "1  1  1  1 1                 1  1  1  1           22                1  1",
    "1  1  1  1    1111111111111  1  1  1                                1  1",
    "1  1  1  111  1           1  1  1  1111111111111111111111111221111  1  1",
    "1  1  1       1              1  1                                   1  1",
    "1  1  111111111111112211111111  1111112211111111111111111111111111111  1",
    "1  1                                                                   1",
    "1  111111111111111111111111111122111111111111111111111111111111111111111",
    "1                                                                      1",
    "111111111111111111111111111111111111111111111111111111111111111111111111",
]

MAP_WIDTH = len(MAP[0])
MAP_HEIGHT = len(MAP)

player_x = 3.0
player_y = 3.0
player_angle = 0.0
FOV = math.pi / 3
DEPTH = 16
SPEED = 0.1

SHADES = ['█', '▓', '▒', '░']
WALL_COLORS = [curses.COLOR_RED, curses.COLOR_GREEN, curses.COLOR_CYAN, curses.COLOR_MAGENTA]

wall_colors_map = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
column_noise = []

goal_x = 0
goal_y = 0

def initialize_wall_colors(screen_width):
    global column_noise, goal_x, goal_y
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if MAP[y][x] == '1':
                wall_colors_map[y][x] = random.randint(1, len(WALL_COLORS))
            elif MAP[y][x] == '2':
                wall_colors_map[y][x] = len(WALL_COLORS)+1  # yellow bricks
    column_noise[:] = [random.uniform(-0.5,0.5) for _ in range(screen_width*2)]
    # Random goal
    while True:
        gx = random.randint(1, MAP_WIDTH-2)
        gy = random.randint(1, MAP_HEIGHT-2)
        if MAP[gy][gx] == ' ':
            global goal_x, goal_y
            goal_x, goal_y = gx + 0.5, gy + 0.5
            break

def cast_ray(x, y, angle):
    for depth in range(1, DEPTH*10):
        tx = x + math.cos(angle) * (depth/10)
        ty = y + math.sin(angle) * (depth/10)
        map_x, map_y = int(tx), int(ty)
        if map_x < 0 or map_x >= MAP_WIDTH or map_y < 0 or map_y >= MAP_HEIGHT:
            return depth/10, 0, ' '
        # Goal check
        if abs(tx-goal_x)<0.25 and abs(ty-goal_y)<0.25:
            return depth/10, 22, 'G'
        cell = MAP[map_y][map_x]
        if cell in '12':
            return depth/10, wall_colors_map[map_y][map_x], cell
    return DEPTH, 0, ' '

def main(stdscr):
    global player_x, player_y, player_angle
    curses.curs_set(0)
    stdscr.nodelay(1)
    curses.start_color()
    height, width = stdscr.getmaxyx()
    initialize_wall_colors(width)

    for i, color in enumerate(WALL_COLORS, start=1):
        curses.init_pair(i, color, curses.COLOR_BLACK)
    curses.init_pair(len(WALL_COLORS)+1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # yellow bricks
    curses.init_pair(20, curses.COLOR_BLUE, curses.COLOR_BLACK)   # floor
    curses.init_pair(21, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # ceiling
    curses.init_pair(22, curses.COLOR_GREEN, curses.COLOR_BLACK)   # goal

    won = False
    HEIGHT_MULT = 1.8  # make walls taller
    while True:
        key = stdscr.getch()
        if key == 27: break
        elif key == ord('a'): player_angle -= 0.1
        elif key == ord('d'): player_angle += 0.1
        elif key == ord('w'):
            player_x += math.cos(player_angle)*SPEED
            player_y += math.sin(player_angle)*SPEED
            if MAP[int(player_y)][int(player_x)] in '12':
                player_x -= math.cos(player_angle)*SPEED
                player_y -= math.sin(player_angle)*SPEED
        elif key == ord('s'):
            player_x -= math.cos(player_angle)*SPEED
            player_y -= math.sin(player_angle)*SPEED
            if MAP[int(player_y)][int(player_x)] in '12':
                player_x += math.cos(player_angle)*SPEED
                player_y += math.sin(player_angle)*SPEED

        if abs(player_x-goal_x)<0.5 and abs(player_y-goal_y)<0.5:
            won = True

        for col in range(width*2):
            ray_angle = (player_angle-FOV/2) + (col/max(1,width*2))*FOV
            distance, color_pair, cell_type = cast_ray(player_x, player_y, ray_angle)
            wall_height = int(height / (distance+0.0001) * HEIGHT_MULT)
            start_row = max(0, height//2 - wall_height//2)
            end_row = min(height, height//2 + wall_height//2)
            col_pos = col//2
            if col_pos >= width: continue

            noise = column_noise[col] if cell_type=='1' else 0

            for row in range(height*2):
                try:
                    if row < start_row:
                        stdscr.addch(row, col_pos, '#', curses.color_pair(21))
                    elif row < end_row:
                        relative_pos = (row - start_row)/max(1,end_row-start_row)
                        distance_factor = (distance/DEPTH)*len(SHADES)
                        shade_index = int(relative_pos*(len(SHADES)-1)+distance_factor+noise)
                        shade_index = max(0, min(len(SHADES)-1, shade_index))
                        shade = SHADES[shade_index]
                        # Yellow bricks taller
                        if cell_type=='2':
                            if col%2==0:  # make 2-wide
                                stdscr.addch(row, col_pos, shade, curses.color_pair(color_pair))
                        elif cell_type=='G':
                            stdscr.addch(row, col_pos, '█', curses.color_pair(22) | curses.A_BOLD)
                        else:
                            stdscr.addch(row, col_pos, shade, curses.color_pair(color_pair))
                    else:
                        stdscr.addch(row, col_pos, '.', curses.color_pair(20))
                except curses.error:
                    pass

        if won:
            msg = "YOU WIN! Press ESC to exit."
            stdscr.addstr(height//2, max(0,width//2-len(msg)//2), msg, curses.A_BOLD | curses.color_pair(22))

        stdscr.refresh()
        time.sleep(0.03)

curses.wrapper(main)