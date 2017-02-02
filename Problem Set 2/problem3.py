#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 20:32:12 2017

@author: radovan
"""
balance = 320000
annualInterestRate = 0.2

p_lower = balance/12
p_upper = (balance*(1 + annualInterestRate/12)**12)/12.0
p = (p_lower + p_upper)/2

def remBalance(n):
    '''
    n - number of months; a positive integer
    Returns balance after n months; a decimal
    '''
    if n == 0:
        return balance
    else:
        return round((remBalance(n-1) - p)*(1+annualInterestRate/12.0), 2)

    
while abs(remBalance(12)) > 0:
    if remBalance(12) < 0:
        p_upper = p       
    else:
        p_lower = p
    p = (p_lower + p_upper)/2
    print(p)  
        
print('Lowest Payment:', round(p,2))