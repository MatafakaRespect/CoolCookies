# from random import randint
# lista = [randint(-50,50) for el in range(100)]
# print(lista)

# 6 .Napisz program, który przyjmuje jako argument powyższą listę i zwróci ile liczb jest większych lub równych 0. 

import random

lista = [random.randint(-50,50) for el in range(100)]
wieksze = 0

for i in lista:
    if i >= 0:
        wieksze += 1

print(lista)
print(f"W liście jest {wieksze} liczb większych bądź równych 0.")