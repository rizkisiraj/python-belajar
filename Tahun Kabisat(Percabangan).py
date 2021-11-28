tahun = int(input("Masukkan tahun: "))

if tahun % 400 == 0 or (tahun % 400 != 0 and tahun % 100 != 0 and tahun % 4) == 0:
    print("Kabisat")
elif (tahun % 400 != 0 and tahun % 100 == 0):
    print("Bukan Kabisat")
else:
    print("Bukan Kabisat")