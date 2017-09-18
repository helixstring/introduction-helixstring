# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:55:19 2017

@author: xchen
"""

#FizzBuzz
# Write a program that prints the numbers from 1 to 100. 
#But for multiples of three print "Fizz" instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.


for a in range(1,101):
    if a%3 == 0 and a%5 != 0:
        print 'Fizz'
    elif a % 3 != 0 and a % 5 == 0:
        print 'Buzz'
    elif a % 3 == 0 and a % 5 == 0:
        print 'FizzBuzz'
    else:
        print a
        