# from random import randint
# lista = [randint(-50,50) for el in range(100)]

# 11. Zwrócić listy w których będą zawarte indeksy pod którymi występują największe i najmniejsze wartości. 

from random import randint

lista = [randint(-50,50) for el in range(100)]

maximum = max(lista)
minimum = min(lista)

max_liczba = [i for i, val in enumerate(lista) if val == maximum]
min_liczba = [i for i, val in enumerate(lista) if val == minimum]

print(lista)
print(f"Najmniejsza liczba w liście to {minimum}, a największa to {maximum}")
print(f"Znajdują się one w indeksach {min_liczba} i {max_liczba} odpowiednio")