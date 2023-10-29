"""
File: quadratic_solver.py
Name: Rebecca
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
import math


def main():
	"""
	This function will ask user for 3 inputs,
	and then return the number and the value of roots.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	d = b**2 - 4 * a * c  # Find the discriminant of the quadratic given by user
	if d < 0:
		print('No real roots')
	else:
		y = math.sqrt(d)  # Find square root of d, and assign it to variable y
		root1 = float((-b + y) / (2 * a))  # Storing one of the root to variable root1, and turns it into float
		root2 = float((-b - y) / (2 * a))  # Storing one of the root to variable root2, and turns it into float
		if d > 0:
			print('Two roots: ' + str(root1) + ', ' + str(root2))
		else:  # d = 0
			print('One root: ' + str(root1))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
