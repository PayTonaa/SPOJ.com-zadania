# https://pl.spoj.com/problems/PA05_POT/
def last_digit(a, b):
    if b == 0:
        return 1
    a %= 10
    b %= 4
    if b == 0:
        b = 4
    return (a ** b) % 10

D = int(input())

for _ in range(D):
    a, b = map(int, input().split())
    result = last_digit(a, b)
    print(result)

#  polecenie:

# PA05_POT - Czy umiesz potęgować
# Zadanie: POT (Czy umiesz potęgować)
# Dla danych dwóch liczb naturalnych a i b, wyznaczyć ostatnią cyfrę liczby ab.

# Zadanie
# Napisz program, który:
# wczyta ze standardowego wejścia: podstawę a oraz wykładnik b,
# wyznaczy ostatnią cyfrę liczby ab,
# wypisze wynik na standardowe wyjście.
# Wejście
# W pierwszej linii wejścia znajduje się jedna liczba całkowia D (1≤D≤10), oznaczjąca liczbę przypadków do rozważenia. Opis każdego przypadku podany jest w jednym wierszu, zawierającym dwie liczby naturalne a i b oddzielone pojedynczym odstępem (spacją), takie, że (1 ≤ a,b ≤ 1 000 000 000).

# Wyjście
# Dla każdego przypadku z wejścia Twój program powinien wypisać (w osobnej linii dla każdego przypadku z wejścia) cyfrę jedności liczby ab zapisanej dziesiętnie.
