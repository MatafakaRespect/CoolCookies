# from random import randint
# lista = [randint(-50,50) for el in range(100)]


# 10. Napisz program który przyjmuje jako argument powyższą listę poprosi o podanie liczby przez użytkownika i powie ile takich liczb występuje na tej liście. 

from random import randint

lista = [randint(-50,50) for el in range(1000)]
while True:

    query = input("Wpisz dowolną liczbę z przedziału od -50 do 50 (lub wpisz stop, aby zatrzymać program): ")
    print("")

    if query in ["stop", "Stop"]:
        break  
    
    query = int(query)
    
    if query > 50:
        
        print("Wpisz liczbę mniejszą niż 50.")
        print("")
    
    elif query < -50:
        
        print("Wpisz liczbę większą od -50.")
        print("")

    elif query in range(-50, 50):
        
        similar = 0

        for el in lista:
            if el == query:
                similar += 1

        print(f"Na liście liczba {query} występuje {similar} razy.")
        print("")

    elif query in ["stop", "Stop"]:
        break