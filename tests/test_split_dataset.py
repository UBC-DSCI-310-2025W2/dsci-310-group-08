import pytest 
import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.split_dataset import split_dataset 


# =============
# SAMPLE DATA
# =============

# A standard DataFrame that mirrors our project's structure: feature columns + a numeric target 
standard_df = pd.DataFrame(
    {
        "city": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
        "year": [2015, 2016, 2017, 2018, 2019, 2015, 2016, 2017, 2018, 2019],
        "park_pct_city_points": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        "spend_per_resident_points": [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],
        "rank": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }
)

# A minimal DataFrame with just enough rows to split (5 rows, 20% test = 1 row)
minimal_df = pd.DataFrame(
    {
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [10, 20, 30, 40, 50],
        "rank": [100, 90, 80, 70, 60],
    }
)

# ===============================
# SIMPLE EXPECTED USE TEST CASES 
# ===============================

# SIMPLE: correct sizes, target not in X, y contains right values, reproducibility, no rows lost

def test_split_returns_four_objects():
    """
    split_dataset should return a tuple of exactly four objects.
    """
    result = split_dataset(standard_df, "rank", test_size=0.2, random_state=73)
    assert len(result) == 4

def test_split_sizes_are_correct():
    """
    With test_size=0.2 and 10 rows, we expect 8 train rows and 2 test rows.
    """
    X_train, X_test, y_train, y_test = split_dataset(
        standard_df, "rank", test_size=0.2, random_state=73
    )
    assert len(X_train) == 8
    assert len(X_test) == 2
    assert len(y_train) == 8
    assert len(y_test) == 2

def test_target_col_not_in_X():
    """
    The target column ('rank') should not appear in X_train or X_test.
    """
    X_train, X_test, y_train, y_test = split_dataset(
        standard_df, "rank", test_size=0.2, random_state=73
    )
    assert "rank" not in X_train.columns
    assert "rank" not in X_test.columns

def test_y_contains_only_target_values():
    """
    y_train and y_test should be pandas Series containing only values from the target column.
    """
    X_train, X_test, y_train, y_test = split_dataset(
        standard_df, "rank", test_size=0.2, random_state=73
    )
    assert isinstance(y_train, pd.Series)
    assert isinstance(y_test, pd.Series)
    assert set(y_train).issubset(set(standard_df["rank"]))
    assert set(y_test).issubset(set(standard_df["rank"]))

def test_all_rows_accounted_for():
    """
    The total rows across train and test sets should equal the original number of rows.
    """
    X_train, X_test, y_train, y_test = split_dataset(
        standard_df, "rank", test_size=0.2, random_state=73
    )
    assert len(X_train) + len(X_test) == len(standard_df)


# ==================
# EDGE TEST CASES
# ==================

def test_minimal_dataframe_splits():
    """
    A DataFrame with only 5 rows should still split without error,
    producing non-empty train and test sets.
    """
    X_train, X_test, y_train, y_test = split_dataset(
        minimal_df, "rank", test_size=0.2, random_state=42
    )
    assert len(X_train) > 0
    assert len(X_test) > 0

def test_equal_split():
    """
    A test_size of 0.5 should produce equal-sized train and test sets
    for a 10-row DataFrame.
    """
    X_train, X_test, y_train, y_test = split_dataset(
        standard_df, "rank", test_size=0.5, random_state=73
    )
    assert len(X_train) == 5
    assert len(X_test) == 5

# ============================================================
# ERROR TEST CASES
# ============================================================

def test_non_dataframe_input_raises_type_error():
    """
    Passing a list instead of a DataFrame should raise a TypeError.
    """
    with pytest.raises(TypeError):
        split_dataset([[1, 2, 3], [4, 5, 6]], "rank")

def test_missing_target_col_raises_value_error():
    """
    Passing a target_col that does not exist in the DataFrame should raise a ValueError.
    """
    with pytest.raises(ValueError):
        split_dataset(standard_df, "nonexistent_column")

def test_test_size_zero_raises_value_error():
    """
    test_size=0 is invalid (would produce an empty test set) and should raise a ValueError.
    test_size=0 = 0% of rows go to test set = empty test set, nothing to evaluate your model on
    """
    with pytest.raises(ValueError):
        split_dataset(standard_df, "rank", test_size=0)

def test_test_size_one_raises_value_error():
    """
    test_size=1 is invalid (would produce an empty training set) and should raise a ValueError.
    test_size=1 = 100% of rows go to test set = empty training set, nothing to train your model on
    """
    with pytest.raises(ValueError):
        split_dataset(standard_df, "rank", test_size=1)

def test_test_size_negative_raises_value_error():
    """
    A negative test_size is invalid and should raise a ValueError.
    (a negative proportion doesn't exist)
    """
    with pytest.raises(ValueError):
        split_dataset(standard_df, "rank", test_size=-0.2)