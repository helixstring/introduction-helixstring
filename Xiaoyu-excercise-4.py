# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:25:12 2017

@author: xchen
"""

#Calculate all coordinates of the line x=y with x < 100.
#Note: This is the sequence (0, 0), (1, 1), ... (99, 99)

coord={0:0}
for i in range(101):
    coord.update ({i:i})
print coord.items()
