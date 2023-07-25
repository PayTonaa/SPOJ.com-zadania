# Napisz prosty parser, który będzie parsował i uruchamiał Deadfish.

# Deadfish posiada 4 komendy, każda o długości 1 znaku:

# i zwiększa wartość (początkowo 0)
# d dekrementuje wartość
# s kwadratuje wartość
# o wypisuje wartość do tablicy zwrotnej
# Nieprawidłowe znaki powinny być ignorowane.

def parse(data):
    data = list(data)
    wynik = []
    wyn = 0
    for x in range (0, len(data)):
        if data[x] == "i":
            wyn += 1
        if data[x] == "o":
            wynik.append(wyn)
        if data[x] == "d":
            wyn -= 1
        if data[x] == "s":
            wyn = wyn**2
        x += 1
    return wynik

data = "ioioio"
print(parse(data))