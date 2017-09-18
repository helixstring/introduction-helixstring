# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:58:25 2017

@author: xchen
"""
# Print all suffixes of the repeat structure.
repeat1= 'ACGT'*3+'TTATT'*5
repeat1
len(repeat1)
i=0
while i< len(repeat1)+1:
    print repeat1[i:]
    i+=1
 # Print all substrings of length 3.
for i in range(len(repeat1)-2):
    print repeat1[i:i+3]
#Print all unique substrings of length 3.
s=set()
for i in range(len(repeat1)-2):
    s.add(repeat1[i:i+3])
print s

    
    
