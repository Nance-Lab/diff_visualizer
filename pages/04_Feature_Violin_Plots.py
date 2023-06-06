import streamlit as st
import matplotlib.pyplot as plt
from diff_viz.feature_distribution_plots import feature_violin_plot

st.session_state.update(st.session_state)
st.header('Violin Feature Plots')

if 'df_in' not in st.session_state:
    st.session_state['df_in'] = None


if st.session_state['df_in'] is not None:
    feature_to_plot = st.selectbox('Select feature to plot', options = st.session_state['df_in'].columns.drop('age'))
else:
    st.error('Please upload a valid CSV file using the File Uploader')

if feature_to_plot:
    fig = feature_violin_plot(df=st.session_state['df_in'], feature_to_plot=feature_to_plot, label_column='age')
    st.pyplot(fig=fig)