# bitwise atau biner operasi masing masing bit

a = 1
b = 2
print("a = ", a, "binary =", format(a, "08b"))
print("b = ", b, "binary =", format(b, "08b"))

c = a | b
print("===OR===")
print(c, "binary =", format(c, "08b"))  # yang di operasikan adalah binary nya

print("===AND===")
c = a & b
print(c, "binary =", format(c, "08b"))  # yang di operasikan adalah binary nya

print("===XOR===")
c = a ^ b
print(c, "binary =", format(c, "08b"))

print("===NOT===")
# karena not akan menjadi mines gunakan binary dan xor
binary = 0b11111111
c = binary ^ 0b00000001
print(c, "binary =", format(c, "08b"))

# shifting
# shift left <<
c = a << 2
print(c, "binary =", format(c, "08b"))

# shift left >>
c = a >> 2
print(c, "binary =", format(c, "08b"))
