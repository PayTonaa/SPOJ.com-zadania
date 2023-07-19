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
