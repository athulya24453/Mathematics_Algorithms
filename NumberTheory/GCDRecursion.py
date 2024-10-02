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

if __name__ == "__main__":
    a, b = map(int, input().split())
    gcd = gcd_rec(a,b)
    print(f"GCD of {a} and {b} is {gcd}")