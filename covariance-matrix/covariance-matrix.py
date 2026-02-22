import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.array(X, dtype=float)

    if X.shape[0] < 2 or X.ndim != 2:
        return None

    x_centetred = X - np.mean(X, axis=0)

    covar_matrix = (x_centetred.T @ x_centetred)/(X.shape[0]-1)

    return covar_matrix
    