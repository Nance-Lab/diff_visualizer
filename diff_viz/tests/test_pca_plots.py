import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from diff_viz.pca_plots import pca_plot, plot_pca_bi_plot
import pandas as pd
import matplotlib.pyplot as plt

# Set up the testing data
testing_data_path = '../diff_viz/diff_viz/tests/testing_data/'
striatum_file = 'features_60X_Striatum_Slice2_Video1.csv'
cortex_file = 'features_100X_OGD_Cortex_Slice2_Video1.csv'
df_striat = pd.read_csv(testing_data_path+striatum_file)
df_cort = pd.read_csv(testing_data_path+cortex_file)
testing_df = pd.read_csv(testing_data_path+'demo_data.csv')

def test_pca_plot():
    fig, ex_var = pca_plot(testing_df, n_components=2, labels='age', scale=True, plot=True, save=False, save_path=None)
    assert isinstance(fig, plt.Figure)  # Check if a Figure object is returned
    assert len(ex_var) == 2
    assert ex_var[0] > ex_var[1]

def test_plot_pca_bi_plot():
    fig = plot_pca_bi_plot(testing_df, n_components=2, features=testing_df.columns[0:10], target_col='age', title='PCA Biplot')
    assert isinstance(fig, plt.Figure)  # Check if a Figure object is returned
    assert len(fig.axes) == 2
    assert len(fig.axes[0].collections) == 2
    assert len(fig.axes[1].collections) == 2
    assert fig.axes[0].get_xlabel() == 'PC1'
    assert fig.axes[0].get_ylabel() == 'PC2'
    assert fig.axes[1].get_xlabel() == 'PC1'
    assert fig.axes[1].get_ylabel() == 'PC2'
    assert fig.axes[0].get_title() == 'PCA Plot'
