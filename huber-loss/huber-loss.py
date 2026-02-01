import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    error = y_true - y_pred

    abs_error = np.abs(error)
    quardatic = 0.5 * error**2
    linear = delta * (abs_error - 0.5 * delta)

    loss = np.where(abs_error <= delta, quardatic, linear)

    return np.mean(loss)