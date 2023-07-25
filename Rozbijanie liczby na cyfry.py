n = int(input("podaj liczbe: "))
b = ""
while n>0:
    reszta = n%10
    b+=str(reszta)
    print(reszta)
    n = n//10
print(b)



# żeby rozbić liczbę -> dzielenie z resztą, którą dodajemy do str b i całkowicie na liczbie dzielonko