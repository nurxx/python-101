from simplify_fraction import *

def collect_two(fraction1,fraction2):
    return (fraction1[0]*fraction2[1] + fraction1[1]*fraction2[0],fraction1[1]*fraction2[1])

def collect_fractions(fractions):
    stack = fractions
    while len(stack) != 1:
        first = stack.pop()
        second = stack.pop()
        stack.append(simplify_fraction(collect_two(first,second)))

    return simplify_fraction(stack[0])

