"""
celcius = float(input("masukan derajat celcius: "))
reamur = celcius * (4 / 5)
fahrenheit = celcius * (9 / 5) + 32
kelvin = celcius + 273
print("Reamur:", reamur)
print("Fahrenheit: ", fahrenheit)
print("Kelvin: ", kelvin)
"""

# SOAL BIKIN FAHRENHEIT -> KELVIN DAN KELVIN  -> FAHRENHEIT

fahrenheit = float(input("fahrenheit -> kelvin,masukan suhu"))
kelvin = ((fahrenheit - 32) * (5 / 9)) + 273
print("kelvin =", kelvin)

kelvin = float(input("kelvin -> fahrenheit,masukan suhu"))
fahrenheit = (kelvin - 273) * (9 / 5) + 32
print("fahrenheint =", fahrenheit)
