# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:52:17 2022

@author: SulisSandiwarno
"""

harga = int(input("masukkan harga buku = "))
jumlah = int(input("masukkan jumlah beli buku = "))
total = harga * jumlah
print("Total Belanja adalah = ", total)

if total > harga:
    print("Anda Mendapatkan Piring")
elif total > jumlah:
    print("Anda Mendapatkan Gelas")
else:
    print("Anda Titdka Mendapatkan")