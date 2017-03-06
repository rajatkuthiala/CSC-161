#
# CSC161 Fall 2014
#
# Rajat Kuthiala        
#
# Chapter 8, Exercise 7
#
# Lab Section MW 6:15-7:30PM
#



def prime(a):
    if a < 2:
        return False
    for i in range(2,a):
        if a % i == 0:
            return False
    return True


def sum():
    a=int(input("Please enter a even number grater than 2:  "))
    if a % 2 or a < 1:                          
        print("Check Number")
    b = 3
    while a-b > 0:
        if prime(b) and prime(a-b):       
            return 'The two primes are',(b), (a-b)                 
        b+=2                                    
      
