import os
import numpy as np
import numpy.testing as npt
from scipy.spatial import Voronoi
import matplotlib as mpl
import diff_classifier.msd as msd
import diff_classifier.features as ft
import diff_classifier.heatmaps as hm
mpl.use('Agg')


def test_voronoi_finite_polygons_2d():
    prefix = 'test'
    msd_file = 'msd_{}.csv'.format(prefix)
    ft_file = 'features_{}.csv'.format(prefix)

    dataf = msd.random_traj_dataset(nparts=30, ndist=(1, 1), seed=3)
    msds = msd.all_msds2(dataf, frames=100)
    msds.to_csv(msd_file)
    feat = ft.calculate_features(msds)
    feat.to_csv(ft_file)

    xs = feat['X'].astype(int)
    ys = feat['Y'].astype(int)
    points = np.zeros((xs.shape[0], 2))
    points[:, 0] = xs
    points[:, 1] = ys

    vor = Voronoi(points)
    regions, vertices = hm.voronoi_finite_polygons_2d(vor)

    npt.assert_equal(243.8, np.round(np.mean(vertices), 1))


def test_plot_heatmap():
    prefix = 'test'
    msd_file = 'msd_{}.csv'.format(prefix)
    ft_file = 'features_{}.csv'.format(prefix)

    dataf = msd.random_traj_dataset(nparts=30, ndist=(1, 1), seed=3)
    msds = msd.all_msds2(dataf, frames=100)
    msds.to_csv(msd_file)
    feat = ft.calculate_features(msds)
    feat.to_csv(ft_file)

    hm.plot_heatmap(prefix, resolution=520, rows=1, cols=1, figsize=(6,5), upload=False)
    assert os.path.isfile('hm_asymmetry1_{}.png'.format(prefix))