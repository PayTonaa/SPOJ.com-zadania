def parzysta(liczba):
    if liczba % 2 == 0:
        return "Parzysta"
    else:
        return "Nieparzysta"
liczba = int(input("podaj liczbę: "))
print(parzysta(liczba))

