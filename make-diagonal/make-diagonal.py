import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    res = np.zeros((n, n))

    for i in range(n):
        res[i][i] = v[i]

    return res
