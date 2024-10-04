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

def catalan_numbers(n):
    return binomial_coefficients(2*n, n)//(n+1)

if __name__ == "__main__":
    n = int(input())
    print(f"{n}th catalan number is {catalan_numbers(n)}")