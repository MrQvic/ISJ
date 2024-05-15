#!/usr/bin/env python3

#author: Adam Mrkva - xmrkva04

import test

class Polynomial:
    """
    Represents a polynomial with coefficients.

    Coefficients can be provided as positional arguments or as keyword arguments.
    If positional arguments are provided, they will be treated as a list of coefficients.
    If keyword arguments are provided, they will be treated as coefficients in the format 'x{i}'.

    Example usage:
    poly = Polynomial(1, 2, 3)              # Creates a polynomial with coefficients [1, 2, 3]
    poly = Polynomial(x0=1, x1=2, x2=3)     # Creates a polynomial with coefficients [1, 2, 3]
    """
    def __init__(self, *coefficients, **kwargs) -> None:
        self.coefficients = []
        if coefficients:
            if isinstance(coefficients[0], list):
                self.coefficients = coefficients[0]
            else:
                self.coefficients = list(coefficients)

        #if coefficients are in xi format
        elif kwargs:   
            for i in range(max(int(k[1:]) for k in kwargs.keys()) + 1):
                self.coefficients.append(kwargs.get(f'x{i}', 0))

        #remove extra zeros
        while self.coefficients and self.coefficients[-1] == 0:
            self.coefficients.pop()

    def __str__(self) -> str:
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff == 0:
                continue
            if i == 0:
                terms.append(str(coeff))
            elif i == 1:
                terms.append(f'{"" if coeff == 1 else coeff if coeff != -1 else "-"}x')     #x 
            else:
                terms.append(f'{"" if coeff == 1 else coeff if coeff != -1 else "-"}x^{i}') #x^i

        if not terms:
            return "0"
        
        #add coeffs together and remove extra +
        return ' + '.join(reversed(terms)).replace("+ -", "- ")
        
    def __eq__(self, other) -> bool:
        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        return False 
    
    def __add__(self, other) -> "Polynomial":
        #check type of the other object
        if not isinstance(other, Polynomial):
            raise TypeError(f"{other} is not an instance of {Polynomial.__name__}")
        
        #create temp variable
        if len(self.coefficients) > len(other.coefficients):
            result = list(self.coefficients)
        else:
            result = list(other.coefficients)

        #add coeffs at given index
        for i in range(min(len(self.coefficients), len(other.coefficients))):
            result[i] = self.coefficients[i] + other.coefficients[i]
        return Polynomial(result)
        
    def __mul__(self, other) -> "Polynomial":
        if not isinstance(other, Polynomial):
            raise TypeError(f"{other} is not an instance of {Polynomial.__name__}")
        
        result = [0] * (len(self.coefficients) + len(other.coefficients))

        #add every coeff with each other
        for i, coeff1 in enumerate(self.coefficients):
            for j, coeff2 in enumerate(other.coefficients):
                result[i + j] += coeff1 * coeff2
        return Polynomial(result)
        
    def __pow__(self, power) -> "Polynomial":
        if not isinstance(power, int):
            raise TypeError("Exponent must be an integer")
        
        if power < 0:
            raise ValueError("Power must be a non-negative integer")
        elif power == 0:
            return Polynomial(1)
        elif power == 1:
            return self
        else:   #multiply polynom with his copy
            result = self
            for _ in range(1, power):
                result *= self
            return result
        
    def derivative(self) -> "Polynomial":
        """
        Returns:
            Polynomial: The derivative of the polynomial.
        """
        if len(self.coefficients) <= 1:
            return Polynomial(0)
        else:
            result = [0] * (len(self.coefficients))
            for i, coeff in enumerate(self.coefficients):
                if i == 0:  # skip first index - always 0
                    continue
                result[i - 1] = i * coeff   # adjust position of coeffs by -1
            return Polynomial(result)
        
    def at_value(self, x1, x2 = None) -> "Polynomial":
        """
        Evaluates the polynomial at the given value(s) and returns the result.

        Parameters:
        - x1: The first value at which to evaluate the polynomial.
        - x2: (optional) The second value at which to evaluate the polynomial. If not provided, only x1 will be used.

        Returns:
        - If x2 is not provided, returns the result of evaluating the polynomial at x1.
        - If x2 is provided, returns the difference between the results of evaluating the polynomial at x2 and x1.
        """
        def eval(x):
            result = 0
            for i, coeff in enumerate(self.coefficients):
                result += x**i * coeff
            return result
        
        if x2 is None:
            return eval(x1)
        else:
            return eval(x2) - eval(x1)
        
if __name__ == '__main__':
    test.test()