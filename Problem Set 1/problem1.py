#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:41:22 2017

@author: radovan
"""

s = 'azcbobobegghakl'

vowels = ('a','e','i','o','u')
count = 0

for i in range(len(s)):
    if s[i] in vowels:
        count += 1
        
print("Number of vowels:", count)