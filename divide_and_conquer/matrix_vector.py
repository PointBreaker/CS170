import numpy as np
def matrix_vector(v, n):
    """
    vector is a length n vector
    n = pow(2, i), i is positive integer
    return Hadamard matrix of dimension n, times vector
    >>> v = [1, -1, -1, 1]
    >>> matrix_vector(v, 4)
    [0, 0, 0, 4]
    >>> v = [1, 2, 3, 4]
    >>> matrix_vector(v, 4)
    [10, -2, -4, 0]
    """
    if n == 1:
        return v
    v1 = v[: n // 2]
    v2 = v[n // 2:]
    return matrix_vector(list(np.array(v1) + np.array(v2)), n // 2) + matrix_vector(list(np.array(v1) - np.array(v2)), n // 2)