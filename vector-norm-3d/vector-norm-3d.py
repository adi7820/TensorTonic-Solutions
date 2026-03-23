import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    v = np.array(v)

    if v.ndim == 1:
        # Single vector: sqrt(x² + y² + z²)
        return np.sqrt(np.sum(v**2))
    else:
        # Batch: har row ka norm, axis=1 matlab har vector ke across
        return np.sqrt(np.sum(v**2, axis=1))