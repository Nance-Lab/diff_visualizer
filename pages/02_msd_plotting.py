import streamlit as st
import pandas as pd
from diff_viz.msd import plot_individual_msd

st.session_state.update(st.session_state)
st.header('MSD Plotting')

if 'df_in' not in st.session_state:
    st.session_state['df_in'] = None # initialize df_in if not already initialized

if st.session_state['df_in'] is None:
    st.error('Please upload a valid CSV file using the File Uploader') # if df_in is None, then no file has been uploaded

if st.session_state['file_type'] == 'MSD Trajectory Data':
        #df = pd.read_csv(demo_datasets['MSD Trajectory Data'])
        data = st.session_state['df_in']
        st.write(data)
else:
    st.error('The data you uploaded is not MSD Trajectory Data. Please upload a valid MSD Trajectory Data file.')


# if 'file_type' is 'MSD Trajectory Data':
#     st.write('Sorry, this feature is not yet available! - Brendan and Nels')
# elif 'file_type' is 'Trajectory Features Data':
#     st.error('You uploaded a Trajectory Features Data file. Please upload a valid MSD Trajectory Data file.')
# elif 'file_type' is 'Geomean or Geosem Data':
#     st.error('You uploaded a Geomean or Geosem Data file. Please upload a valid MSD Trajectory Data file.')
# else:
#     st.error('Please upload a valid CSV file using the File Uploader')

