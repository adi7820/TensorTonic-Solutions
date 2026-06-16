import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    if method == "zeros":
        res = torch.zeros(shape).tolist()
    elif method == "ones":
        res = torch.ones(shape).tolist()
    elif method == "full":
        res = torch.full(shape, value).tolist()

    return res