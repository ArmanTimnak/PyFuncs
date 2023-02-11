def gcd(a, b): 
    if a == 0:
        return b 
    if b == 0: 
        return a 
  
    if a == b: 
        return a 
  
    if a > b: 
        return gcd(a-b, b) 
    return gcd(a, b-a)

def factors(n: int) -> list: # The function takes an integer as an argument and returns a list of all the factors of that integer.
    factors_list = [] # The function first creates an empty list.
    
    for i in range(1, n+1): # It then loops through all the numbers from 1 to the number passed as an argument.
        if n % i == 0: # If the number passed as an argument is divisible by the number in the loop, the number in the loop is appended to the list.
            factors_list.append(i)
    return factors_list # The function then returns the list.

# Common factors of two numbers = Factors of gcd of those two numbers  

def common_factors(x, y):
    z = gcd(x, y)
    return factors(z)