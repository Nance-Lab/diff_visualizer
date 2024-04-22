from hypothesis.extra.pandas import columns, column, data_frames, range_indexes
import pandas as pd
import numpy as np
from hypothesis import strategies as st, given, settings


def hypothesis_features_dataframe(include_target_col=False):
    float_without_nan_st = st.floats(min_value=0.0001, max_value=3030, allow_nan=False)
    float_with_nan_st = st.floats(allow_nan=True, allow_infinity=False)
    int_st = st.integers(min_value=0, max_value=1000)

    np.random.seed(1234)
    param = {}
    df_columns = {
        "alpha": {"elements": float_with_nan_st, "unique": True},
        "D_fit": {"elements": float_with_nan_st, "unique": True},
        "kurtosis": {"elements": float_with_nan_st, "unique": True},
        "asymmetry1": {"elements": float_with_nan_st, "unique": True},
        "asymmetry2": {"elements": float_with_nan_st, "unique": True},
        "asymmetry3": {"elements": float_with_nan_st, "unique": True},
        "AR": {"elements": float_with_nan_st, "unique": True},
        "elongation": {"elements": float_with_nan_st, "unique": True},
        "boundedness": {"elements": float_with_nan_st, "unique": True},
        "fractal_dim": {"elements": float_with_nan_st, "unique": True},
        "trappedness": {"elements": float_with_nan_st, "unique": True},
        "efficiency": {"elements": float_with_nan_st, "unique": True},
        "straightness": {"elements": float_with_nan_st, "unique": True},
        "MSD_ratio": {"elements": float_with_nan_st, "unique": True},
        "frames": {"elements": int_st, "unique": True},
        "Deff1": {"elements": float_with_nan_st, "unique": True},
        "Deff2": {"elements": float_with_nan_st, "unique": True},
        # 'angle_mean',
        # 'angle_mag_mean',
        # 'angle_var',
        # 'dist_tot',
        # 'dist_net',
        # 'progression',
        "Mean alpha": {"elements": float_with_nan_st, "unique": True},
        "Mean D_fit": {"elements": float_with_nan_st, "unique": True},
        "Mean kurtosis": {"elements": float_with_nan_st, "unique": True},
        "Mean asymmetry1": {"elements": float_with_nan_st, "unique": True},
        "Mean asymmetry2": {"elements": float_with_nan_st, "unique": True},
        "Mean asymmetry3": {"elements": float_with_nan_st, "unique": True},
        "Mean AR": {"elements": float_with_nan_st, "unique": True},
        "Mean elongation": {"elements": float_with_nan_st, "unique": True},
        "Mean boundedness": {"elements": float_with_nan_st, "unique": True},
        "Mean fractal_dim": {"elements": float_with_nan_st, "unique": True},
        "Mean trappedness": {"elements": float_with_nan_st, "unique": True},
        "Mean efficiency": {"elements": float_with_nan_st, "unique": True},
        "Mean straightness": {"elements": float_with_nan_st, "unique": True},
        "Mean MSD_ratio": {"elements": float_with_nan_st, "unique": True},
        "Mean Deff1": {"elements": float_with_nan_st, "unique": True},
        "Mean Deff2": {"elements": float_with_nan_st, "unique": True},
    }

    test_dfs = data_frames(
        index=range_indexes(min_size=10),
        columns=[column(key, **value) for key, value in df_columns.items()],
    )

    return test_dfs


# def features_dataframe(features=categories, include_target_col=True):

#     data_cols = columns(names_or_number=features, dtype=float, elements=st.floats())
#     position_cols = columns(names_or_number=['X', 'Y'], dtype=float, elements=st.floats(min_value=0.0, max_value=2048.0))

#     df_columns = [data_cols, position_cols]
#     if include_target_col:
#         target_col = column(name='target', dtype=int, elements=st.integers(min_value=0, max_value=20)) #up to twenty unique targets
#         df_columns.append(target_col)

#     df = data_frames(columns=df_columns, index=range_indexes(min_size=10))
#     return df

dfs = hypothesis_features_dataframe(include_target_col=False)
print("done")
