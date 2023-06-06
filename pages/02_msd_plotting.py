import streamlit as st

st.session_state.update(st.session_state)
st.header('MSD Plotting')

if 'file_type' is 'MSD Trajectory Data':
    st.write('Sorry, this feature is not yet available! - Brendan and Nels')
elif 'file_type' is 'Trajectory Features Data':
    st.error('You uploaded a Trajectory Features Data file. Please upload a valid MSD Trajectory Data file.')
elif 'file_type' is 'Geomean or Geosem Data':
    st.error('You uploaded a Geomean or Geosem Data file. Please upload a valid MSD Trajectory Data file.')
else:
    st.error('Please upload a valid CSV file using the File Uploader')

