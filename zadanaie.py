def simplify(poly):
    monomials = re.findall('[+-]?[^+-]+', poly)
    coeff_dict = {}
    for monomial in monomials:
        match = re.match('([+-]?)(\d*)(\w+)', monomial)
        sign, coeff, vars = match.groups()
        if coeff == '':
            coeff = 1
        else:
            coeff = int(coeff)

        vars = ''.join(sorted(vars))

        if vars in coeff_dict:
            coeff_dict[vars] += coeff if sign == '+' else -coeff
        else:
            coeff_dict[vars] = coeff if sign == '+' else -coeff
    sorted_monomials = sorted(coeff_dict.keys(), key=lambda x: (len(x), x))   
    simplified_poly = ''
    for monomial in sorted_monomials:
        coeff = coeff_dict[monomial]
        if coeff > 0:
            simplified_poly += '+' if simplified_poly else ''
            if coeff == 1 and simplified_poly != '':
                simplified_poly += monomial
            else:
                simplified_poly += str(coeff) + monomial
        elif coeff < 0:
            if coeff == -1:
                simplified_poly += '-' + monomial
            else:
                simplified_poly += str(coeff) + monomial  
    if not simplified_poly:
        return '0'
    if simplified_poly[0] == '+':
        simplified_poly = simplified_poly[1:]  
    return simplified_poly
