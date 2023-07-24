"""
Visualize mean-squared displacement (MSD) data from diffusivity experiments.
 """

import os
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

from os import listdir, getcwd, chdir
from os.path import isfile, join

from utils import get_experiment, get_path, get_csvs, get_geo_dict, get_geo_df, get_df_dose_list, calc_error

def msd_viz(doses,geomean_df,geosem_df,fps):
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
    count=0
    msd_dose_list=get_df_dose_list(doses,geomean_df)
    sem_dose_list=get_df_dose_list(doses,geosem_df)
    
    if len(doses)==1:
        tau=geomean_df.index.values/651
        fig,ax=plt.subplots(figsize=(6,6))
        plt.rcParams.update({'font.family':'helvetica'})
        handles=list(geomean_df.columns)
    
        for handle in handles:    
            ax.loglog(tau,geomean_df[handle])
            ax.set_xlabel('Lag time (s)',fontsize=16)
            ax.set_ylabel('Mean-squared displacement (μ$m^2$)',fontsize=16)
            ax.fill_between(tau,geomean_df[handle]+geosem_df[handle]/2,geomean_df[handle]-geosem_df[handle]/2,cmap='ocean',alpha=0.2)
            ax.legend(handles,loc='best')
            ax.set_xlim([0.008, 0.2])
            ax.set_ylim([0.008,1])
            #ax.set_title(f'\n{doses[c]}\n', fontsize=16)
         
    else:                
        tau=geomean_df.index.values/651
        fig,axes=plt.subplots(nrows=1,ncols=len(doses),figsize=(len(doses)*6,6))
        plt.rcParams.update({'font.family':'helvetica'})
        count=0
        
        for c in np.arange(0,len(doses)):
            while count<=c:
                sem_handles = list(sem_dose_list[c].columns)
                msd_handles = list(msd_dose_list[c].columns)
                axes[c].loglog(tau,msd_dose_list[count])
                axes[c].fill_between(tau,msd_dose_list[count]+sem_dose_list[count]/2,msd_dose_list[count]-sem_dose_list[count]/2,cmap='ocean',alpha=0.2)
                axes[c].set_xlabel('\nLag time (s)',fontsize=16)
                #axes[c].legend(handles,loc='best')
                axes[c].set_xlim([0.008, 1])
                axes[c].set_ylim([0.008,1])
                axes[c].set_title(f'\n{doses[c]}\n', fontsize=16)
    
                if c == 0:
                    axes[c].set_ylabel('Mean-squared displacement (μ$m^2$)',fontsize=16)
    
                count+=1
    return fig