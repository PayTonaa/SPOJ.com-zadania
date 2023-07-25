def najwyższydzielnikliczby(liczba):
    ilość = 0
    dzielnik = 2
    powtorzenia = 0
    while dzielnik * dzielnik <= liczba:
        if liczba % dzielnik == 0:
            ilość += 2
        dzielnik += 1
        powtorzenia += 1
    return ilość, powtorzenia



liczba = int(input("podaj liczbę"))
print(najwyższydzielnikliczby(liczba))


