import random

print("This is a dice simulator")

x = input("Press y to roll ")
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
while x == 'y':
    number = random.randint(1, 6)
    if number == 1:
        print('===========')
        print('|         |')
        print('|    0    |')
        print('|         |')
        print('===========')
        a = 1
    elif number == 2:
        print('===========')
        print('|    0    |')
        print('|         |')
        print('|    0    |')
        print('===========')
        b = 1  
    elif number == 3:
        print('===========')
        print('|    0    |')
        print('|    0    |')
        print('|    0    |')
        print('===========')
        c = 1  
    elif number == 4:
        print('===========')
        print('| 0     0 |')
        print('|         |')
        print('| 0     0 |')
        print('===========')
        d = 1    
    elif number == 5:
        print('===========')
        print('| 0     0 |')
        print('|    0    |')
        print('| 0     0 |')
        print('===========')
        e = 1
    elif number == 6:
        print('===========')
        print('| 0     0 |')
        print('| 0     0 |')
        print('| 0     0 |')
        print('===========')                                   
        f = 1
    if a+b+c+d+e+f != 6:
        x = input("press y to roll ")
    elif a+b+c+d+e+f == 6:
        break
print("Game Over")