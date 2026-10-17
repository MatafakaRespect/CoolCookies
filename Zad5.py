# from random import randint
# lista = [randint(-50,50) for el in range(100)]
# print(lista)

# 5. Napisz program, który przyjmuje jako argument powyższą listę i zwróci ile jest liczb mniejszych od 0

import random

lista = [random.randint(-50,50) for el in range(1000000)]

less = 0

for num in lista:
    if num < 0:
        less += 1

print(lista)
print(f"Liczb mniejszych niż 0 jest {less}")