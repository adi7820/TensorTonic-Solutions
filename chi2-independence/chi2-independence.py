import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C = np.array(C)
    rows = np.sum(C, axis=1)
    cols = np.sum(C, axis=0)
    total = np.sum(C)

    E = np.outer(rows, cols)/total
    print(E)

    res = np.sum((C - E)**2/E)

    return res, E