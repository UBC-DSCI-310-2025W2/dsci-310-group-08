import pandas as pd
from sklearn.pipeline import Pipeline


def get_model_coefficients(fitted_pipe: Pipeline) -> pd.DataFrame:
    """
    Extracts feature coefficients from a fitted Ridge regression pipeline and returns
    a DataFrame with clean feature names and coefficients in descending order.
    
    The model pipeline must have two steps – ColumnTransformer and the Ridge model.
    The ColumnTransformer is expected to use OneHotEncoder for categorical features and
    'passthrough' for numerical features, as the function strips the 'onehotencoder__' and
    'passthrough__' prefixes from feature names.
    
    Returns a TypeError if the parameter passed is not a sklearn Pipeline instance.
    Returns a ValueError if the pipeline does not contain 'columntransformer' and/or 'ridge' steps.
    
    Parameters
    ----------
    fitted_pipe : sklearn.pipeline.Pipeline
        A fitted pipeline containing a 'columntransformer' step followed by a 'ridge' step.
    
    Returns
    -------
    pd.DataFrame
        A DataFrame with columns 'feature' and 'coefficient', sorted by absolute
        coefficient value in descending order, with transformer prefixes removed
        from feature names.
    
    Examples
    --------
    >>> # Given a fitted sklearn Pipeline with a ColumnTransformer and Ridge step
    >>> coef_df = get_model_coefficients(final_pipe)
    >>> coef_df.head()
    
    Notes:
    --------
    This function uses the pandas and sklearn libraries to perform the task
    
    """
    # validating arguments passed in
    if not isinstance(fitted_pipe, Pipeline):
        raise TypeError("fitted_pipe must be a fitted sklearn Pipeline instance.")
    
    if 'columntransformer' not in fitted_pipe.named_steps:
        raise ValueError("Pipeline must contain a 'columntransformer' step.")
    
    if 'ridge' not in fitted_pipe.named_steps:
        raise ValueError("Pipeline must contain a 'ridge' step.")
    
    # extracting feature names and coefficients
    feature_names = fitted_pipe.named_steps['columntransformer'].get_feature_names_out()
    coefficients = fitted_pipe.named_steps['ridge'].coef_
    
    coef_df = pd.DataFrame({
        'feature': feature_names,
        'coefficient': coefficients
    }).sort_values('coefficient', key=abs, ascending=False)
    
    coef_df['feature'] = (
        coef_df['feature']
        .str.replace('onehotencoder__', '', regex=False)
        .str.replace('passthrough__', '', regex=False)
    )
    # Note: prefixes from other transformers (e.g. 'standardscaler__') will not be removed
    
    return coef_df.reset_index(drop=True)