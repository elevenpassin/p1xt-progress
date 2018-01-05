"""
Problem Set 0

Read in two numbers then print out the first raised to the power of the second, and on the next line
print the log base 2 of the first.
"""

import math

X = int(input("Enter number x: "))
Y = int(input("Enter number y: "))
print("x**y = " + str(X**Y))
print("log(x) = " + str(math.log2(X)))
