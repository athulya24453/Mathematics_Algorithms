def extended_sieve(n):
    '''
    Returns an array consisting the smallest prime factor of each integer upto n
    Args:
        n - upper bound
    Returns:
        Array with smallest prime factors
    '''
    sieve = [0 for i in range(n+1)]

    for i in range(2, n+1):
        if not sieve[i]:
            for j in range(2*i,n+1,i):
                sieve[j] = i

    return sieve

if __name__ == "__main__":
    n = int(input()) # Upper bound for the sieve
    m = int(input()) # Integer to check
    assert m<n, "m should be less than n"
    print(f"{m}'s smallest prime factor is {extended_sieve(n)[m]}")