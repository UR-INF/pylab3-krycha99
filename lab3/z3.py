import random
from array import *
lr = array('f', [])
print("podaj ilosc: ")
x = input()

for i in range(int(x)):
    lr.append(random.randrange(-5, 5, 1))

    
f = open("result.txt", "w")
for i in lr:
    f.write(str(i)+ "  ")
f.close()
