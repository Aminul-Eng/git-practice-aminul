from datetime import date

from utils import add, subtract, multiply, divide


print("Name: Aminul Islam")
print("Today's date:", date.today())

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))


try:
    print("Division:", divide(10, 5))
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    divide(10, 0)
except ZeroDivisionError:
    print("Error handled: Cannot divide by zero.")


# Basic calculator checks
assert add(10, 5) == 15
assert subtract(10, 5) == 5
assert multiply(10, 5) == 50

print("All calculator checks passed.")