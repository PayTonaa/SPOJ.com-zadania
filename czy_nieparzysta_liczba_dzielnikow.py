def czy_nieparzysta_liczba_dzielnikow(n):
    dzielniki = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dzielniki += 1
            if i != n // i:
                dzielniki += 1

    return dzielniki % 2 != 0


n = int(input())


if czy_nieparzysta_liczba_dzielnikow(n):
    print("TAK")
else:
    print("NIE")

# polecenie:


# FR_14_08 - Nieparzysta liczba dzielników

# Napisz program, który sprawdzi, czy liczba ma nieparzystą liczbę dzielników.

# Wejście
# Pierwszy i jedyny wiersz wejścia zawiera jedną liczbę całkowitą n (1 ≤ n ≤ 109).

# Wyjście
# W pierwszym i jedynym wierszu wyjścia należy 
