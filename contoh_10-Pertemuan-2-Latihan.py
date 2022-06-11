# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 14:52:17 2022

@author: SulisSandiwarno
"""

absen = int(input("masukkan nilai absen = "))
tugas = int(input("masukkan nilai tugas = "))
uts = int(input("masukkan nilai uts = "))
uas = int(input("masukkan nilai uas = "))

akhir = (absen*0.1) + (tugas*0.2) + (uts*0.3) + (uas*0.4)
print("Nilai Akhir Adalah = ", akhir)

if akhir >= 80 <=100 :
    print("Anda Mendapatkan A")
elif akhir >= 70 <= 79:
    print("Anda Mendapatkan B")
elif akhir >= 60 <= 69:
    print("Anda Mendapatkan C")
elif akhir >= 50 <= 59:
    print("Anda Mendapatkan D")
else:
    print("Anda Tidak Lulus")