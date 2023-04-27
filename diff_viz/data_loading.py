"""
Module for ensuring the validity of uploaded CSV files.
"""

import pandas as pd
import numpy as np

def check_csv_data(df, expected_columns):
    """
    Checks that a pandas DataFrame has at least one row of data and contains specific columns.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The DataFrame to check.
    expected_columns : list
        A list of column names that the DataFrame is expected to have.
        
    Returns:
    --------
    bool
        True if the DataFrame contains at least one row of data and all of the expected columns, False otherwise.
    """
    # Check that all of the expected columns are present
    columns_present = all(col in df.columns for col in expected_columns)
    
    # Check that the DataFrame has at least one row of data
    has_data = not df.empty
    
    # Return True if both the expected columns and data are present
    return columns_present and has_data
