def collatz_seq(starting_num): # The function collatz_seq takes in a starting number and returns a list of numbers that are part of the collatz sequence.
    collatz_seq_list = [] # The function first creates an empty list called collatz_seq_list.
    
    collatz_seq_list.append(starting_num) # The function then appends the starting number to the list.

    while collatz_seq_list[-1] != 1: # The function then enters a while loop that will continue until the last number in the list is 1.
        if collatz_seq_list[-1] % 2 == 0: # The function then checks if the last number in the list is even or odd.
            collatz_seq_list.append(collatz_seq_list[-1]//2) # If the last number in the list is even, the function divides the last number by 2 and appends the result to the list.
        else:
            collatz_seq_list.append(collatz_seq_list[-1]*3+1) # If the last number in the list is odd, the function multiplies the last number by 3 and adds 1 to the result and appends the result to the list.
    return collatz_seq_list # The function then returns the list.
