def divide(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b

try:
    print(divide(10, 0))
except AssertionError as e:
    print("Assertion Error:", e)