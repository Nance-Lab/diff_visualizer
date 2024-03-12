import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from diff_viz.feature_distribution_plots import feature_violin_plot
import pandas as pd
import matplotlib.pyplot as plt

# Set up the testing data
testing_data_path = '../diff_viz/diff_viz/tests/testing_data/feature_data/'
striatum_file = 'features_60X_Striatum_Slice2_Video1.csv'
cortex_file = 'features_100X_OGD_Cortex_Slice2_Video1.csv'
df_striat = pd.read_csv(testing_data_path+striatum_file)
df_cort = pd.read_csv(testing_data_path+cortex_file)
testing_df = pd.read_csv(testing_data_path+'demo_data.csv')

def test_feature_violin_plot():

    #figure with no labels, no title
    fig = feature_violin_plot(testing_df, feature_to_plot='Deff1', label_column=None, figsize=(2,2))
    assert isinstance(fig, plt.Figure)  # Check if a Figure object is returned
    #assert fig.axes[0].get_title() == 'Deff1'
    assert fig.axes[0].get_xlabel() == 'Deff1'
    assert fig.axes[0].get_title() == ''

    #figure with labels, no title
    fig = feature_violin_plot(testing_df, feature_to_plot='Deff1', label_column='age', figsize=(2,2))
    assert isinstance(fig, plt.Figure)  # Check if a Figure object is returned
    assert fig.axes[0].get_title() == ''
    assert fig.axes[0].get_xlabel() == 'age'
    assert fig.axes[0].get_ylabel() == 'Deff1'

    #figure with labels, with title
    fig = feature_violin_plot(testing_df, feature_to_plot='Deff1', label_column='age', figsize=(2,2), title='test')
    assert isinstance(fig, plt.Figure)  # Check if a Figure object is returned
    assert fig.axes[0].get_title() == 'test'
    assert fig.axes[0].get_xlabel() == 'age'
    assert fig.axes[0].get_ylabel() == 'Deff1'
    
    