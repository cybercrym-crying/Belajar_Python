data_angka = [9, 3, 4, 2, 1, 0]
print(f"data_angka : {data_angka}")

# menghitung jumlah data angka 4 di list
print(f"Jumlah angka 4 pada data : {data_angka.count(4)}")

# ambil posisi data
print(f"Angka 2 berada pada index : {data_angka.index(2)}")

# mengurutkan list
print(f"\nSebelum Sort\t : {data_angka}")
data_angka.sort()
print(f"Sesudah Sort\t : {data_angka}")

# reverse
print(f"\nSebelum Reverse\t : {data_angka}")
data_angka.reverse()
print(f"Sesudah Reverse\t : {data_angka}")
