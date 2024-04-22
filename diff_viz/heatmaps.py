import matplotlib as mpl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
import scipy.stats as stats
import os
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy.ma as ma
import matplotlib.cm as cm


def voronoi_finite_polygons_2d(vor, radius=None):
    """
    Reconstruct infinite voronoi regions in a 2D diagram to finite
    regions.

    Parameters
    ----------
    vor : Voronoi
        Input diagram
    radius : float, optional
        Distance to 'points at infinity'.

    Returns
    -------
    regions : list of tuples
        Indices of vertices in each revised Voronoi regions.
    vertices : list of tuples
        Coordinates for revised Voronoi vertices. Same as coordinates
        of input vertices, with 'points at infinity' appended to the
        end.

    """

    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    counter = 0
    for p1, region in enumerate(vor.point_region):
        try:
            vertices = vor.regions[region]

            if all(v >= 0 for v in vertices):
                # finite region
                new_regions.append(vertices)
                continue

            # reconstruct a non-finite region
            ridges = all_ridges[p1]
            new_region = [v for v in vertices if v >= 0]

            for p2, v1, v2 in ridges:
                if v2 < 0:
                    v1, v2 = v2, v1
                if v1 >= 0:
                    # finite ridge: already in the region
                    continue

                # Compute the missing endpoint of an infinite ridge

                t = vor.points[p2] - vor.points[p1]  # tangent
                t /= np.linalg.norm(t)
                n = np.array([-t[1], t[0]])  # normal

                midpoint = vor.points[[p1, p2]].mean(axis=0)
                direction = np.sign(np.dot(midpoint - center, n)) * n
                far_point = vor.vertices[v2] + direction * radius

                new_region.append(len(new_vertices))
                new_vertices.append(far_point.tolist())

            # sort region counterclockwise
            vs = np.asarray([new_vertices[v] for v in new_region])
            c = vs.mean(axis=0)
            angles = np.arctan2(vs[:, 1] - c[1], vs[:, 0] - c[0])
            new_region = np.array(new_region)[np.argsort(angles)]

            # finish
            new_regions.append(new_region.tolist())
        except KeyError:
            counter = counter + 1
            # print('Oops {}'.format(counter))

    return new_regions, np.asarray(new_vertices)


def plot_heatmap(
    prefix,
    feat_df,
    feature="Deff1",
    vmin=0,
    vmax=1,
    resolution=512,
    rows=4,
    cols=4,
    dpi=None,
    figsize=(12, 10),
):
    """
    Plot heatmap of trajectories in video with colors corresponding to features.

    Parameters
    ----------

    prefix: string
        Prefix of file name to be plotted e.g. features_P1.csv prefix is P1.
    feature: string
        Feature to be plotted.  See features_analysis.py
    vmin: float64
        Lower intensity bound for heatmap.
    vmax: float64
        Upper intensity bound for heatmap.
    resolution: int
        Resolution of base image.  Only needed to calculate bounds of image.
    rows: int
        Rows of base images used to build tiled image.
    cols: int
        Columns of base images used to build tiled images.

    dpi: int
        Desired dpi of output image.
    figsize: list
        Desired dimensions of output image.

    Returns
    -------

    """
    # Inputs
    # ----------

    string = feature
    t_min = vmin
    t_max = vmax
    ires = resolution

    # Building points and color schemes
    # ----------
    zs = ma.masked_invalid(feat_df[string])
    zs = ma.masked_where(zs <= t_min, zs)
    zs = ma.masked_where(zs >= t_max, zs)
    to_mask = ma.getmask(zs)
    zs = ma.compressed(zs)

    xs = ma.compressed(ma.masked_where(to_mask, feat_df["X"].astype(int)))
    ys = ma.compressed(ma.masked_where(to_mask, feat_df["Y"].astype(int)))
    points = np.zeros((xs.shape[0], 2))
    points[:, 0] = xs
    points[:, 1] = ys
    vor = Voronoi(points)

    # Plot
    # ----------
    fig = plt.figure(figsize=figsize, dpi=dpi)
    regions, vertices = voronoi_finite_polygons_2d(vor)
    my_map = mpl.colormaps["viridis"]
    norm = mpl.colors.Normalize(t_min, t_max, clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=mpl.colormaps["viridis"])

    test = 0
    p2 = 0
    counter = 0
    for i in range(0, points.shape[0] - 1):
        try:
            polygon = vertices[regions[p2]]
            point1 = Point(points[test, :])
            poly1 = Polygon(polygon)
            check = poly1.contains(point1)
            if check:
                plt.fill(*zip(*polygon), color=my_map(norm(zs[test])), alpha=0.7)
                p2 = p2 + 1
                test = test + 1
            else:
                test = test + 1
        except IndexError:
            print("Index mismatch possible.")

    mapper.set_array(10)
    # plt.colorbar(mapper)
    plt.xlim(0, ires * cols)
    plt.ylim(0, ires * rows)
    plt.axis("off")

    print("Plotted {} heatmap successfully.")
    outfile = "{}_hm_{}.png".format(prefix, feature)
    fig.savefig(outfile, bbox_inches="tight")


