import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    cols_before = df.columns.tolist()
    df = df.reset_index()
    after_cols = df.columns.tolist()
    return [cols_before, after_cols]
    