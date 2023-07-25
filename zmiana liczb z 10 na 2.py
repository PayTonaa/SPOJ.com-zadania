def zmianaliczbz10na2(liczba):
    wynik = ""
    while liczba > 0:
        wynik += str(liczba % 2)
        liczba = liczba//2
    return wynik

liczba = int(input("podaj liczbe: "))
print(zmianaliczbz10na2(liczba))

