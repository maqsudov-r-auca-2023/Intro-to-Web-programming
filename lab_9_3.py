try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("Number must be positive.")
except ValueError as e:
    print("Error:", e)
else:
    print("Success! You entered:", num)