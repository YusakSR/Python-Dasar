# persegi panjang
print("Menghitung Luas Persegi Panjang")
print("===============================")

p = int(input('Masukkan Nilai Panjang : '))
l = int(input('Masukkan Nilai Lebar   : '))

luas = p*l
keliling = 2*(p*l)
print("\n")

print('Luas Persegi Panjang =', str(luas))
print('Keliling Persegi Panjang =', str(keliling))

# Segitiga
print("\nMenghitung Luas Segitiga")
print("========================")

alas = int(input("Masukkan Nilai Alas : "))
tinggi = int(input("Masukkan Nilai Tinggi : "))

luas = (1/2*alas) * tinggi
print("\n")

print("Luas Segitiga = ", str(luas))

# Persegi
print("\nMengitung Luas Persegi")
print("======================")

s = int(input("Masukkan Nilai Sisi : "))

luas = s*s
print("\n")

print("Luas Persegi = ", str(luas))
