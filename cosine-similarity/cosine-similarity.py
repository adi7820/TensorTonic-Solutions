import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    dot_prod = np.dot(a, b)
    a_mag = np.linalg.norm(a)
    b_mag = np.linalg.norm(b)

    if a_mag == 0 or b_mag == 0:
        return 0.0

    return dot_prod/(a_mag*b_mag)
    