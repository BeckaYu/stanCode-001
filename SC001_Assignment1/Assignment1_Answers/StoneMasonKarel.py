"""
File: StoneMasonKarel.py
Name: Rebecca
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will fill all columns with beepers.
    The ending position of Karel will be on the last avenue, the 1st street, facing East
    """
    while front_is_clear():
        reach_the_top()  # go the top of a column
        check_and_put_beeper()  # fill columns with beepers
        if front_is_clear():
            move_4()  # move four times ahead
    fill_the_last_column()  # Karel fill the last column


def reach_the_top():
    """
    Pre-condition: Karel is at the bottom of a column, facing North
    Post-condition: Karel is at the top of a column, facing South
    """
    turn_left()
    move_4()
    turn_around()


def check_and_put_beeper():
    """
    Pre-condition: Karel is at the top of a column, facing South
    Post-condition: Karel is at the bottom of a column, facing East
    """
    while front_is_clear():
        fill_beeper()   # If the spot has no beeper, put one beeper
        if front_is_clear():
            move()
    fill_beeper()
    turn_left()


def move_4():
    for i in range(4):
        move()


def turn_around():
    turn_left()
    turn_left()


def fill_beeper():
    if not on_beeper():
        put_beeper()


def fill_the_last_column():
    """
    Pre-condition: Karel is at the end of the Avenue, 1st street, facing East
    Post-condition: Karel is at the end of the Avenue, 1st street, facing East, standing on a beeper
    """
    reach_the_top()
    check_and_put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
