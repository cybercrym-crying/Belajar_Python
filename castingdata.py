# Merubah tipe data
print("===INT===")
dataint = 9
print("data =", dataint, "bertipe : ", type(dataint))
datafloat = float(dataint)
datastr = str(dataint)
databool = bool(dataint)  # bool = 0 false
print("data =", datafloat, "bertipe : ", type(datafloat))
print("data =", datastr, "bertipe : ", type(datastr))
print("data =", databool, "bertipe : ", type(databool))

print("===FLOAT===")
datafloat = 9.6
print("data =", datafloat, "bertipe : ", type(datafloat))
dataint = int(datafloat)  # akan di bulatkan ke bawah
datastr = str(datafloat)
databool = bool(datafloat)
print("data =", dataint, "bertipe : ", type(dataint))
print("data =", datastr, "bertipe : ", type(datastr))
print("data =", databool, "bertipe : ", type(databool))

print("===STR===")
datastr = "0"
print("data =", datastr, "bertipe : ", type(datastr))
datafloat = float(datastr)
dataint = int(datastr)  # datastr harus berupa angka
datastr = ""
databool = bool(datastr)  # datastr harus kosong agar false
print("data =", datafloat, "bertipe : ", type(datafloat))
print("data =", dataint, "bertipe : ", type(dataint))
print("data =", databool, "bertipe : ", type(databool))

print("===BOOL===")
databool = False
print("data =", databool, "bertipe : ", type(databool))
datafloat = float(databool)
datastr = str(databool)
dataint = int(databool)
print("data =", datafloat, "bertipe : ", type(datafloat))
print("data =", datastr, "bertipe : ", type(datastr))
print("data =", dataint, "bertipe : ", type(dataint))
