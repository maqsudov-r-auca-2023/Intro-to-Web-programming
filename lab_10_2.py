import random

print(f"Random number between 1 and 10: {random.randint(1, 10)}")

names = ["Josh", "Mary", "Charlie", "David"]
print(f"The winner is: {random.choice(names)}")

random.shuffle(names)
print(f"Shuffled names: {names}")
