"""
File: rocket.py
Name: Rebecca
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This program will compose a graphic of rocket.
    The size of the graphic is determined by the constant.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    Build up the head of the rocket.
    """
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def belt():
    """
    Build up the belt of the rocket.
    """
    print('+', end='')
    for i in range(SIZE*2):
        print('=', end='')
    print('+')


def upper():
    """
    Build up the upper part of the rocket
    """
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        for j in range(i+1):
            print('/\\', end='')
        for j in range(SIZE-i-1):
            print('.', end='')
        print('|')


def lower():
    """
    Build up the lower part of the rocket.
    """
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE-i):
            print('\\/', end='')
        for j in range(i):
            print('.', end='')
        print('|')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
