import pandas as pd

def find_measurement_last_time(data_frame: pd.DataFrame, time_col: str, group_col: str, measurement_col: str):
    """
    Finds the previous time period's measurement for a given group and adds it as a new column
    called `{measurement_col}_last_time` in the data frame.
    
    This function sorts the data by the group variable and time (i.e., year), 
    then shifts the specified measurement column by one period within each group 
    to find the previous measurement value. It fills any missing values 
    (usually the first period of a group) with the current period's measurement.
    
    We explicitly request that the measurement column does not have any missing data
    as it is the target variable. If there are any missing values in the measurement
    column, the function will raise a ValueError.

    Parameters:
    ----------
    data_frame : pandas.DataFrame
        The input DataFrame containing the data to analyze.
    time_col : str
        The name of the column representing the time (i.e., 'year') for sorting
    group_col : str
        The name of the group column (i.e., 'city')
    measurement_col : str
        The name of the column containing the measurement value (i.e., `rank`) 
        (should not have NAs).

    Returns:
    -------
    pandas.DataFrame
        A DataFrame with one more column that the original DataFrame:
        The returned DataFrame should have this additional column:
        - '{measurement_col}_last_time': 
            the previous time period's measurement for a given group
        
    Examples:
    --------
    >>> import pandas as pd
    >>> data_raw = pd.read_csv('example_data.csv') 
    >>> data_processed = find_measurement_last_time(data_raw, 'year', 'city', 'rank')
    >>> print(data_processed)

    Notes:
    -----
    This function uses the pandas library to perform the task.

    """
    if data_frame[measurement_col].isna().any():
        raise ValueError("The measurement column should not have any missing values.")
    
    # Sort by group and time columns to ensure accurate shifting and ordering
    data_frame_processed = data_frame.sort_values([group_col, time_col])
    
    # Define the new column name 
    new_col_name = f"{measurement_col}_last_time"
    
    # Shift the measurement with respect to time within each group
    data_frame_processed[new_col_name] = data_frame_processed.groupby(group_col)[measurement_col].shift(1)
    
    # Fill NaNs (first instances) with the current time's measurement
    data_frame_processed[new_col_name] = data_frame_processed[new_col_name].fillna(data_frame_processed[measurement_col])
    
    return data_frame_processed