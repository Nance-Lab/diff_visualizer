import streamlit as st
import streamlit_tags
import pandas as pd
from diff_viz import data_loading
from helper_functions.session_state import ss
from io import BytesIO


######################################### SESSION STATES ##################################################
st.session_state.update(st.session_state)
ss.initialise_state(state_dict = {'file_type': 'MSD Trajectory Data',
                                   'df_in': False,
                                   'demo': False,
                                   'view_df': False,
                                   'data_dict': None,
                                   'num_conditions': None,
                                   'conditions_list': None,
                                   })

# st.session_state.update(st.session_state)
# if 'DATA_LOADED' not in st.session_state:
#     st.session_state['DATA_LOADED'] = False

# if 'file_type' not in st.session_state:
#     st.session_state['file_type'] = 'MSD Trajectory Data'
# if 'df_in' not in st.session_state:
#     st.session_state['df_in'] = None
# ########################################################################################################################


# ###################################################### Loading data ##################################################

st.header('File Uploader')

st.write('How many different conditions do you have?', help='A condition is a set of data that you want to compare. For example, if you have 3 different doses of a drug and a control, then you have 4 conditions.')
st.info('A condition is a set of data that you want to compare. For example, if you have 3 different doses of a drug and a control, then you have 4 conditions. Currently, the maximum number of conditions is 10. Please contact the developer if you need more.', icon="ℹ️")
num_conditions = st.number_input('Number of conditions', min_value=1, max_value=10, value=1, step=1, help='Please enter a number between 1 and 10')
st.session_state['num_conditions'] = num_conditions
if num_conditions == 10:
    st.warning('Currently, the maximum number of conditions is 10. Please contact the developer if you need more.', icon="🚨")

conditions_list = streamlit_tags.st_tags(
            label='## Enter condition names:',
            text='Press enter to add more',
            key='1', 
            maxtags=num_conditions)

if len(conditions_list) != num_conditions:
    st.write(f'You have entered {len(conditions_list)} conditions so far. Please add', num_conditions - len(conditions_list), 'more.')
else:
    st.write('Awesome! we are good to go')
    st.session_state['conditions_list'] = conditions_list
    
    data_dict = {} # initialize data_dict to store data uploaded from file loaders for each condition
    for condition in conditions_list:
        data_dict[condition] = None # set value as none at first
        st.session_state['data_dict'] = data_dict # save to session state
    
    for condition in conditions_list:
        #st.write(f'For experimental condition {condition}, please upload files')
        files = st.file_uploader(f' For experimental condition {condition}, please upload files', type="csv", accept_multiple_files=True)
        if len(files) != 0:
            st.write('You uploaded', len(files), 'files')
            if len(files) == 1:
                st.write(files[0].name)
                data_dict[condition] = pd.read_csv(files[0])
            else:
                concat_df = data_loading.concatenate_csv_files(files)
                st.session_state['data_dict'][condition] = concat_df
        else:
            st.write('No files yet for', condition)
    st.session_state['data_dict'] = data_dict # save to session state
    st.session_state['df_in'] = True # set df_in to True to indicate that data has been uploaded







file_opts = st.sidebar.expander('File Options', expanded=True)
use_demo = file_opts.checkbox(label="Use Demo Data",
                              value=st.session_state['demo'],
                              on_change=ss.binaryswitch,
                              args=('demo',))

# create file uploader
# uploaded_files = file_opts.file_uploader("Upload CSV",
#                                  type="csv",
#                                  accept_multiple_files=True,)
# clear uploaded files if needed
clear = file_opts.button("Clear Uploaded Files", on_click=ss.clear_output)
if clear:
    st.experimental_rerun()
                                 

ftype_list = ['MSD Trajectory Data', 'Trajectory Features Data', 'Geomean or Geosem Data']
file_type = file_opts.radio(label="Select data type for upload", options = ftype_list,
                             index = ftype_list.index(st.session_state['file_type']))
ss.save_state(dict(file_type = file_type))

# if len(uploaded_files) != 0:
#     ss.save_state(dict(df_in = uploaded_files))
# elif st.session_state['demo']:
#     ss.save_state(dict(df_in=None))
# else:
#     st.session_state['df_in'] = st.session_state['df_in']


# # check if file has been uploaded
#if uploaded_files is not None:
    #st.session_state['DATA_LOADED'] = False
#     # check if the file has real data and has the specified columns
#     df = pd.read_csv(uploaded_files)
#     if data_loading.check_mpt_data(df, ['alpha']):
#         # display the dataframe
#         st.write(df)
#         st.session_state['df_in'] = df
#     else:
#         st.write('Please upload a valid CSV file with the correct columns.')

# ########################################################################################################################

# # Complicated conditions
# ## 1. have files uploaded and not using demo
# ## 2. no files uploaded and using demo
# ## 3. have files uploaded and using demo
# ## 4. no files uploaded and no demo



# Condition 1: have files uploaded and not using demo
if st.session_state['df_in'] is not None and st.session_state['demo'] is False:
    #st.write('Condition 1 is active')
    pass

# Condition 2: no files uploaded and using demo
elif st.session_state['df_in'] is False and st.session_state['demo'] is True:
    #st.write('Condition 2 is active')
    demo_datasets = {
        'MSD Trajectory Data': 'diff_viz/tests/testing_data/msd_P17_1h_OGD_1d_40nm_slice_1_cortex_vid_1.csv',
        'Trajectory Features Data': 'diff_viz/tests/testing_data/demo_data.csv',
        'Geomean or Geosem Data': 'diff_viz/tests/testing_data/geomean_P17_NT_1d_40nm_slice_1_cortex_vid_1.csv',
    }

    if st.session_state['file_type'] == 'MSD Trajectory Data':
        demo_df = pd.read_csv(demo_datasets['MSD Trajectory Data'])
        st.session_state['df_in'] = True
    elif st.session_state['file_type'] == 'Trajectory Features Data':
        demo_df = pd.read_csv(demo_datasets['Trajectory Features Data'])
        st.session_state['df_in'] = True
    else:
        demo_df = pd.read_csv(demo_datasets['Geomean or Geosem Data'])
        st.session_state['df_in'] = True
        
# Condition 3: have files uploaded and using demo
elif st.session_state['data_dict'] is not None and st.session_state['demo'] is True:
    #st.write('Condition 3 is active')
    st.sidebar.warning('You have uploaded files and selected to use demo data. Please select only one option.', icon="🚨")

# Condition 4: no files uploaded and no demo
else:
    #st.write('Condition 4 is active')
    st.write('Please upload a valid CSV file with the correct columns.')
    
view_df = file_opts.checkbox("View demo/uploaded MPT dataset", 
                             value = st.session_state['view_df'], 
                             on_change=ss.binaryswitch, args=('view_df', ))

if view_df:
    if st.session_state['demo']:
        st.write('Demo dataset:')
        st.write(demo_df)
    elif num_conditions == 1:
        st.write('Uploaded dataset:')
        st.write(st.session_state['data_dict'])
    else:
        st.write('Uploaded dataset:')
        tabs_name_list = [condition + ' Condition data' for condition in conditions_list]
        tabs = st.tabs(tabs_name_list)

        for i, condition in enumerate(conditions_list):
            with tabs[i]:
                st.write(st.session_state['data_dict'][condition])
else:
    pass
    #st.write(st.session_state['df_in'])
