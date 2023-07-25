# Napisz funkcję o nazwie first_non_repeating_letter, która pobiera ciąg znaków i zwraca pierwszy znak, który nie powtarza się nigdzie w ciągu.
#
# Na przykład, jeśli podano dane wejściowe "stres", funkcja powinna zwrócić "t", ponieważ litera t występuje tylko raz w ciągu i występuje jako pierwsza w ciągu.
#
# Jako dodatkowe wyzwanie, wielkie i małe litery są uważane za ten sam znak, ale funkcja powinna zwrócić poprawną wielkość początkowej litery. Na przykład, wejście "sTreSS" powinno zwrócić "T".
#
# Jeśli łańcuch zawiera wszystkie powtarzające się znaki, powinna zwrócić pusty łańcuch ("") lub None -- zobacz przykładowe testy.



def first_non_repeating_letter(string):
    string = list(string)
    licznik = 0
    while " " in string:
        string.remove(" ")
    for x in range(0, len(string)):
        if licznik == 1:
            return string[x-1]
        licznik = 0
        for y in range(0, len(string)):
            if string[y] == string[x] or string[y] == string[x].upper() or string[y] == string[x].lower():
                licznik += 1
    if licznik == 1:
        return string[x - 1]
    else:
        return ""


string = "XhgMXFDlUJZV"
print(first_non_repeating_letter(string))
