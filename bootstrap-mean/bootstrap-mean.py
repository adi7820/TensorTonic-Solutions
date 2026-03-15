import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    x = np.array(x)
    n = len(x)

    if rng is None:
        rng = np.random.default_rng()

    indices = rng.choice(n, size=(n_bootstrap, n), replace=True)
    bootstrap_samples = x[indices]

    boot_means = np.mean(bootstrap_samples, axis=1)

    alpha = 1.0 - ci
    lower_percentile = (alpha / 2.0) * 100
    upper_percentile = (1.0 - alpha / 2.0) * 100

    lower = np.percentile(boot_means, lower_percentile)
    upper = np.percentile(boot_means, upper_percentile)

    return boot_means, lower, upper
