from collections import OrderedDict
import sys 

class TypeError(Exception):
    pass

class Term:
    def __init__(self,function):
        if type(function) is not str:
            raise TypeError('Term must be of <str> type!')
        self.term = function

    def __str__(self):
        return self.term

    @classmethod
    def find_derivative_of_greater_degree(cls,term):
        numbers = term.replace('x^',',')
        numbers = numbers.split(',')
        if len(numbers) == 1:
            return 'x^{}'.numbers[0]
        else:
            coef = eval('{}*{}'.format(numbers[0],numbers[1]))
            power = eval('{} - 1'.format(numbers[1]))

            der = '{}x^{}'.format(coef,power)
            if '^1' in der:
                der = der.replace('^1','')
            return der

    def find_derivative(self):
        if self.term.isdigit():
            return '0'
        elif self.term.endswith('x'):
            if self.term.strip('x') == '':
                return '1'
            return self.term.strip('x')
        else:
            return self.find_derivative_of_greater_degree(self.term)

class Polynomial:
    def __init__(self,terms):
        for term in terms:
            if type(term) is not Term:
                raise TypeError("Type of terms must be of class <Term>!")
        self.terms = terms

    def __str__(self):
        terms = [str(term) for index,term in enumerate(self.terms)]
        return ' + '.join(terms)

    @classmethod
    def find_derivatives(cls,terms):
        derivatives = [term.find_derivative() for term in terms]
        return derivatives

    @classmethod
    def find_x(cls,term):
        for index,ch in enumerate(term):
            if ch == 'x':
                return index

    def term_derivatives(self):
        derivatives = self.find_derivatives(self.terms)
        while '0' in derivatives:
            derivatives.remove('0')

        if len(derivatives) == 0:
            return '0'

        group = []
        num = 0
        for term in derivatives:
            if 'x' in term:
                index = self.find_x(term)
                group += [(int(term[:index]),term[index:])]
            else:
                num += int(term)

        dictionary = OrderedDict()
        for item in group:
            if item[1] not in dictionary.keys():
                dictionary[item[1]] = item[0]
            else:
                dictionary[item[1]] += item[0]

        dictionary = OrderedDict(sorted(dictionary.items(), reverse=True)) # reverse ordered dict 

        result = list()
        for key,value in dictionary.items():
            result.append(str(value)+key)

        if num != 0:
            result.append(str(num))

        return ' + '.join(result)

def main():
    input_polynomial = sys.argv[1]
    input_polynomial = input_polynomial.split('+')
    polynomial = Polynomial([Term(term) for term in input_polynomial])
    print('The derivative of f(x) = {} is'.format(polynomial))
    print(polynomial.term_derivatives())

if __name__=='__main__':
    main()
