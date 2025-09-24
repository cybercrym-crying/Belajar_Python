harga_tiket = float(50000)
print(15 * "=" + "[LOKET TIKET WAHANA HANTU]" + 15 * "=" + "\n")
tiket_dibeli = int(input("Masukan Jumlah Tiket Yang Di Beli : "))
tiket_diskon = None
total_tiket = []
umur = None

print(f"Masukan {tiket_dibeli} Umur Pembeli :")

for i in range(tiket_dibeli):
    umur = int(input())
    if umur < 12:
        tiket_diskon = harga_tiket - (harga_tiket * 0.20)
    elif umur >= 12 and umur < 17:
        tiket_diskon = harga_tiket - (harga_tiket * 0.15)
    elif umur >= 17 and umur <= 20:
        tiket_diskon = float(harga_tiket - (harga_tiket * 0.10))
    else:
        tiket_diskon = harga_tiket - 0
    total_tiket.append(tiket_diskon)

print(f"\nTotal Tiket Dibeli\t : {tiket_dibeli} Tiket")
print(f"Total Harga Tiket\t : Rp {sum(total_tiket):,.0f}".replace(",", "."))
for i in range(tiket_dibeli):
    print(11 * "=" + "[TIKET WAHANA]" + 11 * "=")
print("\n" + 17 * "=" + "[SILAHKAN AMBIL TIKET]" + 17 * "=")
