#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:37:49 2017

@author: radovan
"""

s = 'qlwsjgpshprtvy'

l = len(s)
max_substring = ''

for i in range(l - 1):
    substring = s[i]
    j = i + 1
    while s[j] >= s[j-1] and j < l - 1:
        substring += s[j]
        j += 1
    
    if s[j] > s[j-1]:
        substring += s[j]
        
    if len(substring) > len(max_substring):
        max_substring = substring
        
print("Longest substring in alphabetical order is:", max_substring)