# 3. Napisz program do którego możemy wprowadzić dowolne zdanie. Niech nasz program wyświetli ile mamy d,v,b,n,k.

text = input("Wprowadź zdanie: ")

d = 0
v = 0
b = 0
n = 0
k = 0

for el in text:
    if el in ["d", "D"]:
        d += 1
    if el in ["v", "V"]:
        v += 1
    if el in ["b", "B"]:
        b += 1
    if el in ["n", "N"]:
        n += 1
    if el in ["k", "K"]:
        k += 1

print("")
print(f"Ilość d w zdaniu: {d}")
print(f"Ilość v w zdaniu: {v}")
print(f"Ilość b w zdaniu: {b}")
print(f"Ilość n w zdaniu: {n}")
print(f"Ilość k w zdaniu: {k}")