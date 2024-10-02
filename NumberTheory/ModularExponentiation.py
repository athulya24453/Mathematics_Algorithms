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
    
if __name__ == "__main__":
    a, n, m = map(int, input().split())
    pow_ans = modular_exponentiation(a, n, m)
    print(f"({a}^{n}) (mod {m}) = {pow_ans}")