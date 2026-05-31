import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)

    return [df.iloc[row, col], df.iloc[row], df.iloc[:,col]]