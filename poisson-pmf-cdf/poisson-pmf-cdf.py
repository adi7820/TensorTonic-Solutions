import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    def factorial(n):
        if n == 0:
            return 1
        return np.prod(np.arange(1, n+1))
        
    pmf = (np.exp(-lam)*(lam**k))/factorial(k)

    cdf = 0.0
    for i in range(k + 1):
        cdf += (np.power(lam, i) * np.exp(-lam)) / factorial(i)

    return pmf, cdf