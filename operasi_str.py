# operasi dan manipulasi str

# 1. menyambung str
namaawal = "ali"
namaakhir = "ismul"

nama_lengkap = namaawal + " " + namaakhir

# 2. menghitung panjang str

panjang = len(nama_lengkap)
print("panjang karakter nama_lengkap : " + nama_lengkap + " " + str(panjang))

# 3. operator untuk str
# mengecek apakah ada komponen char atau str di string

a = "a"
status = a in nama_lengkap
print("string " + a + " ada di " + nama_lengkap + " : " + str(status))
a = "A"
status = a not in nama_lengkap
print("string " + a + " tidak ada di " + nama_lengkap + " : " + str(status))

# mengulang str
print("str " * 10)

# index
print("index ke-2 : " + nama_lengkap[2])  # positif mengambil dari depan
print("index ke-(-2) : " + nama_lengkap[-2])  # negatif mengambil dari belakang
print("index ke-(0-3) : " + nama_lengkap[0:3])  # akan mengambil dari index 0 - 2
print(
    "index ke-(0,2,4,6,8) : " + nama_lengkap[0:9:2]
)  # akan mengambil sesuai dengan masukan batas panjang dan index tertentu

# item paling kecil pada huruf
print("paling kecil : " + min(nama_lengkap))
# item paling besar pada huruf
print("paling besar : " + max(nama_lengkap))
ascii = ord("d")
print("ASCII CODE dari : " + str(ascii))
data = 100
print("char untuk dari ASCII CODE 100: " + chr(data))

# 4. operator dalam bentuk method

data = "alijandro"
jumlah = data.count("a")
print("jumlah a pada alijandro :", jumlah)
