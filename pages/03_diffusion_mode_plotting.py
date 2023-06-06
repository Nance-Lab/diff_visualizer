import streamlit as st
from diff_viz.diffusion_modes import plot_diffusion_modes

st.session_state.update(st.session_state)
st.header('Diffusion Mode Plotting')

if 'df_in' not in st.session_state:
    st.session_state['df_in'] = None

if st.session_state['df_in'] is not None:
    st.pyplot(plot_diffusion_modes(df=st.session_state['df_in'], label_column='age', figsize=(2,4), legend_fontsize=5))
else:
    st.error('Please upload a valid CSV file using the File Uploader')