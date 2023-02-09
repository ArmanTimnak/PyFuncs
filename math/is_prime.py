def is_prime(num: int) -> bool: 
    if num<=1: 
        return False # If num is less than or equal to 1 then it's not prime, so is_prime returns False
    for i in range(2,num): # For all numbers between 2 and num, check if num is divisible by any of those numbers
        if num % i == 0:
            return False # If num is divisible by any of those numbers, then it's not prime, so is_prime returns False
    return True # If none of the numbers between 2 and num cant be divided by num, then num is prime, so is_prime returns True
