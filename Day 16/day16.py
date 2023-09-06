#import


import math
print(math.pi * 5**2)


#----------------------------------------------
from math import fsum
numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))

#----------------------------------------------

import fractions
fraction = fractions.Fraction(2.25)
print(fraction)


#-----------------------------------------------
import random as rand
print(rand.randint(1, 100))

#-----------------------------------------

import random as rand

target_number = rand.randint(1, 100)

guess = int(input("Enter a number: "))

while guess != target_number:
    print("Wrong!")
    guess = int(input("Enter a number: "))

print("You guessed correctly!")















