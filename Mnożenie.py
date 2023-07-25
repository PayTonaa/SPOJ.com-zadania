def count_by(x, n):
    # z = 1
    # list = [x]
    # while z != n:
    #     z += 1                                   ############################# Wcześniejsza mniej optymalna wersja  13.01. 2023 #############################################
    #     u = x * z
    #     list.append(u)
    # return list
    
    list = []
    for n in range (1, n+1):
        list.append(x*n)
    return list
n = 5
x = 50
x = count_by(x, n)
print (x)