import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v, dtype=float)

    if v.ndim == 1:
        norm = np.sqrt(np.sum(v**2))
        if norm == 0:
            return v  # zero vector → zero return karo
        return v / norm

    else:
        # Batch case
        norms = np.sqrt(np.sum(v**2, axis=1, keepdims=True))  # shape (N,1)
        norms[norms == 0] = 1  # zero vectors ke norm ko 1 karo (divide se bachao)
        return v / norms