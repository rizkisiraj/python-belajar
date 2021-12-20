a = int(input("Masukkan angka prima : "))

if a < 1:
    print("Bukan Prima")
elif a > 1:
    for i in range(2, a):
        if a % i == 0:
            print("Bukan Bilangan Prima")
            break
    else:
        print("Bilangan Prima")