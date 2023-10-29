"""
File: CheckerboardKarel.py
Name: Rebecca
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all the
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will place beepers in a checkerboard pattern:
    place one with a beeper, followed by one without a beeper.
    This function will work in any worlds.
    """
    put_beeper()  # put 1 beeper on (1,1)
    if not front_is_clear():  # if Karel is at the world with only one Avenue
        turn_left()
    while front_is_clear():
        fill_one_line()
        go_back()
        go_to_next_avenue()


def fill_one_line():
    """
    Pre-condition: Karel is at the 1st Avenue of the Street, facing East
    Post-condition: Karel is at the end of the Avenue, facing East
    """
    # Karel will place beepers in a checkerboard pattern within one line
    while front_is_clear():
        if on_beeper():
            move()
        else:
            move()
            put_beeper()


def go_back():
    """
    Pre-condition: Karel is at the end of the Avenue, facing East
    Post-condition: Karel is at Avenue 1, facing West
    """
    # Karel return to the 1st Street of the Avenue
    if not front_is_clear():
        turn_around()
    while front_is_clear():
        move()


def go_to_next_avenue():
    """
    Pre-condition: Karel is at Avenue 1, Street n, facing West
    Post-condition: Karel is at Avenue 1, Street n+1, facing East.
                    Karel will put beeper if there isn't any in the previous step.
    """
    if not front_is_clear():
        turn_right()
    if front_is_clear():
        if on_beeper():
            move()
            turn_right()
        else:
            move()
            turn_right()
            put_beeper()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
