def zmiana(tekst, system):
    wynik= 0
    for x in tekst:
        kod = ord(x) - 48
        if kod > 9:
            kod = kod - 7
        wynik = wynik * system + kod
    return wynik


tekst = input("podaj liczbe")
system = int(input("podaj system"))
print (zmiana(tekst,system))

