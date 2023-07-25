def is_defended(attackers, defenders):

    # dane

    survivorsl = 0  # napastnicy przetrwanie
    survivorsl1 = 0  # obroncy przetrwanie
    z = 0
    x = len(l)
    x2 = len(l1)

    # program

    l = attackers.split(', ')
    l1 = defenders.split(', ')
    if x > x2:
        l1.append([x2, x], 1, 0)

        while x > 0:
            z += 1
            p = l[x]  # napastnicy
            o = l1[x2]  # obrońcy
            if p > o:
                survivorsl + 1
                survivorsl1 - 1
            if p == o:
                survivorsl - 1
                survivorsl1 - 1
            if p < o:
                survivorsl - 1
                survivorsl1 + 1
            else:
                return 0


attackers = input("podaj liczby żołniezy ")
defenders = input("podaj obrońców ")
x = is_defended(attackers, defenders)
print(x)
