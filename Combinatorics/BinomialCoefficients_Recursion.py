def binomial_coefficients(n, k):
    '''
    Computes n choose k
    Args:
        n, k - Integers
    Returns:
        nck
    '''
    if k == 0 or k == n:
        return 1
    
    return binomial_coefficients(n-1, k-1) + binomial_coefficients(n-1, k)

if __name__ == "__main__":
    n, k = map(int, input().split())
    nck = binomial_coefficients(n, k)
    print(f"{n}c{k} = {nck}")