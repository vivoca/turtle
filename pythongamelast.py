import time
import curses
from random import randint
start = input("\n \nPlease press F11 for fullscreen! I don't care if you don't want to do this. This is not a choice of yours. PRESS F11 OR I WILL CRASH YOUR TERMINAL! Good boy! Now, you can start the game with a simple word: start. Any other words will quit.:")
score = 0

screen = curses.initscr()
screen = curses.newwin(50, 150)
screen.nodelay(1)
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

x_turtle = 1
y_turtle = 18
x_stones = [140, 110, 80, 50, 20]
y_stones = [3, 3, 3, 3, 3]
z_stones = [1, 1, 1, 1, 1]
v_stones = [1, 1, 1, 1, 1]
a_stones = [2, 4, 7, 9, 11]

curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_YELLOW)
curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_RED, curses.COLOR_RED)
screen.bkgd(" ", curses.color_pair(3))

def look_title():
    screen.addstr(0, 0, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", curses.color_pair(4))
    screen.addstr(1, 0, "!!!!!!!!!!!               !!!!   !!!!!!!   !!!!      !!!!!!               !!!!   !!!!!!!!!!!!!          !!!!!!!!           !!!!!!!!      !!!!!!!!!!!!!", curses.color_pair(4))
    screen.addstr(2, 0, "!!!!!!!!!!!!!!!!!   !!!!!!!!!!   !!!!!!!   !!!!   !!   !!!!!!!!!!   !!!!!!!!!!   !!!!!!!!!!!!!   !!!!!!!!!!!!!!!!!!!!!!!   !!!!!!!!!!!!!   !!!!!!!!!!!", curses.color_pair(4))
    screen.addstr(3, 0, "!!!!!!!!!!!!!!!!!   !!!!!!!!!!   !!!!!!!   !!!!       !!!!!!!!!!!   !!!!!!!!!!   !!!!!!!!!!!!!       !!!!!!!!!!!!!!!       !!!!!!!!!!!    !!!!!!!!!!!!", curses.color_pair(4))
    screen.addstr(4, 0, "!!!!!!!!!!!!!!!!!   !!!!!!!!!!   !!!!!!!   !!!!   !!!  !!!!!!!!!!   !!!!!!!!!!   !!!!!!!!!!!!!   !!!!!!!!!!!!!!!!!!!!!!!   !!!!!!!!!!   !!!!!!!!!!!!!!", curses.color_pair(4))
    screen.addstr(5, 0, "!!!!!!!!!!!!!!!!!   !!!!!!!!!!             !!!!   !!!!  !!!!!!!!!   !!!!!!!!!!            !!!!          !!!!!!!!           !!!   !!          !!!!!!!!!", curses.color_pair(4))
    screen.addstr(6, 0, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", curses.color_pair(4))
    screen.addstr(7, 0, "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", curses.color_pair(4))

def look_turtle():
    global x_turtle
    global y_turtle
    screen.addstr(y_turtle+0, x_turtle, " .-./*)", curses.color_pair(1))
    screen.addstr(y_turtle+1, x_turtle, "/___\/ ", curses.color_pair(1))
    screen.addstr(y_turtle+2, x_turtle, " u u   ", curses.color_pair(1))

def move_turtle():
    global x_turtle
    global y_turtle
    if event == curses.KEY_UP and y_turtle > 8:
        screen.clear()
        y_turtle=y_turtle-1
    if event == curses.KEY_DOWN and y_turtle < 40:
        screen.clear()
        y_turtle=y_turtle+1
    if event == curses.KEY_RIGHT and x_turtle < 134:
        screen.clear()
        x_turtle=x_turtle+2
    if event == curses.KEY_LEFT and x_turtle > 0:
        screen.clear()
        x_turtle=x_turtle-1

def look_stones():
    global x_stones
    global y_stones
    for i in range(0,5):
        screen.addstr(y_stones [i]+0, x_stones [i], "      ", curses.color_pair(2))
        screen.addstr(y_stones [i]+1, x_stones [i], "  KŐ  ", curses.color_pair(2))
        screen.addstr(y_stones [i]+2, x_stones [i], "      ", curses.color_pair(2))

def move_stones():
    global x_stones
    global y_stones
    global v_stones
    global z_stones
    global a_stones
    for i in range (0,5):
        if x_stones [i] > 1 :
            x_stones [i] = x_stones [i] - v_stones[i]
        if x_stones [i] <= 1 :
            x_stones [i] = 142
            y_stones [i] = randint (8, 40)
        if x_stones [i] == 142 :
            z_stones[i] = z_stones[i]+1
        if z_stones[i] == a_stones[i] and v_stones[i] < 2:
            v_stones[i] = v_stones[i]+1
        time.sleep (0.01)
        screen.clear()

def look_score():
    global score
    screen.addstr(7, 71, "Score:" + " " + str(score) + " ", curses.color_pair(4))

def change_score():
    global score
    global z_stones
    if sum(z_stones) > 10:
     score = sum(z_stones) - 10

def highscore():
    filename = "highscore.txt"
    new_score = score

    file = open(filename, "a")
    file.write(str(new_score))
    file.write("\n")
    file.close

    list = []
    print("Highscore:")
    file = open(filename, "r")
    for i, scores in enumerate(file):
        list.append(int(scores))
    list.sort()
    list.reverse()
    for i in range(0,10):
        print(str(i + 1) + ".", list[i], "\n")
    file.close

if start == "start":
    print ("\n \nAwesome. In the game you have to avoid the obstacles with a turtle. Move: Arrows. Quit: q. Good luck!")
    time.sleep (5.00)

    while True:
        look_stones ()
        look_title ()
        look_turtle ()
        look_score ()
        event = screen.getch()
        change_score ()
        move_stones ()
        move_turtle ()
        if event == ord("q"):
            break

        break_from_while = False

        for i in range(0,5):
            if abs(x_turtle - x_stones[i]) < 6 and abs(y_turtle - y_stones[i]) < 3:
                break_from_while = True
                break
        if break_from_while:
            break

    curses.endwin()
    print ("Game over!")
    print ("Your score is:", score, " ", "Congratulations!")
    highscore()
