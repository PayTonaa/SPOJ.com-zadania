def list_squared(m, n):
    dzielniki = []
    suma = 0
    wyniki = []
    for x in range(n, m):
        for i in range(1, int(x/2) + 1): 
            if x % i == 0: 
                dzielniki.append(i)
        for z in range(0, len(dzielniki)):
            suma += dzielniki[x]
            if suma == x**2:
                wyniki.append(suma, dzielniki)
        dzielniki = []
        suma = 0

    return wyniki
        




    


n = 1
m = 250