#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:05:07 2017

@author: radovan
"""

balance = 3926
annualInterestRate = 0.2
p = 10

def remBalance(n):
    '''
    n - number of months; a positive integer
    Returns balance after n months; a decimal
    '''
    if n == 0:
        return balance
    else:
        return round((remBalance(n-1) - p)*(1+annualInterestRate/12.0), 2)

while remBalance(12) > 0:
    p += 10
    
print('Lowest Payment:', p)