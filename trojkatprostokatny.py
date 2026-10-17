# Finally something more normal

print("Czy ten trójkąt jest prostokątny?")

a = float(input("Podaj bok 1. (przyprostokątna) "))
b = float(input("Podaj bok 2. (przyprostokątna) "))
c = float(input("Podaj bok 3. (przeciwprostokątna) "))

if (a*a + b*b == c*c) or (c*c - a*a == b*b) or (c*c - b*b == a*a):
 print("Trójkąt jest prostokątny")
else:
 print("Trójkąt nie jest prostokątny")

# He cooking up some bs i swear 🤣🤣