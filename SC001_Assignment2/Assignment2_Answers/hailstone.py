"""
File: hailstone.py
Name: Rebecca
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This function allows user to enter a positive integer.
    The number will then go through the execution of the Hailstone sequence
    """
    print('This program computes Hailstone sequences.')
    print('')
    n = int(input('Enter a number: '))
    total_steps = 0  # Create a variable to count the total steps needed to reach 1
    while True:
        if n != 1:
            total_steps += 1    # Count the total steps needed to reach 1
            if n % 2 == 0:  # If the number is even, divides it by 2
                print(str(n)+' is even, so I take half: ', end='')
                n = n // 2
                print(str(n))
            else:  # If the number is odd, times it by 3 and then plus 1
                print(str(n)+' is odd, so I make 3n+1: ', end='')
                n = 3 * n + 1
                print(str(n))
        else:  # If the number reach 1, stop the loop
            break
    print('It took ' + str(total_steps) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
