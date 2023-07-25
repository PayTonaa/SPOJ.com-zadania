def solution(start, finish):
    n = finish - start
    return n // 3 + n % 3

start = 1
finish = 3
x = solution(start, finish)
print(x)