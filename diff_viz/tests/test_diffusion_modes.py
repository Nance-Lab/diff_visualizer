import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from diff_viz.diffusion_modes import plot_diffusion_modes_single_label, plot_diffusion_modes
import pandas as pd
import matplotlib.pyplot as plt

# Set up the testing data
testing_data_path = '../diff_viz/diff_viz/tests/testing_data/'
striatum_file = 'features_60X_Striatum_Slice2_Video1.csv'
cortex_file = 'features_100X_OGD_Cortex_Slice2_Video1.csv'
df_striat = pd.read_csv(testing_data_path+striatum_file)
df_cort = pd.read_csv(testing_data_path+cortex_file)
testing_df = pd.read_csv(testing_data_path+'demo_data.csv')

def test_plot_diffusion_modes_single_label():
    # Create a sample DataFrame for testing
    data = {
        'alpha': [1.2, 0.8, 1.0, 1.5, 0.9, 1.1],
        # Add more columns if necessary for your specific use case
    }
    ecm = pd.DataFrame(data)

    # Call the function being tested
    fig = plot_diffusion_modes_single_label(ecm, 'Age')

    # Assertions to verify the correctness of the plot
    assert isinstance(fig, plt.Figure)  # Check if a Figure object is returned

    # Assert that the plot contains the expected number of bars
    ax = fig.gca()
    assert len(ax.patches) == 3

    # Assert that the plot has the correct title
    assert ax.get_title() == 'Percentage of Diffusion Modes per Age'

        
    # Test that the bar heights are correct
    # Assert that each bar has the correct height based on the data
    bars = ax.patches
    expected_heights = [
        ecm[ecm['alpha'] < 0.9].shape[0] / ecm.shape[0],  # Subdiffusive
        ecm[(ecm['alpha'] <= 1.1) & (ecm['alpha'] >= 0.9)].shape[0] / ecm.shape[0],  # Brownian
        ecm[ecm['alpha'] > 1.1].shape[0] / ecm.shape[0]  # Superdiffusive
    ]
    for bar, expected_height in zip(bars, expected_heights):
        assert np.isclose(bar.get_height(), expected_height)


def test_plot_diffusion_modes():

    fig = plot_diffusion_modes(testing_df, 'age')
    ax = fig.gca()

    assert isinstance(fig, plt.Figure)  # Check if a Figure object is returned
    assert ax.get_title() == 'Percentage of Diffusion Modes per age'

    num_bars = len(fig.axes[0].patches)
    assert num_bars == len(testing_df['age'].unique())*3
    heights = [element.get_height() for element in fig.axes[0].patches]
    assert np.isclose(sum(heights), len(testing_df['age'].unique()), 0.05)
