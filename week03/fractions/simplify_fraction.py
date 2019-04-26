def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    loop = min(nominator,denominator)

    if type(fraction) != tuple:
        raise ValidationError('Type of fraction not tuple !')

    if nominator == 0 or nominator == 1:
        return fraction

    if denominator == 0:
        raise ZeroDivisionError('Division by zero not allowed !')

    for number in range(1,loop+1):
        if nominator % number == 0 and denominator % number == 0:
            nominator //= number
            denominator //= number
            fraction=(nominator,denominator)

    return fraction
