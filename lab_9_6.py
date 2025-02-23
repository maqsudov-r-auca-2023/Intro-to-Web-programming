class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot compute square root of a negative number.")
    return number ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print("Error:", e)
