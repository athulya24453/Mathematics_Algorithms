import math

def prime_factors(n):
    '''
    Given an integer, returns an array consisiting of its prime factors. The number of occurances of
    of an integer in the array is equal to the power of that integer in the prime factorization.
    Args:
        n - Number
    Returns:
        f - Prime Factor Array
    '''
    f = []
    
    x = 2
    while x * x <= n:
        while n % x == 0:
            f.append(x)
            n //= x
        x += 1
    if n > 1:
        f.append(n)
    return f

if __name__ == "__main__":
    n = int(input())
    print(prime_factors(n))