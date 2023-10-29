"""
File: prime_checker.py
Name: Rebecca
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ”Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    This program asks our user for input and
    checks if the input is a prime number or not.
    """
    print('Welcome to the prime checker!')
    while True:
        n = int(input('n: '))
        if n == EXIT:  # If user enter the EXIT value, this program will stop.
            print('Have a good one!')
            break
        else:
            # Check if there is any factor exist. Start from "user's input minus one" to "2".
            factor_test = n - 1
            while factor_test >= 2:
                if n % factor_test != 0:
                    factor_test -= 1
                else:  # User find a factor other than their input or 2.
                    print(str(n) + ' is not a prime number.')
                    break
            if factor_test == 1:  # User's input is 2 OR User cannot find a factor other than user's input or 2.
                print(str(n) + ' is a prime number.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
