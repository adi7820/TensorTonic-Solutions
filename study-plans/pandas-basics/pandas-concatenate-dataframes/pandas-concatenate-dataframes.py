import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    dfs = [pd.DataFrame(tdf) for tdf in dfs]
    df = pd.concat(dfs, axis=0, ignore_index=True)

    return [list(df.shape), df.to_dict("list")]