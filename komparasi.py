# > < <= >= == != is is not

a = 3
b = 4

hasil = a > b
print(hasil)
hasil = a < b
print(hasil)
hasil = a <= 3
print(hasil)
hasil = a >= 3
print(hasil)
hasil = a == 3
print(hasil)
hasil = a != b
print(hasil)

# is dan is not sebagai pembanding identitas memori
# jadi literal tidak bisa
x = 5
y = 4

print("id x =", hex(id(x)))
print("id y =", hex(id(y)))
print(x is y)
print(x is not y)
