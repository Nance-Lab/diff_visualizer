import streamlit as st
from diff_viz.diffusion_modes import plot_diffusion_modes

st.session_state.update(st.session_state)
st.header('Diffusion Mode Plotting')

if 'df_in' not in st.session_state:
    st.session_state['df_in'] = None

if st.session_state['df_in'] is not None:
    targ_col = st.text_input('Please input name of target column', help='This is the column that will be used to seperate the data into unique classes')
    st.session_state['targ_col'] = targ_col

    if st.button('Plot Diffusion Modes'):
        st.pyplot(plot_diffusion_modes(df=st.session_state['df_in'], label_column='age', figsize=(2,4), legend_fontsize=5))
else:
    st.error('Please upload a valid CSV file using the File Uploader')