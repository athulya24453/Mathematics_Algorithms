def inclusion_exclusion(sets):
    '''
    Finds the size of elements in the union of sets
    Args:
        sets - Array of all sets
    Returns:
        Number of elements in the union
    '''
    n = len(sets)
    result = 0

    for subset_size in range(1, n+1):
        subsets = generate_subsets(sets, subset_size)
        for subset in subsets:
            intersection_size = count_intersection(subset)
            if subset_size % 2 == 1:
                result += intersection_size
            else:
                result -= intersection_size

    return result

def generate_subsets(sets, subset_size):
    # Helper function to generate all subsets of a given size
    from itertools import combinations
    return list(combinations(sets, subset_size))

def count_intersection(subset):
    # Helper function to count the number of elements in the intersection of the subset
    intersection = subset[0]
    for s in subset[1:]:
        intersection = intersection.intersection(s)
    return len(intersection)

if __name__ == "__main__":
    sets = []
    n = int(input()) # Number of sets

    for _ in range(n):
        A = set(map(int, input().split()))
        sets.append(A)

    print(inclusion_exclusion(sets))