#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:40:19 2017

@author: radovan
"""
s = 'azcbobobegghakl'

count = 0

for i in range(len(s) - 3):
    if s[i:i+3] == 'bob':
        count += 1
if s[-3:] == 'bob':
    count +=1
print('Number of times bob occurs is:', count)