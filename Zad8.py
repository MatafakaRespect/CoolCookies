# from random import randint
# lista = [randint(-50,50) for el in range(100)]
# print(lista)

# 8. Napisz program który przyjmuje jako argument powyższą listę i zwróci sumę wszystkich elementów nieparzystych.

from random import randint

lista = [randint(-50,50) for el in range(100)]

nieparzyste = []

for el in lista:
    if el % 2 == 0:
        nieparzyste.append(el)

print(nieparzyste)
suma = sum(nieparzyste)

print(f"Suma wszystkich elementów nieparzystych wynosi {suma}")