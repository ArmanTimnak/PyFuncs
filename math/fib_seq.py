# The fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers.
# The first two numbers in the sequence are 0 and 1.

def fib_seq(n): # The function fib_seq takes in a number n and returns the n'th number in the fibonacci sequence.
    if n<0: 
        print("Incorrect input") 
    elif n==1: # When n is equal to 1, the function returns 0.
        return 0
    elif n==2: # When n is equal to 2, the function returns 1.
        return 1
    else: 
        return fib_seq(n-1)+fib_seq(n-2) 
