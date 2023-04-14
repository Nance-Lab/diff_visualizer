import streamlit as st
from diff_viz import testing_module

data = testing_module.test_func()
st.header('Diff Viz: Your One Stop Shop for MPT Plots!')
st.write(data)