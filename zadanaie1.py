# -------------------------------------------------- COŚ ZEPSUŁEM ALE DO NAPRAWY, POLECENIE PONIZEJ -----------------------------------------#


# When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

# Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):

# All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
# "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"


# All monomials appears in order of increasing number of variables, e.g.:
# "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

# If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
# "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

# There is no leading + sign if the first coefficient is positive, e.g.:
# "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

# N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. Multilinear means in this context: of degree 1 on each variable.

# Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.

# Good Work :) 



def simplify(poly):
    poly = list(poly)
    #porządkowanie
    cache = ""
    y = ""
    for x in range (len(poly)):
        cache += poly[x]
        if poly[x] == "+" or poly[x] == "-":            
                z= cache[:-1]
                cache = ""
                z = sorted(z)
                for a in range (len(z)):
                     y += z[a]
                y += " "
                y += poly[x]
    poly = ""
    y += " "
    z = list(cache) 
    z = sorted(z)
    for b in range(len(z)):
         y += z[b]
    y += " "
    y = y.split(" ")
    while "" in y:
         y.remove("")
    # Obliczanie wartrości wyrazenia
    stack = []
    for m in range (len(y)):
        for i in y[m]:
            if i == "+" or i == "-":
                 stack.append(i)
            elif i.isdigit():
                stack.append(i)
                stack.append(" ")
            elif stack[-1] == "+" or stack[-1] == "-" and i.isalpha():
                 stack.append("1")
                 stack.append(" ")
                 stack.append(i)
            elif i.isalpha():
                stack.append(i) 


    return y, stack


        





poly = "2xy+yx"
print(simplify(poly))

#https://www.codewars.com/kata/55f89832ac9a66518f000118/train/python