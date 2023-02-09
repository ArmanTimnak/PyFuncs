def factors(n: int) -> list:
    factors_list = []
    
    for i in range(1, n+1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list