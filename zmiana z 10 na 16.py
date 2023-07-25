def zmianaz10na16(liczba):
    wynik = ""
    while liczba > 0:
        reszta = liczba%16
        if reszta > 9:
            wynik = chr(reszta+55)+wynik
        else:
            wynik = str(reszta) + wynik
            liczba = liczba // 16
liczba = int(input("podaj liczbe"))
print  (zmianaz10na16(liczba))