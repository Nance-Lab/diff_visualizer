""" 
Module for utility functions for diff_viz and MPT data
"""


import os
from os import listdir, getcwd, chdir
from os.path import isfile, join
import pandas as pd


def get_experiment(date,donor,DIV,stimulus,level):
    '''Generates a string for the Traj csv folder you're working in.
    This follows the naming convention I use, but you can omit this function and
    code in the name of the Traj csv folder (second to last cell).
    '''
    experiment=date+'_'+donor+'_'+DIV+'_'+stimulus+'_'+level #Title of the Traj_csv folder without '_Traj_csv'
    
    return experiment

def get_path(model,experiment):
    '''Returns the datapath in your directory corresponding to the Traj csv folder.
    '''
    data_path=f'/Users/brendanbutler/Desktop/Nance Lab/Data/diff_classifier/notebooks/development/MPT_Data/{model} MPT/{experiment}_Traj_csv/'
    return data_path

def get_csvs(data_path,filetype):
    '''Returns the master list of csv files in the Traj csv folder, geoMean or geoSEM files depending on user input.
    '''
    geo_list=[j for j in listdir(data_path) if isfile(join(data_path, j)) and filetype in j]
    
    return geo_list

def get_geo_dict(geo_list,doses):
    '''Converts the list of csv files into a dictionary split by dose (50nM ROT, 0.5h OGD, etc.)
    '''
    geo_dict={}
    
    for dose in doses:
        geo_dict[dose]=[]
        
    for dose in doses:
        geo_dose=[file for file in geo_list if dose in file]
        geo_dict[dose].append(geo_dose)
    
    return geo_dict

def get_df_dose_list(doses,geo_df):
    '''Generates list of column headers for plotting purposes.
    '''
    df_dose_list = []
    
    for dose in doses:
        dose_df = pd.DataFrame()
        dose_cols = [col for col in geo_df.columns if dose in col]
        dose_df = geo_df.filter(dose_cols, axis=1)
        df_dose_list.append(dose_df)
        
    return df_dose_list
