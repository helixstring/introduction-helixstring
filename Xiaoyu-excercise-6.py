# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:45:43 2017

@author: xchen
"""

#k-mer counting
#(1/2)

#Remember the previous exercise of finding (unique) substrings of length 3.
#Make a function from your implementation.
#Have k as an argument to the function.
#Test the function on several input strings.
a='ABCDDCBAABCDDCBAABCDDCBATTTAAACCCTTTAAACCC'
k=3  
def kmer(a,k):
    s=set()
    for i in range(len(a)-2):
        s.add(a[i:i+k])
    print s 
kmer(a,k)
    

#(2/2)
#Modify your function to use a dictionary with substring counts.
#Use the substrings as dictionary keys.
#Use the counts as dictionary values.
#Have the function return the dictionary.
#Add a docstring to the function.
#Use the function to print k-mer counts for some strings.

b='ABCDDCBAABCDDCBAaaBccDddDDD'
k=3  
def kmer(b,k):
    """ substring as dictionary keys, counts as dictionary values."""
    d={}
    for i in range(len(b)-2):
        d.update({b[i:i+k]:b.count(b[i:i+k])})
    print d.items()
kmer(b,k)
## Awaits updating