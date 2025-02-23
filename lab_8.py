def square(num):
    return num ** 2

print(square(5))


# 2.
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))


# 3.
def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


# 4.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
