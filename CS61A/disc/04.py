def max_product(s):
    if s==[]:
        return 1
    if len(s)==1:
        return s[0]
    if len(s)==2:
        return max(s)
    return max(max_product(s[2::])*s[0],max_product(s[1::]))
#print(max_product([5,10,5,10,5]))
def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0:
        sums_to_zero = []     # The only way to sum to zero using positives
        return [sums_to_zero] # Return a list of all the ways to sum to zero
    result = []
    for k in range(1, m + 1):#set the first one.Reasonale!
        result = result + [[k]+rest for rest in sums(n-k,m) if rest == [] or rest[0]!=k ]
    return result
print(sums(5,1),sums(5,2),sums(5,3))