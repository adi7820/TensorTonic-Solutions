import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    df = pd.DataFrame(data)

    gsum = df.groupby(group_col)[value_col].sum()
    gmean = df.groupby(group_col)[value_col].mean()
    gcount = df.groupby(group_col)[value_col].count()
    
    return {"sum":gsum.to_dict(), "mean": gmean.to_dict(), "count": gcount.to_dict()}

    
    