# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# This is Xiaoyu Chen's submission for question 1 18-09-17

a=range(0,10)
b=a.reverse()
for i in a:
    if i>0 :
        print '{} bottles of beer on the wall, {} bottles of beer. Take one down and pass it around, {} bottles of beer on the wall'.format(i,i,i-1)
    else:
        print 'No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.'
    
    
###output:
###9 bottles of beer on the wall, 9 bottles of beer. Take one down and pass it around, 8 bottles of beer on the wall
###8 bottles of beer on the wall, 8 bottles of beer. Take one down and pass it around, 7 bottles of beer on the wall
###7 bottles of beer on the wall, 7 bottles of beer. Take one down and pass it around, 6 bottles of beer on the wall
###6 bottles of beer on the wall, 6 bottles of beer. Take one down and pass it around, 5 bottles of beer on the wall
###5 bottles of beer on the wall, 5 bottles of beer. Take one down and pass it around, 4 bottles of beer on the wall
###4 bottles of beer on the wall, 4 bottles of beer. Take one down and pass it around, 3 bottles of beer on the wall
###3 bottles of beer on the wall, 3 bottles of beer. Take one down and pass it around, 2 bottles of beer on the wall
###2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottles of beer on the wall
###1 bottles of beer on the wall, 1 bottles of beer. Take one down and pass it around, 0 bottles of beer on the wall
###No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.