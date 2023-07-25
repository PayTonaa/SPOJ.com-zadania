import math
import matplotlib.pyplot as plt

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Miejsca zerowe to: x1={x1}, x2={x2}")
    x = range(-10, 11)
    y = [a*i**2 + b*i + c for i in x]
    plt.plot(x, y, 'b-')
    plt.plot([x1], [0], 'ro')
    plt.plot([x2], [0], 'ro')
    plt.show(block=False)
    plt.pause(3)
    plt.close()
elif delta == 0:
    x = -b / (2*a)
    print(f"Miejsce zerowe to: x={x}")
    x = range(-10, 11)
    y = [a*i**2 + b*i + c for i in x]
    plt.plot(x, y, 'b-')
    plt.plot([x], [0], 'ro')
    plt.show(block=False)
    plt.pause(3)
    plt.close()
else:
    print("Funkcja nie ma miejsc zerowych")


