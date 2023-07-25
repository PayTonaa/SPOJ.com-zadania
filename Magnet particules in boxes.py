def doubles(maxk, maxn):
    result = 0
    for k in range(1, maxk+1):
        for n in range(1, maxn+1):
            result += 1 / (k * (n + 1) ** (2 * k))
    return result