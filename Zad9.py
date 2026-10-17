# from random import randint
# lista = [randint(-50,50) for el in range(100)]
# print(lista)

# 9. Napisz program który przyjmuje jako argument powyższą listę i zwróci sumę wszystkich elementów podzielnych przez 5 i 7. 

from random import randint

lista = [randint(-50,50) for el in range(100)]

x = []

for el in lista:
    if el % 5 == 0 or el % 7 == 0:
        x.append(el)

suma = sum(x)

print(suma)
print(x)
print(f"Suma wszystkich elementów wynosi {suma}")