import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    df = pd.DataFrame(data)

    # print(df.to_json(orient='index'))

    return {"data": data, "shape": list(df.shape), "columns": list(df.columns)}