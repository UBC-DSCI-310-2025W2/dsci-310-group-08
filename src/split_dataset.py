import pandas as pd
from sklearn.model_selection import train_test_split


def split_dataset(data_frame, target_col, test_size=0.2, random_state=None):
    """
    Split a pandas DataFrame into train and test sets by target column.

    Separates the input DataFrame into features (X) and target (y), then splits each 
    into training and test sets using sklearn's train_test_split.

    Parameters
    ----------
    data_frame : pandas.DataFrame
        The input DataFrame containing both features and the target column.
    target_col : str
        The name of the column in data_frame to use as the target (y).
    test_size : float, optional
        Proportion of the dataset to include in the test split.
        Must be between 0 and 1 (exclusive). Default is 0.2.
    random_state : int or None, optional
        Controls the shuffling for reproducible output. Default is None.

    Returns
    -------
    tuple of pandas.DataFrame
        A tuple (X_train, X_test, y_train, y_test) where:
        - X_train : training features DataFrame
        - X_test  : test features DataFrame
        - y_train : training target Series (as DataFrame with one column)
        - y_test  : test target Series (as DataFrame with one column)

    Raises
    ------
    TypeError
        If data_frame is not a pandas DataFrame.
    ValueError
        If target_col is not a column in data_frame.
    ValueError
        If test_size is not strictly between 0 and 1.
    """
    if not isinstance(data_frame, pd.DataFrame):
        raise TypeError("data_frame must be a pandas DataFrame.")

    if target_col not in data_frame.columns:
        raise ValueError(
            f"target_col '{target_col}' is not a column in data_frame. "
            f"Available columns: {list(data_frame.columns)}"
        )

    if not (0 < test_size < 1):
        raise ValueError(
            f"test_size must be between 0 and 1 (exclusive), got {test_size}."
        )

    X = data_frame.drop(columns=[target_col])
    y = data_frame[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    return X_train, X_test, y_train, y_test