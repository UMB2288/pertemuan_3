# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 16:19:12 2022

@author: SulisSandiwarno
"""

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')