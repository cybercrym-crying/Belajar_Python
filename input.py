# Input user

data = input("masukan data: ")
print("data = ", data, "tipe data =", type(data))

# jika ingin mengambil tipe str
data = int(input("masukan data: "))
print("data = ", data, "tipe data =", type(data))

# bagaimana dengan boolean? harus casting ke int dulu agar dapat menerima int berupa 1 = True atau 0 = False
data = bool(int(input("masukan data: ")))
print("data = ", data, "tipe data =", type(data))
