import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    if not isinstance(matrix, (list, tuple)) or len(matrix) == 0:
        return None

    # 2️⃣ Must be 2D (list of lists)
    if not all(isinstance(row, (list, tuple)) for row in matrix):
        return None

    # 3️⃣ Rectangular check
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        return None
    matrix = np.asarray(matrix, dtype=float)

    if matrix.shape[0] != matrix.shape[1] or matrix.ndim != 2:
        return None

    eigen = np.linalg.eigvals(matrix)

    return eigen