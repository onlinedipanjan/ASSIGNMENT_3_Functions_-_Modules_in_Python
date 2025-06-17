# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.
 
# Expected Output:
# For example, if the function is called with 5, it should return:




input_1 = input("Enter your number: ")

# Check if the input is a valid integer
try:
    input_1 = int(input_1)
except ValueError:
    print("Please enter a valid integer.")
    exit()

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

sample_number = input_1
output = factorial(sample_number)
print(f"The factorial of {sample_number} is: {output}")


# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.
#  Expected Output:
#  For example, if the user enters 25, the output should be:


import math  # this is math module without this module it is not working.


input_number = float(input("Enter a number: "))

sqrt_result = math.sqrt(input_number)
log_result = math.log(input_number)
sine_result = math.sin(input_number)

print(f"Square root: {sqrt_result}")
print(f"logarithm: {log_result}")
print(f"Sine: {sine_result}")