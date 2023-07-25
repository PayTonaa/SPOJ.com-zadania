def zmianaliczbz10na8(liczba):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % 8) + wynik
        liczba = liczba // 8
    return wynik

liczba = int(input("podaj liczbe: "))
print(zmianaliczbz10na8(liczba))
