import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from diff_viz.diffusion_modes import plot_diffusion_modes_single_label, plot_diffusion_modes

import pandas as pd
import matplotlib.pyplot as plt

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

    # Optionally, you can add more specific assertions depending on your requirements
    # For example, checking the labels, colors, and other properties of the plot

    # Optionally, you can save the plot for manual inspection
    # fig.savefig('diffusion_modes_plot.png')

        
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
