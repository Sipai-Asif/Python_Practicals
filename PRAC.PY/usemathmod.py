'''5 Write a Python program that uses the math module to: 
    Greet the user before calculation
    Find the square root of a number
    Find the power of a number
    Display the value of π
    Greeting the user after calculation.'''

import math

# Greeting before calculation
print("Hello! Welcome to the math program.")

# Input number for square root
num = float(input("Enter a number to find its square root: "))
sqrt_num = math.sqrt(num)
print("Square root of", num, "is", sqrt_num)

# Input numbers for power calculation
base = float(input("Enter the base number: "))
exp = float(input("Enter the exponent: "))
power = math.pow(base, exp)
print(base, "raised to the power", exp, "is", power)

# Display the value of π
print("The value of π is:", math.pi)

# Greeting after calculation
print("Thank you for using the math program. Goodbye!")