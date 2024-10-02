def SieveOfEratosthenes(n):
    '''
    Returns an array consisting the information about whether a number is a prime.
    Args:
        n - upper bound
    Returns:
        Array with 1 if the number corresponding to the index is not a prime and 0 if a prime
    '''
    sieve = [0 for i in range(n+1)]
    for i in range(2,n+1):
        if not sieve[i]:
            for j in range(2*i,n+1,i):
                sieve[j] = 1

    return sieve

if __name__ == "__main__":
    n = int(input()) # Upper bound of the sieve
    m = int(input()) # Number to check
    assert m<n, "m should be less than n"
    print(f"{m} is not a prime" if SieveOfEratosthenes(n)[m] else f"{m} is a prime")