# The factorial of a number is the product of all the numbers from 1 to n.
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.

# The function uses recursion to calculate the factorial.
# Recursion is when a function calls itself.

def factorial(n): # The function takes in a number n and returns the factorial of n.
  if n == 0:
    return 1 # The function will return 1 if n is equal to 0.
  else:
    return n * factorial(n-1) # The function will return n times the factorial of n minus 1 if n is not equal to 0.