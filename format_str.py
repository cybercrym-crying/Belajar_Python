nama = "sina"
format_str = f"hello {nama}"
print(format_str)


angka = 2323
format_str = f"angka = {angka}"
print(format_str)

boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

angka = 23
format_str = f"angka = {angka:d}"
print(format_str)

ribuan = 20000
format_str = f"ribuan = {ribuan:,}"
print(format_str)

# mengambil 2 angka desimal di belakang
desimal = 434.1234
format_str = f"desimal = {desimal:.2f}"
print(format_str)

# menampilkan leading zero penambahan di depan sebuah data
angka = 123.456
format_str = f"angka = {angka:009.3f}"
print(format_str)

# menampilkan angka minus dan plus
mines = -19
plus = 23.345
format_mines = f"mines = {mines:+d}"
format_plus = f"plus = {plus:+.2f}"
print(format_plus, "\n", format_mines)

persen = 0.25
format_persen = f"persen = {persen:.0%}"
print(format_persen)

# melakukan operasi di dalam place holder

harga = 300000
jumlah = 2
format_str = f"harga total = Rp.{harga*jumlah:,}"
print(format_str)

# format angka lain (binary octal dan hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_hex = f"hex = {hex(angka)}"
format_octal = f"octal {oct(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
