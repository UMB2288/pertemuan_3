# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:44:37 2022

@author: SulisSandiwarno
"""

# Function definition is here
def printinfo( arg1, *tuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for variable in tuple:
      print(variable)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, 40, 30, "a" )