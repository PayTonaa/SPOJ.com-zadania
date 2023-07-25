# #Napisz funkcję, która przyjmuje tablicę liczb (całkowitych dla testów) oraz liczbę docelową. Powinna znaleźć dwa różne elementy w tablicy, które po zsumowaniu dają wartość docelową. Indeksy tych elementów powinny być następnie zwrócone w krotce / liście (w zależności od twojego języka), jak to: (index1, index2).

# Dla celów tego kata, niektóre testy mogą mieć wiele odpowiedzi; każde poprawne rozwiązanie będzie akceptowane.

# Dane wejściowe będą zawsze poprawne (liczby będą tablicą o długości 2 lub większej, a wszystkie elementy będą liczbami; cel będzie zawsze sumą dwóch różnych elementów z tej tablicy).

def two_sum(numbers, target):
    wynik = []
    for x in range (0, len(numbers)):
        for y in range(1, len(numbers)):
            if numbers[x] + numbers[y] == target:
                return [x, y]

numbers = [1,2,3]
target = 4
print(two_sum(numbers, target))