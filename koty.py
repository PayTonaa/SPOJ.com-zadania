def solution(start, finish):
    skok = 0
    roz = finish-start
    if roz <= 2:
        skok = roz
        return skok
    if roz % 3 == 1:
        skok = roz // 3 + 1
        return skok
    if roz % 3 == 2:
        skok = roz // 3 + 2
        return skok
    if roz % 3 == 0:
        skok = roz / 3
        return skok


start = 1
finish = 6
x = solution(start, finish)
print(x)
