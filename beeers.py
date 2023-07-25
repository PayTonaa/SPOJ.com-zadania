import math


def beeramid(bonus, price):
    if bonus <= 0 or bonus < price:
        return 0
    used = 0
    beers = math.floor(bonus / price)
    levels = 0
    x = 1
    while beers > 0:
        used = x*x
        beers -= used
        levels += 1
        x += 1
        if beers < 0:
            return levels - 1
    return levels
