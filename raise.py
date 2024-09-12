class NegativeNumberError(Exception):
    """Exception raised for errors in the input if the number is negative."""
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot take the square root of a negative number.")
    return x ** 0.5

try:
    result = square_root(-8)
except NegativeNumberError as e:
    print(e)
