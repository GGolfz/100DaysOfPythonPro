# Reeborg already define turn_left() and move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_set():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def play():
    i = 0
    while(i<6):
        move_set()
        i+=1
play()