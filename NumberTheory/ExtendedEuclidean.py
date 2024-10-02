def extended_euclidean(a,b):
    '''
    Returns a tuple (x,y,g) which satisfies ax+by=g for given two integers a and b where g is the GCD
    of a and b
    Args:
        a, b - Integers to find GCD
    Returns:
        Tuple (x,y,g)
    '''
    if b == 0:
        return (1,0,a)
    
    t_int = extended_euclidean(b, a%b)

    return (t_int[1], t_int[0]-(a//b)*t_int[1], t_int[2])

if __name__ == "__main__":
    a, b = map(int, input().split())
    gcd = extended_euclidean(a, b)[2]
    print(f"GCD of {a} and {b} is {gcd}")