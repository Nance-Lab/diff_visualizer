import streamlit as st
import pandas as pd
from diff_viz import data_loading, diffusion_modes

st.header('Diff Viz: Your One Stop Shop for MPT Plots!')

DATA_LOADED = False # flag to check if data has been loaded

# create file uploader
uploaded_file = st.file_uploader("Upload CSV", type="csv")

# check if file has been uploaded
if uploaded_file is not None:
    # check if the file has real data and has the specified columns
    df = pd.read_csv(uploaded_file)
    if data_loading.check_csv_data(df, ['alpha']):
        # display the dataframe
        st.write(df)
        DATA_LOADED = True
    else:
        st.write('Please upload a valid CSV file with the correct columns.')

# Create a dropdown menu for the user to select a plot type, but only if data has been loaded
if DATA_LOADED:
    st.write('What type of plot would you like to see?')
    options = ['Diffusion Modes', 'MSDs', 'Individual Trajectories']
    PLACEHOLDER = 'Select a plot type'
    options.insert(0, PLACEHOLDER)
    choice = st.selectbox('Select a plot type', options)
    if choice is not None and choice != PLACEHOLDER:
        st.write('You selected:', choice)

        # Generate the selected plot based on the user's choice
        if choice == 'Diffusion Modes':
            diffusion_modes.plot_diffusion_modes(ecm=df, target='alpha')
        elif choice == 'MSDs':
            st.write('Sorry, this feature is not yet available! - Nels')
        elif choice == 'Individual Trajectories':
            st.write('Sorry, this feature is not yet available! - Nels')
