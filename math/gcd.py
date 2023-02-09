# This function finds the greatest common divisor of the two numbers a and b  

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
