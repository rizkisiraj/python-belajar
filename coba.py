#input jenis magnet
#Str untuk kata-kata, int untuk bilangan asli, float untuk bilangan desimal
a = str(input())
b = str(input())
c = str(input())
d = str(input())
e = str(input())
f = str(input())

jumlah_batang = 1

if a != b:
    jumlah_batang = jumlah_batang + 1
if b != c:
    jumlah_batang = jumlah_batang + 1
if c != d:
    jumlah_batang = jumlah_batang + 1
if d != e:
    jumlah_batang = jumlah_batang + 1
if e != f:
    jumlah_batang = jumlah_batang + 1

print(jumlah_batang)
