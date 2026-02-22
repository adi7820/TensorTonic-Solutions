import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    X = np.array(X, dtype=float)
    if X.ndim != 2:
        return None

    if X.shape[0] < 2:
        return None

    X_centered = X - np.mean(X, axis=0)

    n = X.shape[0]

    cov_matrix = (X_centered.T @ X_centered) / (n - 1)

    std_dev = np.sqrt(np.diag(cov_matrix))

    denom = np.outer(std_dev, std_dev)

    corr_matrix = np.full_like(cov_matrix, np.nan)

    valid = denom != 0
    corr_matrix[valid] = cov_matrix[valid] / denom[valid]

    for i in range(len(std_dev)):
        if std_dev[i] != 0:
            corr_matrix[i, i] = 1.0
        else:
            corr_matrix[i, i] = np.nan

    return corr_matrix
        