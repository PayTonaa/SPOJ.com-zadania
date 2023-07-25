def NWD(liczba, liczba2):
    while liczba != liczba2:
        if liczba > liczba2:
            liczba = liczba - liczba2
        else:
            liczba2 = liczba2 - liczba
    return liczba

def NWD2(liczba, liczba2):
    while liczba2 != 0:
        p = liczba%liczba2
        liczba = liczba2
        liczba2 = p
    return liczba

def NWW(liczba, liczba2):
    return (liczba*liczba2)/NWD(liczba, liczba2)

liczba = int(input("podaj liczbę: "))
liczba2 = int(input("podaj 2 liczbę: "))
# print(NWD(liczba, liczba2), NWD(liczba, liczba2))
print(NWW(liczba, liczba2))

