# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:32:45 2017

@author: xchen
"""

#We are going to store the output of a function (f(x)=x2) together with its input in a dictionary.
#Make a dictionary containing all squares smaller than 100.
#Print the content of this dictionary in english, e.g., "4 is the square of 2".

square={0:0}
i=0
for i in range(1,101):
    if i*i < 100:
        square.update({i:i*i})
        i+=1
print square.items()

for i in range(1,101):
    if i*i < 100:
        print '{} is the square of {}'.format(i*i,i)