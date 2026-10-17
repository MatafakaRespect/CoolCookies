# 1. Wygeneruj listę 10 liczb losowych z przedziału 1 do 100. 

import random

list = []
amount = 0

for amount in range(10):
    amount += 1
    number = random.randint(1, 100)
    list.append(number)

print(list)