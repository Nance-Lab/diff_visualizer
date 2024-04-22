"""
Description: Class for storing MPT data
"""
from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass
class MPTData:
    """
    Class for storing MPT data
    """

    feature_data: pd.DataFrame
    msd_data: pd.DataFrame

    def features_df(self):
        return self.feature_data

    def msd_df(self):
        return self.msd_data
