# Mój przyjaciel bierze ciąg wszystkich liczb od 1 do n (gdzie n > 0).
# W ciągu tym wybiera dwie liczby, a i b.
# Mówi, że iloczyn a i b powinien być równy sumie wszystkich liczb w tym ciągu, z wyłączeniem a i b.
# Czy biorąc pod uwagę liczbę n, mógłbyś powiedzieć, jakie liczby wykluczył z ciągu?
# Funkcja przyjmuje parametr: n (n jest zawsze ściśle większe od 0) i zwraca tablicę lub ciąg znaków (w zależności od języka) postaci:

# [(a, b), ...] lub [[a, b], ...] lub {{a, b}, ...} lub lub [{a, b}, ...]
# z wszystkimi (a, b), które są możliwymi usuniętymi liczbami w ciągu od 1 do n.

# [(a, b), ...] lub [[a, b], ...] lub {{a, b}, ...} lub ... zostaną posortowane w porządku rosnącym "a".

# Zdarza się, że istnieje kilka możliwych (a, b). Funkcja zwraca pustą tablicę (lub pusty łańcuch), jeśli nie zostaną znalezione żadne możliwe liczby, co udowodni, że mój przyjaciel nie powiedział prawdy! (Idź: w tym przypadku zwróć nil).

# Przykłady:
# removNb(26) powinno zwrócić [(15, 21), (21, 15)]
# lub
# removNb(26) powinno zwrócić { {15, 21}, {21, 15} }
# lub
# removeNb(26) powinno zwrócić [[15, 21], [21, 15]]
# lub
# removeNb(26) powinno zwrócić [ {15, 21}, {21, 15} ]
# lub
# removeNb(26) powinien zwrócić "15 21, 21 15"
# lub

def remov_nb(n):
    x=1
    liczby = []
    wynik = []
    suma = 0
    z = 0
    while x<=n:
        liczby.append(x)
        x+=1
    for x in range(len(liczby)):
        suma = suma + liczby[x]
        if 15*21 == suma:
            return True
        z+=1

    return liczby, suma, wynik


n = 26
print(remov_nb(n))