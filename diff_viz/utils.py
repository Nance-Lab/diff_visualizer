import os
from os import listdir, getcwd, chdir
from os.path import isfile, join

def get_experiment(traj_folder):
    '''Generates a string for the Traj csv folder you're working in.
    This follows the naming convention I use, but you can omit this function and
    code in the name of the Traj csv folder (second to last cell).
    '''
    experiment=traj_folder #Title of the Traj_csv folder without '_Traj_csv'
    
    return experiment

def get_path(model_system,experiment):
    '''Generates the data path of the folder containing the trajectories relevant to the specified experiment
    and model system.'''

    base_path=os.getcwd()
    data_path=base_path+'/'+f'{model_system}'+'/'+experiment+'/'

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

def get_geo_df(data_path,filetype,doses,timepoints,experiment):
    '''Constructs a dataframe of MSD values for every combination of dose/time.
    If there are multiple csv files for a single dose/time, the arithmatic mean is computed.
    The user has the option to generate dataframes for the MSD values (geoMean) or the standard
    error of the mean (geoSEM) from MPT segmenting. 
    '''
    df_list=[]   
        
    if filetype=='geomean':
        geo_list=get_csvs(data_path,filetype)
        geo_dict=get_geo_dict(geo_list,doses)
    
        for dose in doses: 
            for time in timepoints:
                csv_list=[file for file in geo_dict[dose][0] if dose in file and time in file]
                temp_csv_df=[]
                 
                for csv in csv_list:
                    if sum(dose and time in csv for csv in csv_list)==1: 
                        temp_csv_df.append(pd.read_csv(data_path+csv))
                        csv_df=pd.concat(temp_csv_df,axis=1)
                        csv_df[dose+"_"+time]=np.exp(csv_df.mean(axis=1))
                        geo_df=csv_df.drop(columns=csv_df.columns[:1],axis=1)
                        df_list.append(geo_df)
                
                    if sum(dose and time in csv for csv in csv_list)>1:
                        ndrop=sum(dose and time in csv for csv in csv_list)
                        temp_csv_df.append(pd.read_csv(data_path+csv))
                        csv_df=pd.concat(temp_csv_df,axis=1)
                        csv_df[dose+"_"+time]=np.exp(csv_df.mean(axis=1))
                        geo_df=csv_df.drop(columns=csv_df.columns[:ndrop],axis=1)
                        df_list.append(geo_df)
    
            geo_df=pd.concat(df_list,axis=1)
        
    if filetype =='geoSEM':
        geo_list=get_csvs(data_path,filetype)
        geo_dict=get_geo_dict(geo_list,doses)
        
        for dose in doses: 
            for time in timepoints:
                csv_list=[file for file in geo_dict[dose][0] if dose in file and time in file]
                temp_csv_df=[]
                
                for csv in csv_list:
                    if sum(dose and time in csv for csv in csv_list)==1:
                        temp_csv_df.append(pd.read_csv(data_path+csv))
                        csv_df=pd.concat(temp_csv_df,axis=1)
                        csv_df[dose+"_"+time]=csv_df.mean(axis=1)
                        geo_df=csv_df.drop(columns=csv_df.columns[:1],axis=1)
                        df_list.append(geo_df)
                    
                    if sum(dose and time in csv for csv in csv_list)>1:
                        ndrop=sum(dose and time in csv for csv in csv_list)
                        temp_csv_df.append(pd.read_csv(data_path+csv))
                        csv_df=pd.concat(temp_csv_df,axis=1)
                        csv_df[dose+"_"+time]=csv_df.mean(axis=1)
                        geo_df_full=csv_df.drop(columns=csv_df.columns[:ndrop],axis=1)
                        df_list.append(geo_df_full)
    
            geo_df=pd.concat(df_list,axis=1)
        
    return geo_df

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

def calc_error(doses,timepoints,experiment,geomean_df):

    geosem_df=get_geo_df(data_path,'geoSEM',doses,timepoints,experiment)

    return geosem_df