print("Konversi Suhu")
print("-------------")

print("1. Celcius")
print("2. Farenheit")
print("3. Reamur")
print("4. Kelvin")

suhu = int(input("Masukkan Pilihan Anda : "))
print("\n")
if (suhu == 1):
    print("1. Celcius ke Farenheit")
    print("2. Celcius ke Reamur")
    print("3. Celcius ke Kelvin")

    suhu_celcius = int(input("Masukkan Pilihan Anda : "))
    print("\n")
    if (suhu_celcius == 1):
        print("Celcius ke Farenheit")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Celcius adalah :", a, "C")

        farenheit = ((9/5) * a) + 32

        print("Suhu dalam Farenheit adalah : ", farenheit, "F")

    elif (suhu_celcius == 2):
        print("Celcius ke Reamur")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Celcius adalah :", a, "C")

        reamur = (4/5) * a
        print("Suhu dalam Reamur adalah : ", reamur, "R")

    elif (suhu_celcius == 3):
        print("Celcius ke Kelvin")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Celcius adalah :", a, "C")

        kelvin = a + 273
        print("Suhu dalam Kelvin adalah : ", kelvin, "K")

if (suhu == 2):
    print("1. Farenheit ke Reamur")
    print("2. Farenheit ke Kelvin")
    print("3. Farenheit ke Celcius")

    suhu_farenheit = int(input("Masukkan Pilihan Anda : "))
    print("\n")
    if (suhu_farenheit == 1):
        print("Farenheit ke Reamur")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Farenheit adalah : ", a, "F")

        reamur = (4/5) * (a-32)
        print("Suhu dalam Reamur adalah : ", reamur, "R")

    elif (suhu_farenheit == 2):
        print("Farenheit ke Kelvin")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Farenheit adalah : ", a, "F")

        kelvin = ((5/9) * (a-32)) + 273
        print("Suhu dalam Kelvin adalah : ", kelvin, "K")

    elif (suhu_farenheit):
        print("Farenheit ke Celcius")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Farenheit adalah : ", a, "F")

        celcius = 5/9 * (a-32)
        print("Suhu dalam Celcius adalah : ", celcius, "C")

if (suhu == 3):
    print("1. Reamur ke Kelvin")
    print("2. Reamur ke Celcius")
    print("3. Reamur ke Farenheit")

    suhu_reamur = int(input("Masukkan Pilihan Anda : "))
    print("\n")

    if (suhu_reamur == 1):
        print("Reamur ke Kelvin")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Reamur adalah : ", a, "R")

        kelvin = ((5/4) * a) + 273
        print("Suhu dalam Kelvin adalah : ", kelvin, "K")

    elif (suhu_reamur == 2):
        print("Reamur ke Celcius")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Reamur adalah : ", a, "R")

        celcius = (5/4) * a
        print("Suhu dalam Celcius adalah : ", celcius, "C")

    elif (suhu_reamur == 3):
        print("Reamur ke Farenheit")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Reamur adalah : ", a, "R")

        farenheit = ((9/4) * a) + 32
        print("Suhu dalam Farenheit adalah : ", farenheit, "F")

if (suhu == 4):
    print("1. Kelvin ke Celcius")
    print("2. Kelvin ke Farenheit")
    print("3. Kelvin ke Reamur")

    suhu_kelvin = int(input("Masukkan Pilihan Anda : "))
    print("\n")

    if (suhu_kelvin == 1):
        print("Kelvin ke Celcius")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Kelvin adalah : ", a, "K")

        celcius = a - 273
        print("Suhu dalam Celcius adalah : ", celcius, "C")

    elif (suhu_kelvin == 2):
        print("Kelvin ke Farenheit")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Kelvin adalah : ", a, "K")

        farenheit = (9/5 * (a-273)) + 32
        print("Suhu dalam Farenheit adalah : ", farenheit, "F")

    elif (suhu_kelvin == 3):
        print("Kelvin ke Reamur")

        a = float(input("Masukkan Nilai Suhu : "))
        print("Suhu dalam Kelvin adalah : ", a, "K")

        reamur = (4/5 * (a-273))
        print("Suhu dalam Reamur adalah : ", reamur, "R")
