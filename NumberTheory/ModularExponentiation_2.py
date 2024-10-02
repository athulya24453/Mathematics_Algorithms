def modular_exponentiation(a, n, m):
    '''
    Calculates a^n (mod m) in O(log n) time
    Args:
        a,n,m - Integers
    Returns:
        a^n (mod m)
    '''
    if n == 0:
        return 1 % m
    u = modular_exponentiation(a, n // 2, m)
    u = (u * u) % m
    if n % 2 == 1:
        u = (u * a) % m
    return u

def gcd_rec(a,b):
    '''
    Returns the GCD of two numbers
    Args:
        a,b - Integers to find GCD
    Returns:
        The GCD of a and b
    '''
    if b == 0:
        return a
    
    return gcd_rec(b, a%b)

def modular_exponentiation_2(a, n, m):
    '''
    Returns a^n (mod m) for very large n. a and m must be a coprime pair.
    Args:
        a, n, m - Integers

    Return:
        a^n (mod m)
    '''
    assert gcd_rec(a, m) == 1, "a and m must be a coprime pair"
    return modular_exponentiation(a, n%(m-1), m)

if __name__ == "__main__":
    a, n, m = map(int, input().split())
    pow_ans = modular_exponentiation_2(a,n,m)
    print(f"{a}^{n} (mod {m}) = {pow_ans}")