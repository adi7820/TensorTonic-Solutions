import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    df_clean = df.drop_duplicates()
    return [df.shape[0], df_clean.shape[0], df_clean.to_dict('list')]