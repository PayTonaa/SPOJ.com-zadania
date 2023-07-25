def zmianaz10nadowolny(liczba, system):
    wynik = ""
    while liczba > 0:
        reszta = liczba % system
        if reszta > 9:
            wynik = chr(reszta+55) + wynik
        else:
            wynik = str(reszta) + wynik
        liczba = liczba // system
    return wynik



liczba = int(input("podaj liczbe: "))
system = int(input("podaj system na jaki chcesz: "))
print(zmianaz10nadowolny(liczba, system))