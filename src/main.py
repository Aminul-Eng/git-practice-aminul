from datetime import date

from utils import add, subtract, multiply


print("Name: Aminul Islam")
print("Today's date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))


# Basic calculator checks
assert add(10, 5) == 15
assert subtract(10, 5) == 5
assert multiply(10, 5) == 50

print("All calculator checks passed.")