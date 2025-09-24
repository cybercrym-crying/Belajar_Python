import datetime

print("Masukan Tanggal Bulan Dan Tahun Lahir anda")

tanggal = int(input("Tanggal \t : "))
bulan = int(input("Bulan \t : "))
tahun = int(input("Tahun \t : "))
tanggal_lahir = datetime.date(tahun, bulan, tanggal)
print(f"Anda lahir pada \t:", tanggal_lahir)
print(f"Lahir pada hari \t: { datetime.date(tahun, bulan, tanggal):%A}")
hari_ini = datetime.date.today()
umur_hari = int((hari_ini - tanggal_lahir).days)
umur_bulan = int(umur_hari // 30)
umur_tahun = int(umur_bulan / 12)
print(f"Umur anda sekarang \t: {umur_tahun} Tahun")
print(f"Umur anda sekaran \t: {umur_bulan} Bulan")
print(f"Umur anda sekaran \t: {umur_hari} Hari")
# print(f"Umur anda sekarang \t:", umur_tahun[0:3], "Tahun")
