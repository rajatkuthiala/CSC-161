#
# CSC161 Fall 2014
#
# RAJAT KUTHIALA
#
# Chapter 3, Exercise 17
#
# Lab Section MW 6:25-7:40PM
#

import math

def main():
    value = int(input("Please enter the value "))
    guess = int(input("guess"))
     

    for i in range(guess):
        top = guess + value / guess
        final_value = float(top) / 2


    close = final_value - math.sqrt(value)
    close_two = math.sqrt(value)

    print("The guess is", final_value, "which is", close, "away from", close_two)
    return value
main()
