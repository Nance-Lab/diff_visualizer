"""
This file contains unit tests for the data_loading module.
"""

import io
import pandas as pd
from diff_viz.data_loading import check_csv_data

def test_check_csv_data():
    # Create a DataFrame with the expected columns and data
    expected_columns = ['name', 'age', 'gender']
    data = [['Alice', 25, 'F'], ['Bob', 30, 'M']]
    df = pd.DataFrame(data, columns=expected_columns)

    # Test the function with the expected DataFrame
    assert check_csv_data(df, expected_columns) == True

    # Test the function with a DataFrame that is missing a column
    assert check_csv_data(df.drop(columns='age'), expected_columns) == False

    # Test the function with a DataFrame that has extra columns
    extra_columns = expected_columns + ['occupation']
    assert check_csv_data(df.assign(occupation=['doctor', 'teacher']), expected_columns) == True

    # Test the function with an empty DataFrame
    assert check_csv_data(pd.DataFrame(), expected_columns) == False

