"""
File: complement.py
Name: Rebecca
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    This program helps find the complement
    strand of a DNA sequence.
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    """
    This function will return the complement of the DNA sequence.
    - 'A' and 'T' are complements for each other
    - 'C' and 'G' are complements for each other
    - If no dna data exists, the function will return 'DNA strand is missing.'
    """
    ans = ""    # Start with an empty string.
    if dna == '':   # If dna data is empty, returns 'DNA strand is missing.'
        ans += 'DNA strand is missing.'
    else:
        for i in range(len(dna)):   # Look through dan data and find its complement.
            ch = dna[i]
            if ch == 'A':
                ans += 'T'
            elif ch == 'T':
                ans += 'A'
            elif ch == 'C':
                ans += 'G'
            elif ch == 'G':
                ans += 'C'
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
