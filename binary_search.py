#!/bin/python3
'''
JOKE: There are 2 hard problems in computer science: cache invalidation, na
ming things, and off-by-1 errors.

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.
    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    def search(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        if xs[mid] <= 0:
            return search(mid + 1, right)
        elif mid == 0 or xs[mid - 1] <= 0:
            return mid
        else:
            return search(left, mid - 1)
    return search(0, len(xs) - 1)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.
    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    def binary_search_left(xs, x):
        low, high = 0, len(xs) - 1
        while low <= high:
            mid = (low + high) // 2
            if xs[mid] < x:
                high = mid - 1
            elif xs[mid] > x:
                low = mid + 1
            else:
                if mid == 0 or xs[mid - 1] != x:
                    return mid
                else:
                    high = mid - 1
        return None

    def binary_search_right(xs, x):
        low, high = 0, len(xs) - 1
        while low <= high:
            mid = (low + high) // 2
            if xs[mid] < x:
                high = mid - 1
            elif xs[mid] > x:
                low = mid + 1
            else:
                if mid == len(xs) - 1 or xs[mid + 1] != x:
                    return mid
                else:
                    low = mid + 1
        return None
    left_index = binary_search_left(xs, x)
    right_index = binary_search_right(xs, x)
    if left_index is None or right_index is None:
        return 0
    return right_index - left_index + 1


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and ret
    urns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x
    ) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest,
               you recursively call your function on the interval [lo,m2] or
               [m1,hi]

    APPLICATION:
    Essentially all data mining algorithms are just this argmin implementati
    on in disguise.
    If you go on to take the data mining class (CS145/MATH166),
    we will spend a lot of time talking about different f functions that can
    be minimized and their applications.
    But the actual minimization code will all be a variant of this binary s
    earch.

    WARNING:
    The doctests below are not intended to pass on your code,
    and are only given so that you have an example of what the output should
    look like.
    Your output numbers are likely to be slightly different due to minor im
    plementation details.
    Writing tests for code that uses floating point numbers is notoriously
    difficult.
    See the pytests for correct examples.

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    if hi - lo < epsilon:
        return (lo + hi) / 2
    else:
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            return argmin(f, lo, m2, epsilon)
        else:
            return argmin(f, m1, hi, epsilon)

###########################################################################
#####
# the functions below are extra credit
############################################################################
####


def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    If f is a convex function, then the minimum is guaranteed to be between
    lo and hi.
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo=-1, hi=1.
    Let mid = (lo+hi)/2
    if f(lo) > f(mid):
        recurse with lo*=2
    elif f(hi) < f(mid):
        recurse with hi*=2
    else:
        you're done; return lo,hi
    '''


def argmin_simple(f, epsilon=1e-3):
    '''
    This function is like argmin, but it internally uses the find_boundaries
    function so that
    you do not need to specify lo and hi.

    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)
