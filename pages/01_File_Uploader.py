import streamlit as st
import pandas as pd
from diff_viz import data_loading
from helper_functions.session_state import ss
from io import BytesIO


# ###################################################### SESSION STATES ##################################################
st.session_state.update(st.session_state)
ss.initialise_state(state_dict = {'file_type': None,
                                   'df_in': None,
                                   'demo': False,
                                   'view_df': False,
                                   })

# st.session_state.update(st.session_state)
# if 'DATA_LOADED' not in st.session_state:
#     st.session_state['DATA_LOADED'] = False

# if 'file_type' not in st.session_state:
#     st.session_state['file_type'] = 'MSD Trajectory Data'
# if 'df_in' not in st.session_state:
#     st.session_state['df_in'] = None

# ########################################################################################################################

st.header('File Uploader')

file_opts = st.sidebar.expander('File Options', expanded=True)
use_demo = file_opts.checkbox(label="Use Demo Data",
                              value=st.session_state['demo'],
                              on_change=ss.binaryswitch,
                              args=('demo',))

# create file uploader
uploaded_files = file_opts.file_uploader("Upload CSV",
                                 type="csv",
                                 accept_multiple_files=True,)
                                 

ftype_list = ['MSD Trajectory Data', 'Trajectory Features Data', 'Geomean or Geosem Data']
file_type = file_opts.radio(label="Select data type for upload", options = ftype_list,
                             index = ftype_list.index(st.session_state['file_type']))
ss.save_state(dict(file_type = file_type))

if len(uploaded_files) != 0:
    ss.save_state(dict(df_in = uploaded_files))
elif st.session_state['demo']:
    ss.save_state(dict(df_in=None))
else:
    st.session_state['df_in'] = st.session_state['df_in']
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

# # Complicated conditions
# ## 1. have files uploaded and not using demo
# ## 2. no files uploaded and using demo
# ## 3. have files uploaded and using demo
# ## 4. no files uploaded and no demo

if st.session_state['df_in'] is not None and st.session_state['demo'] is False:
    pass

elif st.session_state['df_in'] is None and st.session_state['demo'] is True:
    demo_datasets = {
        'MSD Trajectory Data': 'diff_viz/tests/testing_data/msd_P17_1h_OGD_1d_40nm_slice_1_cortex_vid_1.csv',
        'Trajectory Features Data': 'diff_viz/tests/testing_data/features_P14_40nm_s1_v1.csv',
        'Geomean or Geosem Data': 'diff_viz/tests/testing_data/geomean_P17_NT_1d_40nm_slice_1_cortex_vid_1.csv',
    }

    if st.session_state['file_type'] == 'MSD Trajectory Data':
        df = pd.read_csv(demo_datasets['MSD Trajectory Data'])
        st.session_state['df_in'] = df
    elif st.session_state['file_type'] == 'Trajectory Features Data':
        df = pd.read_csv(demo_datasets['Trajectory Features Data'])
        st.session_state['df_in'] = df
    else:
        df = pd.read_csv(demo_datasets['Geomean or Geosem Data'])
        st.session_state['df_in'] = df
        

elif st.session_state['df_in'] is not None and st.session_state['demo'] is True:
    pass

else:
    pass
    
view_df = file_opts.checkbox("View demo/uploaded MPT dataset", value = st.session_state['view_df'], on_change=ss.binaryswitch, args=('view_df', ))

if view_df:
    if st.session_state['demo']:
        st.write('Demo dataset:')
    else:
        st.write('Uploaded dataset:')
    st.write(st.session_state['df_in'])
