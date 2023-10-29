"""
File: CollectNewspaperKarel.py
Name: Rebecca
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will go outside to pick up the newspaper,
    return to its stating position,
    facing the same direction,
    and then put down the newspaper
    """
    get_newspaper()  # Karel go outside and get newspaper at (3,6)
    put_newspaper()  # Karel returns to it's starting point, facing East


def get_newspaper():
    """
    Pre-condition: Karel is at the North-west corner of the house, facing East
    Post-condition: Karel arrives at the location of the newspaper (Street 3, Avenue 6), facing East
    """
    turn_right()
    move()
    turn_left()
    move_3()  # move forwards for 3 times


def move_3():
    for i in range(3):
        move()


def turn_right():
    for i in range(3):
        turn_left()


def put_newspaper():
    """
    Pre-condition: Karel arrives at the location of the newspaper (Street 3, Avenue 6), facing East
    Post-condition: Karel returns to the North-west corner of the house, facing East. Karel put down the newspaper
    """
    pick_beeper()
    turn_around()
    move_3()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
