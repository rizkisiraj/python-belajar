x = int(input("Masukkan halaman buku: "))


halaman = [20, 30, 15, 10, 20, 35, 50]

hari = ["Ahad", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

p = 0

for i in halaman:
    x = x - i
    p = p + 1
    if x <= 0:
        break

if 7 > p > 0:
    print(hari[p-1])
else:
    print("Lanjut Minggu Depan")