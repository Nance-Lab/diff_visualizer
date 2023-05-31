import os
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

from os import listdir, getcwd, chdir
from os.path import isfile, join
from sklearn import linear_model



def get_msd_dose_dict(doses):
    msd_dose_dict = {}
    #sem_dose_dict = {}

    for dose in doses:
        msd_dose_dict[dose] = []
        #sem_dose_dict[dose] = []
    
    return msd_dose_dict

def get_df_dose_list(doses,geomean_df):
    df_dose_list = []
    #sem_dose_list = []
    
    for dose in doses:
        msd_dose_df = pd.DataFrame()
        dose_cols = [col for col in geomean_df.columns if dose in col]
        msd_dose_df = geomean_df.filter(dose_cols, axis=1)
        df_dose_list.append(msd_dose_df)
        #sem_dose_df = pd.DataFrame()
        #sem_cols = [col for col in geosem_df.columns if dose in col]
        #sem_dose_df = geosem_df.filter(sem_cols, axis=1)
        #sem_dose_list.append(sem_dose_df)
        
    return df_dose_list

def msd_viz(doses,geomean_df,df_dose_list):
    count = 0
    labels = 'Roteneone'
    if len(doses) == 1:
        tau = geomean_df.index.values / 651
        fig, ax = plt.subplots(figsize=(6,6))
        #plt.suptitle(f'MSD Analysis for {model} experiment {experiment}',fontsize=20)
        plt.rcParams.update({'font.family':'helvetica'})
        handles = list(geomean_df.columns)
        #labels = [handle.split(stimulus+'_')[1] for handle in handles]
    
        for handle in handles:    
            ax.loglog(tau[0:70],geomean_df[handle][0:70])
            ax.set_xlabel('Lag time (s)',fontsize=16)
            ax.set_ylabel('Mean-squared displacement (μ$m^2$)',fontsize=16)
            ax.legend(labels,loc='upper left')
            ax.set_xlim([0.002, 0.05])
            ax.set_ylim([0.0009,1.3])
         
    else:                
        tau = geomean_df.index.values[0:100] / 651
        fig, axes = plt.subplots(nrows=1, ncols=len(doses),figsize=(10,4))
        #plt.suptitle(f'MSD Analysis for {model} experiment {experiment}\n\n',fontsize=20)
        plt.rcParams.update({'font.family':'helvetica'})
        count=0
        
        for c in np.arange(0,len(doses)):
            handles = list(df_dose_list[c].columns)
            #err = sem_dose_list[count][handles[c]][0:70]/2
            times = []
            handles = list(df_dose_list[c].columns)
            #labels = [handle.split(stimulus+'_')[1] for handle in handles]
            print(handles,labels)
            #err = sem_dose_list[count][handles[c]][0:70]/2
            axes[c].loglog(tau[0:70],df_dose_list[count][0:70])
            axes[c].set_xlabel('\nLag time (s)',fontsize=16)
            axes[c].legend(labels,loc='best')
            axes[c].set_xlim([0.002, 0.1])
            axes[c].set_ylim([0.0009,10])
            axes[c].set_title(f'\n{doses[c]}', fontsize=14)
    
            if c == 0:
                axes[c].set_ylabel('Mean-squared displacement (μ$m^2$)',fontsize=16)
    
            count+=1
    return