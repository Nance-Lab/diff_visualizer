import streamlit as st

st.session_state.update(st.session_state)
st.header('MSD Plotting')

if 'DATA_LOADED' == True:
    st.write('Sorry, this feature is not yet available! - Brendan and Nels')
else:
    st.error('Please upload a valid CSV file using the File Uploader')

