#
# CSC161 Fall 2014
#
# Rajat Kuthiala & Evan Dellavi
#
# Chapter 6, Exercise 14
#
# Lab Section MW 12:30-1:45PM
#

from math import *
import string
import os
 
inFile = open(input("Enter the file path: "),'r')
 
def toNumbers(strList):
    numList = [float(str) for str in strList]
    return numList
 
def squareEach(nums):
    squaresList = []
    for i in range(len(nums)):
        squaresList.append(nums[i]**2)
    return squaresList
 
def sumList(nums):
    sums = 0
    for i in range(len(nums)):
        sums  += nums[i]
    print(sums)
 
def main():
    sList = []
    lines = inFile.readlines()[21:56]
    for line in lines:
        sList.append(line[:2])
    numList = toNumbers(sList)
    squaresList = squareEach(numList)
    sumList(squaresList)
 
main()
inFile.close
