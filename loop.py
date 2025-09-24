# looping or perulangan
# dengan list
data = [1, 2, 3, 4, 5]
print(data)
for i in data:
    print(f"i sekarang : {i}")

# Dengan range
# Di mulai dari 0
data = range(5)
for i in data:
    print(f"Hello World")
# Di mulai dari indeks 1->10 atau 1->9
for i in range(1, 10):
    print(f"i sekarang : {i}")

# while loop
i = 1
while i <= 3:
    print(f"Ini while ke-{i}")
    i += 1
