"""
File: hangman.py
Name: Rebecca
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is a hangman game. User can input a character at each turn.
    The program will reveal the correct characters if user's guess is correct.
    User will win this game if they correctly guess all the characters within the given turns.
    """
    # Encrypted the answer with the correspond number of dashed.
    ans = random_word()
    ans_encrypted = ''
    for i in range(len(ans)):
        ans_encrypted += '-'
    print('The word looks like ' + ans_encrypted)

    # Total turns of guess granted.
    remain_turns = N_TURNS  # Change the constant into variable.
    print('You have ' + str(remain_turns) + ' wrong guess.')

    # Set up the variable to reveal partial characters if user make a correct guess.
    ans_decode = ans_encrypted

    # User can continue guessing until they have no turn left.
    while remain_turns != 0:
        # User enter a non-alphabetic input or their input contains more than 1 alphabet.
        guess = input('Your guess: ')
        if not guess.isalpha():
            print('Illegal format.')
        elif len(guess) > 1:
            print('Illegal format.')

        # User enter one character.
        else:
            guess = guess.upper()   # Change the character into uppercase.

            # Reveal partial characters if user make a correct guess.
            for i in range(len(ans)):
                ch = ans[i]
                if ch == guess:
                    ans_decode = ans_decode[:i] + guess + ans_decode[i+1:]  # Replace "-" with the correct guess.

            # Return correspond response depends on user's guess.
            if guess not in ans:    # If user make a wrong guess.
                print('There is no ' + str(guess) + '\'s in the word.')
                print('The word looks like ' + str(ans_decode))
                if remain_turns == 1:   # If user make the wrong guess with no turn left.
                    print('You are completely hung : (')
                    print('The word was: ' + str(ans))
                    break
                remain_turns = remain_turns - 1
                print('You have ' + str(remain_turns) + ' wrong guesses left.')
            else:   # If user make a correct guess.
                print('You are correct!')
                if ans_decode.find('-') == -1:  # If all the encrypted characters have been revealed.
                    print('You win!!')
                    print('The word was: ' + str(ans))
                    break
                else:
                    print('The word looks like ' + str(ans_decode))
                    print('You have ' + str(remain_turns) + ' wrong guesses left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
