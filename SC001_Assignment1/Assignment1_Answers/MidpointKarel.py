"""
File: MidpointKarel.py
Name: Rebecca
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will find the midpoint (or either of the two central corners
    if 1st Street has an even number of corners) of the 1st Street, and
    Karel will put one beeper on the midpoint.
    """
    if front_is_clear():
        put_beeper_on_both_sides()  # Set up beepers on both sides
        while not on_beeper():
            find_midpoint()  # Keep shrinking the distance between both sides through putting and picking beepers
    else:
        put_beeper()  # If this is a 1*1 world, the midpoint is at (1,1)


def put_beeper_on_both_sides():
    """
    Pre-condition: Karel is at (1,1), facing East,
    Post-condition: Karel is at the 2nd end of the 1st Street, facing West
    """
    put_beeper()  # Karel put 1 beeper at the beginning of Street 1
    move()
    if front_is_clear():  # Check if this is a 2*2 world
        while front_is_clear():
            move()
        if not front_is_clear():
            put_beeper()
            turn_around()
            move()
    else:  # If this is a 2*2 world, the midpoint is at (1,1). Karel should return to (1,1) without putting beeper
        turn_around()
        move()


def find_midpoint():
    """
    Pre-condition: Karel is at the 2nd end of the 1st Street, facing West
    Post-condition: Karel will stand on the midpoint of the 1st Street
    """
    while not on_beeper():
        move()
    if on_beeper():  # If Karel stands on beeper, it will turn around, pick beeper, and then move one step
        turn_around()
        pick_beeper()
        move()
    if not on_beeper():  # If Karel doesn't stand on beeper, it will put one beeper, and then move one step
        put_beeper()
        move()
    if on_beeper():  # Karel pickup the extra beeper and return to the midpoint
        pick_beeper()
        turn_around()
        move()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
