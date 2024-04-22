"""
Module for ensuring the validity of uploaded CSV files.
"""

import pandas as pd
import numpy as np

# import diff_predictor


def check_mpt_data(df, expected_columns):
    """
    Checks that a pandas DataFrame has at least one row of data and contains specific columns.

    Parameters
    -----------
    df : pandas.DataFrame
        The DataFrame to check.
    expected_columns : list
        A list of column names that the DataFrame is expected to have.

    Returns
    --------
    columns_present, has_data: bool
        True if the DataFrame contains at least one row of data and all of the expected columns,
        False otherwise.
    """
    # Check that all of the expected columns are present
    columns_present = all(col in df.columns for col in expected_columns)
    # Check that the DataFrame has at least one row of data
    has_data = not df.empty

    # Return True if both the expected columns and data are present
    return columns_present and has_data


def clean_mpt_data(df, features_to_keep="default", target_column=None):
    """
    Cleans a pandas DataFrame containing MPT data.

    Parameters
    -----------
    df : pandas.DataFrame
        The DataFrame to clean.

    Returns
    --------
    df: pandas.DataFrame
        The cleaned DataFrame.
    """

    default_feature_list = [
        "alpha",  # Fitted anomalous diffusion alpha exponenet
        "D_fit",  # Fitted anomalous diffusion coefficient
        "kurtosis",  # Kurtosis of track
        "asymmetry1",  # Asymmetry of trajecory (0 for circular symmetric, 1 for linear)
        "asymmetry2",  # Ratio of the smaller to larger principal radius of gyration
        "asymmetry3",  # An asymmetric feature that accnts for non-cylindrically symmetric pt distributions
        "AR",  # Aspect ratio of long and short side of trajectory's minimum bounding rectangle
        "elongation",  # Est. of amount of extension of trajectory from centroid
        "boundedness",  # How much a particle with Deff is restricted by a circular confinement of radius r
        "fractal_dim",  # Measure of how complicated a self similar figure is
        "trappedness",  # Probability that a particle with Deff is trapped in a region
        "efficiency",  # Ratio of squared net displacement to the sum of squared step lengths
        "straightness",  # Ratio of net displacement to the sum of squared step lengths
        "MSD_ratio",  # MSD ratio of the track
        "Deff1",  # Effective diffusion coefficient at 0.33 s
        "Deff2",  # Effective diffusion coefficient at 3.3 s
        "Mean alpha",
        "Mean D_fit",
        "Mean kurtosis",
        "Mean asymmetry1",
        "Mean asymmetry2",
        "Mean asymmetry3",
        "Mean AR",
        "Mean elongation",
        "Mean boundedness",
        "Mean fractal_dim",
        "Mean trappedness",
        "Mean efficiency",
        "Mean straightness",
        "Mean MSD_ratio",
        "Mean Deff1",
        "Mean Deff2",
    ]

    if target_column is not None:
        assert target_column in df.columns, "Target column not in DataFrame"
        assert df[target_column].notna().all(), "Target column contains NaN values"

    if (
        features_to_keep == "default" and target_column is None
    ):  # user wants all default features
        df = df[default_feature_list]
        df = df[
            ~df[list(set(default_feature_list) - set(["Deff2", "Mean Deff2"]))]
            .isin([np.inf, np.nan, -np.inf])
            .any(axis=1)
        ]
    elif (
        features_to_keep == "default" and target_column is not None
    ):  # user wants all default features and target column
        df = df[default_feature_list + [target_column]]
        df = df[
            ~df[list(set(default_feature_list) - set(["Deff2", "Mean Deff2"]))]
            .isin([np.inf, np.nan, -np.inf])
            .any(axis=1)
        ]
    elif (
        features_to_keep != "default" and target_column is None
    ):  # user wants specific features
        df = df[features_to_keep]
        df = df[
            ~df[list(set(features_to_keep) - set(["Deff2", "Mean Deff2"]))]
            .isin([np.inf, np.nan, -np.inf])
            .any(axis=1)
        ]
    else:
        df = df[
            features_to_keep + [target_column]
        ]  # user wants specific features and target column
        df = df[
            ~df[list(set(features_to_keep) - set(["Deff2", "Mean Deff2"]))]
            .isin([np.inf, np.nan, -np.inf])
            .any(axis=1)
        ]

    df = df.fillna(0)  # setting any Deff2, Mean Deff2, to 0
    # This may also fill NA target columns with 0, which may not be desired

    return df


def combine_csvs(file_list, class_list, features_to_keep="default", target_column=None):
    """
    Combines multiple CSV files into a single DataFrame.

    Parameters
    -----------
    file_list : list
        A list of file paths to the CSV files to combine.
    features_to_keep : list
        A list of column names to keep in the combined DataFrame.
    target_column : str
        The name of the target column to keep in the combined DataFrame.


    Returns
    --------
    df: pandas.DataFrame
        The combined DataFrame.
    """

    df_list = []
    for file in file_list:
        df = pd.read_csv(file)
        for unique_class in class_list:
            if unique_class in file:
                df[target_column] = unique_class
                df_list.append(df)
    full_df = pd.concat(df_list)
    full_df = clean_mpt_data(
        full_df, features_to_keep=features_to_keep, target_column=target_column
    )

    return full_df


def concatenate_csv_files(uploaded_files):
    dfs = []
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        dfs.append(df)

    concatenated_df = pd.concat(dfs, ignore_index=True)
    return concatenated_df
