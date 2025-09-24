a = 4  # ini adalah assignment
print("a = ", a)

# pertambahan
a += 1
print("a = ", a)

# pengurangan
a -= 2
print("a = ", a)

# perkalian
a *= 2
print("a = ", a)

# pembagian
a /= 2
print("a = ", a)

# modulus
a %= 2
print("a = ", a)

# floor
a //= 2
print("a = ", a)

# pangkat
a **= 2
print("a = ", a)

# operasi bit wise
b = True
# or
print("b =", format(b, "08b"))
b |= False
print("b =", format(b, "08b"))
# and
b &= False
print("b =", format(b, "08b"))
b = 0b0100
b >>= 1
print("b =", b)
print("b =", format(b, "04b"))
