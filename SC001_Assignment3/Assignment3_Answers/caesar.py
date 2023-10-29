"""
File: caesar.py
Name: Rebecca
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program allows users to decipher Caesar Cipher through
    entering the secret number and encrypted strings.
    """
    secret_number = int(input('Secret number: '))
    ciphered_string = input("What's the ciphered string?")
    print('The deciphered string is: ' + str(find_ans(secret_number, ciphered_string)))


def find_ans(secret_number, ciphered_string):
    """
    :param secret_number: int, the secret number of the ciphered string.
    :param ciphered_string: str, the ciphered string.
    :return: str, the deciphered Caesar Cipher.
    """
    ciphered_string = ciphered_string.upper()   # Change user's input into upper cases.
    ans = ""    # Start with an empty string.

    # Identify the location of each character of ciphered_string in ALPHABET.
    for i in range(len(ciphered_string)):
        ch = ciphered_string[i]
        ch_number = ALPHABET.find(ch)

        # Decipher the encrypted strings.
        if ch_number >= 0:  # If the character is an alphabet.
            # Identify the real location of the alphabet.
            if ch_number + secret_number >= 26:
                ch_number += secret_number - 26
            else:
                ch_number += secret_number
            ans += ALPHABET[ch_number]  # Composed the answers with the encrypted locations of alphabets.
        else:
            if ch == ' ':
                ans += ' '
            if ch == '!':
                ans += '!'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
