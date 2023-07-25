
def controller(events):
    zmiana = events.split('.')

    import time
    a = 0
    sprawdzenie = 0

    for x in range(4, -1, -1):
        print(x)
        time.sleep(1)

    return zmiana


events = input("podaj zdarzenia: ")
x = controller(events)
print(x)
