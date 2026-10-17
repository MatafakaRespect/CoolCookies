# 2. Wygeneruj listę 20 liczb losowych z przedziału 100 do 200. Parzystych niepodzielnych przez 5. 

import random

list = []
amount = 0

while len(list) < 20:
    rand = random.randint(100, 200)
    if rand % 5 != 0 and rand % 2 == 0:
        list.append(rand)
        amount += 1

print(list)