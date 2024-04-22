"""
Visualize mean-squared displacement (MSD) data from diffusivity experiments.
 """
import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import numpy.ma as ma
import matplotlib.pyplot as plt
from diff_viz import diff_utils

from os import listdir, getcwd, chdir
from os.path import isfile, join

# from diff_utils import get_experiment, get_path, get_csvs, get_geo_dict, get_geo_df, get_df_dose_list, calc_error


def plot_individual_msds(
    df,
    x_range=10,
    y_range=100,
    umppx=0.16,
    fps=100.02,
    alpha=0.1,
    figsize=(10, 10),
    subset=False,
    size=1000,
    dpi=300,
    title=None,
):
    """
    Plot MSDs of trajectories and the geometric average.

    Parameters
    ----------
    prefix: string
        Prefix of file name to be plotted e.g. features_P1.csv prefix is P1.
    x_range: float64 or int
        Desire x range of graph.
    y_range: float64 or int
        Desire y range of graph.
    fps: float64
        Frames per second of video.
    umppx: float64
        Resolution of video in microns per pixel.
    alpha: float64
        Transparency factor.  Between 0 and 1.
    upload: boolean
        True if you want to upload to s3.

    Returns
    -------
    geo_mean: numpy array
        Geometric mean of trajectory MSDs at all time points.
    geo_SEM: numpy array
        Geometric standard errot of trajectory MSDs at all time points.

    """

    merged = df

    fig = plt.figure(figsize=figsize)
    particles = int(max(merged["Track_ID"]))

    if particles < size:
        size = particles - 1
    else:
        pass

    frames = int(max(merged["Frame"]))

    y = merged["Y"]  # .values.reshape((particles+1, frames+1))*umppx*umppx
    x = merged["X"]  # .values.reshape((particles+1, frames+1))/fps
    #     for i in range(0, particles+1):
    #         y[i, :] = merged.loc[merged.Track_ID == i, 'MSDs']*umppx*umppx
    #         x = merged.loc[merged.Track_ID == i, 'Frame']/fps

    particles = np.linspace(0, particles, particles - 1).astype(int)
    if subset:
        particles = np.random.choice(particles, size=size, replace=False)

    y = np.zeros((particles.shape[0], frames + 1))
    for idx, val in enumerate(particles):
        y[idx, :] = merged.loc[merged.Track_ID == val, "MSDs"] * umppx * umppx
        x = merged.loc[merged.Track_ID == val, "Frame"] / fps
        plt.plot(x, y[idx, :], "k", alpha=alpha)

    geo_mean = np.nanmean(ma.log(y), axis=0)
    geo_SEM = stats.sem(ma.log(y), axis=0, nan_policy="omit")
    plt.plot(x, np.exp(geo_mean), "k", linewidth=4)
    plt.plot(x, np.exp(geo_mean - geo_SEM), "k--", linewidth=2)
    plt.plot(x, np.exp(geo_mean + geo_SEM), "k--", linewidth=2)
    plt.xlim(0, x_range)
    plt.ylim(0, y_range)
    plt.xlabel("Tau (s)", fontsize=25)
    plt.ylabel(r"Mean Squared Displacement ($\mu$m$^2$)", fontsize=25)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.tight_layout()
    plt.title(title, fontsize=25)
    plt.show()
    return fig


def msd_viz(doses, geomean_df, geosem_df, fps):
    """
    Visualize MSD data from diffusivity experiments.

    Parameters
    ----------
        doses (list):
            List of doses used in the experiment.
        geomean_df (pandas.DataFrame):
            DataFrame containing the mean-squared displacement data.
        geosem_df (pandas.DataFrame):
            DataFrame containing the standard error of the mean-squared displacement data.
        fps (int):
            Frames per second of the experiment.

    Returns
    -------
        fig (matplotlib.figure.Figure):
            Figure containing the MSD data.

    """
    count = 0
    msd_dose_list = diff_utils.get_df_dose_list(doses, geomean_df)
    sem_dose_list = diff_utils.get_df_dose_list(doses, geosem_df)

    if len(doses) == 1:
        tau = geomean_df.index.values / 651
        fig, ax = plt.subplots(figsize=(6, 6))
        plt.rcParams.update({"font.family": "helvetica"})
        handles = list(geomean_df.columns)

        for handle in handles:
            ax.loglog(tau, geomean_df[handle])
            ax.set_xlabel("Lag time (s)", fontsize=16)
            ax.set_ylabel("Mean-squared displacement (μ$m^2$)", fontsize=16)
            ax.fill_between(
                tau,
                geomean_df[handle] + geosem_df[handle] / 2,
                geomean_df[handle] - geosem_df[handle] / 2,
                cmap="ocean",
                alpha=0.2,
            )
            ax.legend(handles, loc="best")
            ax.set_xlim([0.008, 0.2])
            ax.set_ylim([0.008, 1])
            # ax.set_title(f'\n{doses[c]}\n', fontsize=16)

    else:
        tau = geomean_df.index.values / 651
        fig, axes = plt.subplots(nrows=1, ncols=len(doses), figsize=(len(doses) * 6, 6))
        plt.rcParams.update({"font.family": "helvetica"})
        count = 0

        for c in np.arange(0, len(doses)):
            while count <= c:
                sem_handles = list(sem_dose_list[c].columns)
                msd_handles = list(msd_dose_list[c].columns)
                axes[c].loglog(tau, msd_dose_list[count])
                axes[c].fill_between(
                    tau,
                    msd_dose_list[count] + sem_dose_list[count] / 2,
                    msd_dose_list[count] - sem_dose_list[count] / 2,
                    cmap="ocean",
                    alpha=0.2,
                )
                axes[c].set_xlabel("\nLag time (s)", fontsize=16)
                # axes[c].legend(handles,loc='best')
                axes[c].set_xlim([0.008, 1])
                axes[c].set_ylim([0.008, 1])
                axes[c].set_title(f"\n{doses[c]}\n", fontsize=16)

                if c == 0:
                    axes[c].set_ylabel(
                        "Mean-squared displacement (μ$m^2$)", fontsize=16
                    )

                count += 1
    return fig


def get_geo_data(merged, umppx=0.16, fps=100.02, size=1000):
    "takes in a df and returns the geo mean and     geo SEM"

    particles = int(max(merged["Track_ID"]))

    if particles < size:
        size = particles - 1
    else:
        pass

    frames = int(max(merged["Frame"]))

    y = merged["Y"].values.reshape((particles + 1, frames + 1)) * umppx * umppx
    x = merged["X"].values.reshape((particles + 1, frames + 1)) / fps
    #     for i in range(0, particles+1):
    #         y[i, :] = merged.loc[merged.Track_ID == i, 'MSDs']*umppx*umppx
    #         x = merged.loc[merged.Track_ID == i, 'Frame']/fps

    particles = np.linspace(0, particles, particles - 1).astype(int)

    y = np.zeros((particles.shape[0], frames + 1))
    for idx, val in enumerate(particles):
        y[idx, :] = merged.loc[merged.Track_ID == val, "MSDs"] * umppx * umppx
        x = merged.loc[merged.Track_ID == val, "Frame"] / fps

    geo_mean = np.nanmean(ma.log(y), axis=0)
    geo_SEM = stats.sem(ma.log(y), axis=0, nan_policy="omit")

    return geo_mean, geo_SEM
