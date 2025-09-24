# Latihan bikin bintang
i = 0
jumlah_bintang = 5
while i < jumlah_bintang:
    j = 0
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

print()
bintang = 5
count = 1
for i in range(bintang):
    print("*" * count)
    count += 1

count = 1
print()
while True:
    print("*" * count)
    if count == bintang:
        count = 1
        break
    count += 1

# Just Ganjil

print()
i = 1
while i <= bintang:
    print("*" * count)
    i += 1
    count += 2

print()
count = 1
while True:
    if count % 2 == 1:
        print("*" * count)
    if count == bintang:
        break
    count += 1

# Segitiga sama kaki

count = 1
bintang = 5
kosong = bintang
print()
for i in range(bintang):
    print(" " * kosong + "*" * count)
    count += 2
    kosong -= 1

# Diamond
count = 1
bintang = 5
kosong = bintang
print()
for i in range(bintang):
    print(" " * kosong + "*" * count)
    count += 2
    kosong -= 1


bintang = 5
for i in range(bintang):
    count -= 2
    kosong += 1
    print(" " * kosong + "*" * count)
