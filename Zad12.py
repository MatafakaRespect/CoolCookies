# 12. Napisz program która wygeneruje listę o n wielkości i “zasięgu” podanego przez użytkownika.

import random

n = int(input("Podaj najmniejszą liczbę, którą może wylosować program (musi być liczbą całkowitą): "))

print("")

n_naj = int(input("Podaj największą liczbę, którą może wylosować program (musi być liczbą całkowitą): "))

print("")

zasieg = int(input("Podaj, ile liczb ma wygenerować program (zasięg, musi być liczbą całkowitą): "))

print("")

print("Generowanie listy... ")

x = []

for i in range(zasieg):
    x.append(random.randint(n, n_naj))

print(f"Twoja niezbyt losowa lista (Python używa PRNG) to: {x}")