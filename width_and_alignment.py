# Width and Multiline

# Data

data_nama = "ucup"
data_umur = 23
data_prodi = "Teksip"

data_str = f"nama = {data_nama}, \numur = {data_umur}, \nprodi = {data_prodi}"

print("\n" + 5 * "=" + "Data String" + 5 * "=")
print(data_str)

data_str = f"""
nama  = {data_nama:>6}
umur  = {data_umur:>6}
prodi = {data_prodi:>5}

"""
print("\n" + 5 * "=" + "Data String" + 5 * "=")
print(data_str)