def plot_scatterplot(
    feat_df,
    feature="asymmetry1",
    vmin=0,
    vmax=1,
    resolution=512,
    rows=4,
    cols=4,
    dotsize=10,
    figsize=(12, 10),
):
    """
    Plot scatterplot of trajectories in video with colors corresponding to features.

    Parameters
    ----------

    feature: string
        Feature to be plotted.  See features_analysis.py
    vmin: float64
        Lower intensity bound for heatmap.
    vmax: float64
        Upper intensity bound for heatmap.
    resolution: int
        Resolution of base image.  Only needed to calculate bounds of image.
    rows: int
        Rows of base images used to build tiled image.
    cols: int
        Columns of base images used to build tiled images.


    """
    # Inputs
    # ----------
    string = feature
    leveler = feat_df[string]
    t_min = vmin
    t_max = vmax
    ires = resolution

    norm = mpl.colors.Normalize(t_min, t_max, clip=True)
    mapper = cm.ScalarMappable(norm=norm, cmap=mpl.colormaps["viridis"])

    zs = ma.masked_invalid(feat_df[string])
    zs = ma.masked_where(zs <= t_min, zs)
    zs = ma.masked_where(zs >= t_max, zs)
    to_mask = ma.getmask(zs)
    zs = ma.compressed(zs)
    xs = ma.compressed(ma.masked_where(to_mask, feat_df["X"].astype(int)))
    ys = ma.compressed(ma.masked_where(to_mask, feat_df["Y"].astype(int)))

    fig = plt.figure(figsize=figsize)
    plt.scatter(xs, ys, c=zs, s=dotsize)
    mapper.set_array(10)
    # plt.colorbar(mapper)
    plt.xlim(0, ires * cols)
    plt.ylim(0, ires * rows)
    plt.axis("off")

    # print('Plotted {} scatterplot successfully.'.format(prefix))
    # outfile = 'scatter_{}_{}.png'.format(feature, prefix)
    # fig.savefig(outfile, bbox_inches='tight')
    # if upload == True:
    #     aws.upload_s3(outfile, remote_folder+'/'+outfile, bucket_name=bucket)


def plot_trajectories(
    msd_df, resolution=512, rows=4, cols=4, figsize=(12, 12), subset=True, size=1000
):
    """
    Plot trajectories in video.

    Parameters
    ----------
    prefix: string
        Prefix of file name to be plotted e.g. features_P1.csv prefix is P1.
    resolution: int
        Resolution of base image.  Only needed to calculate bounds of image.
    rows: int
        Rows of base images used to build tiled image.
    cols: int
        Columns of base images used to build tiled images.
    upload: boolean
        True if you want to upload to s3.

    """
    merged = msd_df
    particles = int(max(merged["Track_ID"]))
    if particles < size:
        size = particles - 1
    else:
        pass
    particles = np.linspace(0, particles, particles - 1).astype(int)
    if subset:
        particles = np.random.choice(particles, size=size, replace=False)
    ires = resolution

    fig = plt.figure(figsize=figsize)
    for part in particles:
        x = merged[merged["Track_ID"] == part]["X"]
        y = merged[merged["Track_ID"] == part]["Y"]
        plt.plot(x, y, color="k", alpha=0.7)

    plt.xlim(0, ires * cols)
    plt.ylim(0, ires * rows)
    plt.axis("off")

    # print('Plotted {} trajectories successfully.'.format(prefix))
    # outfile = 'traj_{}.png'.format(prefix)
    # fig.savefig(outfile, bbox_inches='tight')
    # if upload:
    #     aws.upload_s3(outfile, remote_folder+'/'+outfile, bucket_name=bucket)
