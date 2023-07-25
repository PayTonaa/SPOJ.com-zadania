def find_needle(haystack):
    txt = "found the needle at position %s"
    for x in range (0, len(haystack)+1 ):
        if haystack[x] == "needle":
            return txt % x
haystack = ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]
print (find_needle(haystack))
