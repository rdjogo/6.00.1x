#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 09:18:56 2017

@author: radovan
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def remainBalance(n):
    '''
    n - number of months positive integer
    Returns balance after n months - a decimal
    '''    
    if n == 0:
        return balance
    else:
        return round(remainBalance(n-1)*(1 - monthlyPaymentRate)*(1 + annualInterestRate/12.0), 2)
        

print("Remaining balance:", remainBalance(12))
        
#for i in range (1,13):
#   print('Month ', i, 'Remaining balance: ',remainBalance(i))