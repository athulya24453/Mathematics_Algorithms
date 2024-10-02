import math

def IsPrime(n):
    '''
    A O(sqrt(n)) time algorithm to check whether a given number is a prime
    Args:
        n - Number

    Returns:
        True if prime, False if not
    '''
    prime = True

    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            prime = False
            break

    return prime

if __name__ == "__main__":
    n = int(input())
    print(f"{n} is a prime" if IsPrime(n) else f"{n} is not a prime")