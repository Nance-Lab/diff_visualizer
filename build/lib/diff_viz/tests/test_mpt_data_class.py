import pandas as pd
import numpy as np
import diff_viz.mpt_data_class as mptdata


mpt_data_object =  mptdata.MPTData(
    feature_data=pd.read_csv('testing_data/demo_data.csv'),
    msd_data=None,
    )
    
feature_df = mpt_data_object.feature_data()