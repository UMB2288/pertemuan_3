# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 11:18:59 2022

@author: SulisSandiwarno
"""

total = 5; 

def sum( arg1, arg2 ):

    total = arg1 + arg2; 
    print("Inside the function local total : ", total)
    return total;

#def min():
    

    sum( 10, 20 );
print("Outside the function global total : ", total)