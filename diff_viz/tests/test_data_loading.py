"""
This file contains unit tests for the data_loading module.
"""
import pandas as pd
import numpy as np
from hypothesis import HealthCheck, given, settings, strategies as st
from hypothesis.extra.pandas import columns, column, data_frames, range_indexes

from diff_viz.data_loading import check_mpt_data, clean_mpt_data


np.random.seed(1234)
param = {}
categories = ['alpha', 'D_fit', 'kurtosis', 'asymmetry1', 'asymmetry2',
            'asymmetry3', 'AR', 'elongation', 'boundedness', 'fractal_dim',
            'trappedness', 'efficiency', 'straightness', 'MSD_ratio',
            'frames', 'Deff1', 'Deff2', 'angle_mean', 'angle_mag_mean',
            'angle_var', 'dist_tot', 'dist_net', 'progression',
            'Mean alpha', 'Mean D_fit', 'Mean kurtosis', 'Mean asymmetry1',
            'Mean asymmetry2', 'Mean asymmetry3', 'Mean AR',
            'Mean elongation', 'Mean boundedness', 'Mean fractal_dim',
            'Mean trappedness', 'Mean efficiency', 'Mean straightness',
            'Mean MSD_ratio', 'Mean Deff1', 'Mean Deff2']


data_cols = columns(names_or_number=categories, dtype=float, elements=st.floats())
position_cols = columns(names_or_number=['X', 'Y'], dtype=float, elements=st.floats(min_value=0.0, max_value=2048.0))
target_col = column(name='target', dtype=int, elements=st.integers(min_value=0, max_value=20)) #up to twenty unique targets

df = data_frames(columns=data_cols + position_cols + [target_col], index=range_indexes(min_size=10))


@given(df)
@settings(suppress_health_check=[HealthCheck.large_base_example, HealthCheck.too_slow])
def test_check_mpt_data(df):
    # Create a DataFrame with the expected columns and data


    expected_columns = categories

    # Test the function with the expected DataFrame
    assert check_mpt_data(df, expected_columns=expected_columns) is True

    # Test the function with a DataFrame that is missing a column
    assert check_mpt_data(df.drop(columns='trappedness'), expected_columns) is False


    # Test the function with an empty DataFrame
    assert check_mpt_data(pd.DataFrame(), expected_columns) is False

@given(df)
@settings(suppress_health_check=[HealthCheck.large_base_example, HealthCheck.too_slow])
def test_clean_mpt_data(df):

    assert clean_mpt_data(df) is not None #check that the function returns a DataFrame  
    
    # check the first if statement
    assert clean_mpt_data(df, features_to_keep='default', target_column=None).shape[1] == 32 #check that the function returns a DataFrame with 40 columns
    # check the first elif statement
    assert clean_mpt_data(df, features_to_keep='default', target_column='target').shape[1] == 33 #check that the function returns a DataFrame with 41 columns  
    # check the second elif statement
    subset_df = clean_mpt_data(df, features_to_keep=['alpha', 'asymmetry1', 'Mean MSD_ratio', 'AR', 'Mean Deff1'], target_column=None)
    assert subset_df.shape[1] == 5 #check that the function returns a DataFrame with 5 columns   
    assert all(element in subset_df.columns for element in ['alpha', 'asymmetry1', 'Mean MSD_ratio', 'AR', 'Mean Deff1']) #check that the function returns a DataFrame with 5 columns   

    # check the else statement
    else_df = clean_mpt_data(df, features_to_keep=['alpha', 'asymmetry1', 'Mean MSD_ratio', 'AR', 'Mean Deff1'], target_column='target')
    assert else_df.shape[1] == 6 #check that the function returns a DataFrame with 6 columns
    assert all(element in else_df.columns for element in ['alpha', 'asymmetry1', 'Mean MSD_ratio', 'AR', 'Mean Deff1', 'target']) #check that the function returns a DataFrame with 6 columns