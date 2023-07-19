D = int(input())
for x in range(D):
    n = int(input())
    dzie = 0
    jed = 1
    for i in range(2, n + 1):
        dzie = ((dzie * i) % 100) // 10
        jed = (jed * i) % 10
    print(dzie, jed)
