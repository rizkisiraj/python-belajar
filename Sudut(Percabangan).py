#input sudut
sudut = int(input("tuliskan nama sudut: "))

#lakukan percabangan
if sudut == 90:
    print("Sudut", sudut, "adalah", "sudut siku-siku") #print hasil
elif sudut < 90:
    print("Sudut", sudut, "adalah", "sudut lancip")
elif sudut == 180:
    print("Sudut", sudut, "adalah", "sudut lurus")
else :
    print("Sudut", sudut, "adalah", "sudut tumpul")