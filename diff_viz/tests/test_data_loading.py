"""
This file contains unit tests for the data_loading module.
"""
import pandas as pd
import numpy as np
from diff_viz.data_loading import check_mpt_data, clean_mpt_data, combine_csvs
from hypothesis import HealthCheck, given, settings, strategies as st
from diff_viz.tests.hypothesis_util_functions import hypothesis_features_dataframe

df = hypothesis_features_dataframe()

@given(df)
@settings(suppress_health_check=[HealthCheck.large_base_example, HealthCheck.too_slow])
def test_check_mpt_data(df):
    # Create a DataFrame with the expected columns and data


    expected_columns = df.columns

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


def test_combine_csvs():
    file_list = [
        'diff_viz/tests/testing_data/feature_data/features_P14_40nm_s1_v1.csv',
        'diff_viz/tests/testing_data/feature_data/features_P14_40nm_s1_v2.csv',
        'diff_viz/tests/testing_data/feature_data/features_P14_40nm_s1_v3.csv',
        'diff_viz/tests/testing_data/feature_data/features_P35_brain_2_slice_1_vid_1.csv',
        'diff_viz/tests/testing_data/feature_data/features_P35_brain_2_slice_1_vid_2.csv',
        'diff_viz/tests/testing_data/feature_data/features_P35_brain_2_slice_1_vid_3.csv',
        'diff_viz/tests/testing_data/feature_data/features_P70_40nm_s1_v1.csv',
        'diff_viz/tests/testing_data/feature_data/features_P70_40nm_s1_v2.csv',
        'diff_viz/tests/testing_data/feature_data/features_P70_40nm_s1_v3.csv',
    ]

    def helper_func():
        tot_len = 0
        for file in file_list:
            clean_df = clean_mpt_data(pd.read_csv(file))
            tot_len += len(clean_df)
        return tot_len

    class_list = ['P14', 'P35', 'P70']

    df = combine_csvs(file_list, class_list)

    assert len(df) == helper_func()
    assert len(df.columns) == 33
    assert set(['P14', 'P35', 'P70']).issubset(df['class'].unique())
