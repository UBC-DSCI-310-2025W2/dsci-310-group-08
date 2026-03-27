import pytest
import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import Ridge
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
import sys
import os

# Import the get_model_coefficients function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.get_model_coefficients import get_model_coefficients

# Setting up a minimal fitted pipeline
@pytest.fixture
def fitted_pipe():
    """A minimal fitted pipeline for testing."""
    X = pd.DataFrame({
        'color': ['red', 'blue', 'red', 'blue'],
        'size': [1.0, 2.0, 3.0, 4.0]
    })
    y = pd.Series([10.0, 20.0, 30.0, 40.0])

    preprocessor = make_column_transformer(
        (OneHotEncoder(handle_unknown='ignore'), ['color']),
        ('passthrough', ['size'])
    )
    pipe = make_pipeline(preprocessor, Ridge())
    pipe.fit(X, y)
    return pipe


# Simple case 1: check output is a DataFrame with correct columns
def test_returns_dataframe_with_correct_columns(fitted_pipe):
    """
    Tests that the get_model_coefficients() function returns a DataFrame with 
    'feature' and 'coefficient' columns.
    """
    result = get_model_coefficients(fitted_pipe)
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == ['feature', 'coefficient']

# Simple case 2: check coefficients are sorted by absolute value in descending order
def test_sorted_by_absolute_coefficient(fitted_pipe):
    """
    Test that coefficients are sorted by absolute value in descending order.
    """
    result = get_model_coefficients(fitted_pipe)
    abs_coefs = result['coefficient'].abs().tolist()
    assert abs_coefs == sorted(abs_coefs, reverse=True)

# Simple case 3: check that OHE and passthrough prefixes are stripped from feature names
def test_prefixes_removed(fitted_pipe):
    """
    Test that 'onehotencoder__' and 'passthrough__' prefixes are 
    stripped from feature names.
    """
    result = get_model_coefficients(fitted_pipe)
    assert not any(result['feature'].str.startswith('onehotencoder__'))
    assert not any(result['feature'].str.startswith('passthrough__'))

# Sample pipeline for edge case
@pytest.fixture
def fitted_pipe_numerical_only():
    """A fitted pipeline with only numerical features (no OHE)."""
    X = pd.DataFrame({
        'size': [1.0, 2.0, 3.0, 4.0],
        'weight': [5.0, 6.0, 7.0, 8.0]
    })
    y = pd.Series([10.0, 20.0, 30.0, 40.0])
    preprocessor = make_column_transformer(
        ('passthrough', ['size', 'weight'])
    )
    pipe = make_pipeline(preprocessor, Ridge())
    pipe.fit(X, y)
    return pipe

# Edge case: pipeline with no categorical features (no OHE), only passthrough
def test_numerical_only_pipeline(fitted_pipe_numerical_only):
    """
    Test that the function handles a pipeline with only numerical 
    features with a 'passthrough' transformer.
    """
    result = get_model_coefficients(fitted_pipe_numerical_only)
    assert isinstance(result, pd.DataFrame)
    assert not any(result['feature'].str.startswith('passthrough__'))

# Error case: check that a TypeError is raised when input is not a Pipeline
def test_raises_type_error_on_non_pipeline():
    """
    Test that a TypeError is raised when the input is not a sklearn 
    Pipeline instance.
    """
    with pytest.raises(TypeError):
        get_model_coefficients("not a pipeline")