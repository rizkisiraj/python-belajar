list = []
n = int(input("Berapa banyak angka yang anda mau : ")) #input batas looping
for i in range(n):
    c = input("silahkan masukkan perintah: ").split() #input perintah   
    if c[0] == "remove":
        list.remove(int(c[1])) #remove list
    elif c[0] == "insert":
        list.insert(int(c[1]), int(c[2])) #insert list 
    elif c[0] == "append":
        list.append(int(c[1])) #append list
    elif c[0] == "sort":
        list.sort() #sort list
    elif c[0] == "reverse":
        list.reverse() #reverse list
    elif c[0] == "pop":
        list.pop() #pop list alias menghilangkan yang paling belakang
    elif c[0] == "print":
        print(list) #print list