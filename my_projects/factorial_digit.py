# Importing necessary function from math library
import math
from math import ceil, factorial

# Defining factorial function to calculate factorial of ceil value of a float
def float_ceil_factorial(n):
    fac = 0
    if n > 0:
        fac = factorial(n)
    else:
        fac = -1
    return fac

# Taking input from user
n = math.ceil(float(input()))

# Calling the function with the user input
output = float_ceil_factorial(n)

# Printing the output
print(output)
