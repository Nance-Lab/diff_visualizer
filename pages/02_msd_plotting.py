"""
Page for the MSD Plotting tab
"""

import streamlit as st
import pandas as pd

from diff_viz.msd import plot_individual_msds

st.session_state.update(st.session_state)
st.header('MSD Plotting')

if 'df_in' not in st.session_state:
    st.session_state['df_in'] = None # initialize df_in if not already initialized

if st.session_state['df_in'] is False:
    st.error('Please upload a valid CSV file using the File Uploader') # if df_in is None, then no file has been uploaded

if st.session_state['file_type'] == 'MSD Trajectory Data':
    st.sidebar.header('MSD Plotting Options')
    x_range = st.sidebar.slider('x_range', 0, 100, 10)
    y_range = st.sidebar.slider('y_range', 0, 100, 100)
    # umppx = st.number_input('umppx', 0.0)
    # fps = st.number_input('fps', 0.0)
    # alpha = st.number_input('alpha', 0.0)
    # figsize = st.number_input('figsize', 0.0)
    # subset = st.checkbox('subset')
    # size = st.number_input('size', 0.0)
    # dpi = st.number_input('dpi', 0.0)
    #df = pd.read_csv(demo_datasets['MSD Trajectory Data'])
    if st.session_state['demo'] is True:
        data_to_plot = pd.read_csv('diff_viz/tests/testing_data/msd_P17_1h_OGD_1d_40nm_slice_1_cortex_vid_1.csv')
    elif st.session_state['df_in'] is True and st.session_state['num_conditions'] ==1:
        data_to_plot = st.session_state['data_dict'][st.session_state['conditions_list'][0]]
    else:

        

        st.write('Sorry, Nels has not made this possible yet.')
    render = st.sidebar.checkbox('Show MSD Trajectory plot?')
    if render:
        fig = st.pyplot(plot_individual_msds(data_to_plot, x_range=x_range, y_range=y_range))

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

