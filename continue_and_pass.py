# continue , pass

# pass -> berfungsi sebagai dummy

angka = 0

while angka <= 4:
    angka += 1

    if angka == 3:
        pass
    print(angka)


# continue -> akan melewati code setelahnya namun perulangan tetap berlanjut
i = 1
for i in range(5):
    if i == 3:
        print("ini continue")
        continue
    print(i)
