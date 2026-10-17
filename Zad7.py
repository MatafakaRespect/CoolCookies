# from random import randint
# lista = [randint(-50,50) for el in range(100)]
# print(lista)

# 7. Napisz program który przyjmuje jako argument powyższą listę i zwróci sumę wszystkich elementów parzystych. 

from random import randint

lista = [randint(-50,50) for el in range(100)]

parzyste = []

for el in lista:
    if el % 2 == 0:
        parzyste.append(el)

print(parzyste)
suma = sum(parzyste)

print(f"Suma wszystkich elementów parzystych wynosi {suma}")