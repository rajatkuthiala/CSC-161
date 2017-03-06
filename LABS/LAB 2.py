#
# CSC161 Fall 2014
#
# Rajat Kuthiala
#
# Chapter 2, Exercise 11
#
# Lab Section MW 6:16-7:30PM
#

def calculator():
    print("This is a Calculator")
    for i in range(100):
        x = input("Enter an expression to calculate: ")
        cal = eval(x)
        print(x, "=", cal)
    print()
calculator()












   


