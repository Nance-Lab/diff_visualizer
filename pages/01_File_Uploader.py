import streamlit as st
import pandas as pd
from diff_viz import data_loading

# ###################################################### SESSION STATES ##################################################
st.session_state.update(st.session_state)
if 'DATA_LOADED' not in st.session_state:
    st.session_state['DATA_LOADED'] = False

if 'file_type' not in st.session_state:
    st.session_state['file_type'] = 'MSD Trajectory Data'

# ########################################################################################################################

st.header('File Uploader')

file_opts = st.sidebar.expander('File Options', expanded=True)

# create file uploader
uploaded_file = st.file_uploader("Upload CSV", type="csv")

ftype_list = ['MSD Trajectory Data', 'Trajectory Features Data', 'Geomean or Geosem Data']
file_type = file_opts.radio(label="Select data type for upload", options = ftype_list,
                             index = ftype_list.index(st.session_state['file_type']))

# check if file has been uploaded
if uploaded_file is not None:
    # check if the file has real data and has the specified columns
    df = pd.read_csv(uploaded_file)
    if data_loading.check_mpt_data(df, ['alpha']):
        # display the dataframe
        st.write(df)
        #st.session_state['DATA_LOADED'] = True
    else:
        st.write('Please upload a valid CSV file with the correct columns.')

