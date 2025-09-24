data_int = 2
print(data_int)
print("bertipe : ", type(data_int))

data_float = 2.3
print(data_float)
print("bertipe : ", type(data_float))

data_str = "halo"
print(data_str)
print("bertipe : ", type(data_str))

data_bool = True
print(data_bool)
print("bertipe : ", type(data_bool))

data_complex = complex(3, 4)
print(data_complex)
print("bertipe : ", type(data_complex))

# tipe data dari C
from ctypes import c_double, c_char

data_c_double = c_double(10.3)
print(data_c_double)
print("bertipe : ", type(data_c_double))
