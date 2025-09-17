
# merubah semua ke upper case

salam = "bro"

print(salam)
salam = salam.upper()
print(salam)

nama = "RRRRR"
print(nama)
print(nama.lower())

# pengecekan dengan is

# contoh pengecekan lower case

test = "sis"
print("apakah lower sis :", test.islower())
print("apakah upper sis :", test.isupper())

# isalpha() cek semua apakah huruf
# isalnum() cek semua huruf dan angka
# usdecimal() cek semua angka
# isspace() cek semua spasi tab newline
# istitle() cek semua kata dimulai huruf besar

cekalpha = "aisu33"
print(cekalpha.isalpha())
cekalnum = "cek233"
print(cekalnum.isalnum())
cekdecimal = "2334"
print(cekdecimal.isdecimal())
cekspace = " "
print(cekspace.isspace())
cektitle = "Titanic It's"
print(cektitle.istitle())

# cek komponen starswith() endswith()
cekstar = "Zidan Kadir".startswith("Zidan")
print(cekstar)  # di cek awalan apakah "Zidan"
cekend = "Dea Ananda".endswith("Ananda")
print(cekend)  # di cek akhiran apakah "Ananda"

# penggabungan komponen join() and split()
kumpulankata = ["aku", "mau", "makan"]
gabung = " ".join(kumpulankata)
print(kumpulankata)
print(gabung)
gabung = "akuhasukahajoget"
print(gabung.split("ha"))

# alokasi karakter rjust() ljust() center()
kanan = "kanan".rjust(10)  # memberikan space sebanyak 10 dari depan
print("'" + kanan + "'")
kiri = "kiri".ljust(10)  # memberikan space sebanyak 10 dari belakang
print("'" + kiri + "'")
tengah = "tengah".center(10, "s")
print("'" + tengah + "'")
tengah = tengah.strip("s")  # menghilangkan sebuah karakter
print(tengah)

perubahan = "cita cita saya jadi pilot"
print(perubahan)
print(perubahan.replace("pilot", "cybersecurity"))
