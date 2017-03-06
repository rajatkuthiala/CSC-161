#
# CSC161 Fall 2014
#
# Rajat Kuthiala
#
# Chapter 1, Exercise 5
#
# Lab Section MW 6:15-7:30PM
#


def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
	
