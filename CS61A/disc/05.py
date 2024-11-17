def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if p == [label(t)]:  # when len(p) is 1
        return True
    elif label(t) != p[0]:
        return False
    else:
        "*** YOUR CODE HERE ***"
        for i in branches(t):
            if has_path(i,p[1:]):
                return True
        else:
            return False
# t2 = tree(5, [tree(6), tree(7)])
# t1 = tree(3, [tree(4), t2])
# print(has_path(t1, [5, 6]),has_path(t2, [5, 6]),has_path(t1, [3, 5]),has_path(t1, [3, 4, 5, 6]))
def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if x==label(t):#really understand the base condition!
        return [label(t)]
    else:
        path =[find_path(i,x) for i in branches(t) if find_path(i,x)]
        if path:
            return [label(t)]+path[0]
    return None
t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])
print(find_path(t1, 5),find_path(t1, 4),find_path(t1, 6),find_path(t2, 6))
print(find_path(t1, 2))