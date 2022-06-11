# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:28:48 2022

@author: SulisSandiwarno
"""

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1]);
   mylist.append([5,6,7,8]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
mylist = [40,50,60];
mylist = [70,80,90];
changeme( mylist );
print("Values outside the function: ", mylist)