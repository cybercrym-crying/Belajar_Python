"""
# ++++++++3-----------10++++++++

inputuser = float(input("masukan angka yang 3< dan >10:"))
hasil = (inputuser < 3) or (inputuser > 10)
print(hasil)

# --------3+++++++++++10--------

inputuser = float(input("masukan angka yang >3 dan <10:"))
a = inputuser < 10
b = inputuser > 3
hasil = (inputuser > 3) and (inputuser < 10)
print(hasil)
"""

# PR
# SOAL 1 ---------0++++++++5-------8++++++++11------
inputuser = int(input("MASUKAN ANGKA "))
hasil = inputuser > 0 and inputuser < 5 or inputuser > 8 and inputuser < 11
print(hasil)
# SOAL 2 +++++++++0--------5+++++++8--------11++++++
inputuser = int(input("MASUKAN ANGKA "))
hasil = inputuser < 0 or inputuser > 5 and inputuser < 8 or inputuser > 11
print(hasil)
