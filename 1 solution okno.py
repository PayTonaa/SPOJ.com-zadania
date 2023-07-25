def bouncing_ball(height, bounce, window):
    if height > 0:
        a = 1
    else:
        return -1
    if bounce > 0 and bounce < 1:
        a = 2
    else:
        return -1
    if window < height:
        wysodb = height * bounce
        ile = 1
        while wysodb > window:
            wysodb = wysodb * bounce
            ile += 2
        return ile
    else:
        return -1
    

window = int(input("podaj wysokosc okba"))
height = int(input("wysokość podaj: "))
bounce = 0.5
x = bouncing_ball(height, bounce, window)
print(x)
