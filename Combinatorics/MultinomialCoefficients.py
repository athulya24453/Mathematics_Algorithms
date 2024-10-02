from math import prod

def multinomial_coefficient(n, ks):
    '''
    Computes number of ways to partition n objects into k distinct groups, with specified sizes
    Args:
        n - Number of elements in the set
        ks - Array consisting the number of elements in each group
    Returns:
        Number of distinct groups
    '''
    if sum(ks) != n:
        raise ValueError("The sum of the group sizes must equal n.")
    
    result = 1
    ks = sorted(ks, reverse=True)  # Sorting can help minimize intermediate values
    total = n
    
    for k in ks:
        for i in range(k):
            result *= total
            result //= (i + 1)
            total -= 1

    return result

if __name__ == "__main__":
    n = int(input())
    ks = list(map(int, input().split()))
    print(multinomial_coefficient(n, ks))