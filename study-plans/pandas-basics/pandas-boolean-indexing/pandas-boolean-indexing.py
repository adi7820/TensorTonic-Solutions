import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)

    filtered_df = df[df[column] > threshold]

    return {"filtered_data": filtered_df.to_dict("list"), "count": len(filtered_df)}