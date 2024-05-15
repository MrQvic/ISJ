This Python file contains a class named `Polynomial` that represents a polynomial with coefficients. The coefficients can be provided as positional arguments or as keyword arguments.

## Usage

You can create a `Polynomial` object in two ways:

1. Using positional arguments, which will be treated as a list of coefficients. For example:

```python
poly = Polynomial(1, 2, 3)  # Creates a polynomial with coefficients [1, 2, 3]
```

2. Using keyword arguments, which will be treated as coefficients in the format 'x{i}'. For example:

```python
poly = Polynomial(x0=1, x1=2, x2=3)  # Creates a polynomial with coefficients [1, 2, 3]
```

## Methods

The `Polynomial` class provides the following methods:

- `__str__`: Returns a string representation of the polynomial.
- `__eq__`: Checks if two polynomials are equal.
- `__add__`: Adds two polynomials.
- `__mul__`: Multiplies two polynomials.
- `__pow__`: Raises a polynomial to a power.
- `derivative`: Returns the derivative of the polynomial.
- `at_value`: Evaluates the polynomial at the given value(s) and returns the result.

## Testing

The file also includes a `main` function that runs tests on the `Polynomial` class.

```python
if __name__ == '__main__':
    test.test()
```

To run the tests, simply execute the Python file.