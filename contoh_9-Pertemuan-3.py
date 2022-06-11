# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 10:37:35 2022

@author: SulisSandiwarno
"""

def printinfo( variabel ):
   "This prints a passed info into this function"
   variabel = "coba"
   return variabel

variabel = "latihan"
print(variabel)

variabel = printinfo ( variabel )
print( variabel )
  