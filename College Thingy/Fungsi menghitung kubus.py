def luas_kubus(x):
    luas = 6 * (x ** 2)
    return luas

def volume_kubus(x):
    volume = x ** 3
    return volume

def hasil_luas(x,y):
    print("Luas kubus dengan sisi",x,"yaitu: ",y)

def hasil_volume(x,y):
    print("Volume kubus dengan sisi",x,"yaitu: ",y)

# sisi kubus
sisi_1 = int(input("Masukkan sisi kubus: "))
sisi_2 = int(input("Masukkan sisi kubus: "))
sisi_3 = int(input("Masukkan sisi kubus: "))
print('')
print('========================================')
print('')

lst = {sisi_1:luas_kubus(sisi_1),sisi_2:luas_kubus(sisi_2),sisi_3:luas_kubus(sisi_3)}
listo = {sisi_1:volume_kubus(sisi_1),sisi_2:volume_kubus(sisi_2),sisi_3:volume_kubus(sisi_3)}


for i in lst:
    hasil_luas(i, lst[i])

print('')

for a in listo:
    hasil_volume(a, listo[a])
