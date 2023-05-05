import streamlit as st
import pandas as pd
import random
import string

output_type = st.text_input('Output Type')
date_collected = st.text_input('Date Collected')
magnification = st.text_input('Magnification')
frames_per_second = st.text_input('Frames Per Second')
model_system = st.text_input('Model System')

if 'input_keys' not in st.session_state:
    st.session_state.input_keys = []

# make it possible to add more variables
variable_1 = st.text_input('Variable 1')
variable_2 = st.text_input('Variable 2')

if st.button("Add another variable"):
    st.session_state.input_keys.append(random.choice(string.ascii_uppercase)+str(random.randint(0,999999)))

variable_count = 2
input_values = []
for input_key in st.session_state.input_keys:
    input_value = st.text_input(f"Variable {variable_count + 1}", key=input_key)
    variable_count += 1
    input_values.append(input_value)
    


replicate_number = st.text_input('Replicate Number')

st.write('You selected:', output_type, date_collected, magnification, frames_per_second, model_system, variable_1, variable_2, replicate_number) 
