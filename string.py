data = "ini str"
print(data)
print(type(data))

# cara membuat str

"""
1. Dengan menggunakan single quote ' '
2. Dengan menggunakan double quote " " 

"""
data = "single quote"
print(data)
data = "double quote"
print(data)

# menggunakan tanda \
print("mari jum'at")
print("isn't")
print("user\\user\\ali")
# tab
print("tab \t tab")
# backspace
print("alo \balo")
# new line
print("baris 1 \nbaris 2")  # new OS UNIX,LINUX
print("baris 1 \rbaris 2")  # old OS ACORN
print("baris 1 \r\nbaris 2")  # WINDOWS

# string literal atau raw
# menghilangkan semua  fungsi dengan str menggunakan r sebagai awalan sebelum str
print("\\user\\newfolder")
print(r"\user\newfolder")

# multi line litereal str
print(
    r"""
        \user\identitas\mahasiswa\ali
        nama : ali
        kelas: 3 sma"""
)
