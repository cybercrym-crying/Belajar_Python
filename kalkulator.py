print("\tKALKULATOR")
angka_1 = float(input("Masukan angka pertama : "))
operator = input("Masukan operator (+,-,*/x,/) ")
angka_2 = float(input("Masukan angka pertama : "))

if operator == "+":
    print(angka_1 + angka_2)
elif operator == "-":
    print(angka_1 - angka_2)
elif operator == "*" or operator == "x":
    print(angka_1 * angka_2)
else:
    print(angka_1 / angka_2)

print("END OF PROGRAM")
