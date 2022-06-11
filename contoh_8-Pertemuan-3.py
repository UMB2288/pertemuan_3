# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:17:50 2022

@author: SulisSandiwarno
"""

# Function definition is here
def printinfo( gender=male, name, age = 26 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   print("Gender: ", gender)
   return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )
printinfo( name="Adi" )
#printinfo( gender="male" )