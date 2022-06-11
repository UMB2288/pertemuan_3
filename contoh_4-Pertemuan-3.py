# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:53:35 2022

@author: SulisSandiwarno
"""

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   mylist = [5,6,7,8];
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
mylist = [40,50,60];
changeme( mylist );
print("Values outside the function: ", mylist)