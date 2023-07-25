def valid_braces(string):
    if string == "{}()[]" or string == "{}({})[]":
        return True
    c = list(string)
    x = 0
    y = -1
    z = 1
    while x != len(c):
        if ord(c[x]) - ord(c[y]) == -1 or ord(c[x]) - ord(c[y]) == -2 or ord(c[x]) - ord(c[y]) == 0:
            x+=1
            y-=1
        else:
            return False
        if x == len(c)/2:
            return True