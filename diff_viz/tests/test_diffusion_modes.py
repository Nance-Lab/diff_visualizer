import pytest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from diff_viz.diffusion_modes import plot_diffusion_modes

class TestPlotDiffusionModes:
    @classmethod
    def setup_class(cls):
        # Create a sample DataFrame for testing
        cls.ecm = pd.DataFrame({
            'age': [10, 10, 20, 20, 30, 30],
            'alpha': [1.2, 0.8, 1.1, 0.9, 1.0, 1.3],
        })
        cls.target = 'age'
    
    def test_plot_diffusion_modes(self):
        # Test that the function returns a Matplotlib Axes object
        ax = plot_diffusion_modes(self.ecm, self.target)
        assert isinstance(ax, plt.Axes)
        
        # Test that the y-axis limits are set to [0, 1]
        ylim = ax.get_ylim()
        assert ylim == (0, 1)
        
        # Test that the bar heights are correct
        subdiffusive = ax.containers[0].get_heights()
        brownian = ax.containers[1].get_heights()
        superdiffusive = ax.containers[2].get_heights()
        np.testing.assert_allclose(subdiffusive, [0.5, 0, 0])
        np.testing.assert_allclose(brownian, [0, 0.5, 1])
        np.testing.assert_allclose(superdiffusive, [0.5, 0.5, 0])
