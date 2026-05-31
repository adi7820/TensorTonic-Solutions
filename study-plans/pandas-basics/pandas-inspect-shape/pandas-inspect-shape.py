import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)

    rows, cols = df.shape

    print(df.dtypes.to_dict())

    dtypes = {col: str(dt) for col, dt in df.dtypes.to_dict().items()}

    return {"rows": rows, "cols": cols, "columns": df.columns.tolist(), "dtypes": dtypes, "total_values": rows*cols}