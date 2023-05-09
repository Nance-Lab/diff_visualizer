import streamlit as st
import streamlit_tags
from io import StringIO
import json

metadata_dict = {}


with st.sidebar:
    st.sidebar.title("Metadata format")
    st.sidebar.write("After you add in your information, your metadata file will be displayed here.")
    st.sidebar.write("You can copy and paste it into a text file and save it as a .json file.")

st.write('## Please enter background information about your experiment.')
output_type = st.text_input('Output Type (ex. features, traj, geomean, geosem)')
if output_type:
    metadata_dict['output_type'] = output_type

date_collected = st.text_input('Date Collected')
if date_collected:
    metadata_dict['date_collected'] = date_collected

magnification = st.text_input('Magnification')
if magnification:
    metadata_dict['magnification'] = magnification

frames_per_second = st.text_input('Frames Per Second')
if frames_per_second:
    metadata_dict['frames_per_second'] = frames_per_second

model_system = st.text_input('Model System (ex. rodent, agarose)')
if model_system:
    metadata_dict['model_system'] = model_system

if 'input_keys' not in st.session_state:
    st.session_state.input_keys = []

# make it possible to add more variables

st.write('## Please enter information about the experimental design. If you have a factorial experimental design, you can add multiple levels of variables')

keywords_level_one = streamlit_tags.st_tags(
    label='Keywords for age and sex experimental variables (ex. P10F, P14F, P35M)',
    text='Press enter to add more', key='1')
if keywords_level_one:
    metadata_dict['age/sex keywords'] = keywords_level_one

keywords_level_two = streamlit_tags.st_tags(
    label='Keywords for region experimental variables (ex. cortex, hippocampus, striatum)',
    text='Press enter to add more', key='2')
if keywords_level_two:
    metadata_dict['keywords_level_two'] = keywords_level_two

keywords_level_three = streamlit_tags.st_tags(
    label='Keywords for any treatment or condition experimental variables (ex. control, OGD, rotenone)',
    text='Press enter to add more', key='3')
if keywords_level_three:
    metadata_dict['keywords_level_three'] = keywords_level_three

keywords_level_four = streamlit_tags.st_tags(
    label='Keywords for any experimental variables related to treatment or condition (ex. 4DIV, 10uM)',
    text='Press enter to add more', key='4')
if keywords_level_four:
    metadata_dict['keywords_level_four'] = keywords_level_four



with st.sidebar:
    #st.sidebar.write(json.dumps(metadata_dict, indent=4))
    st.sidebar.json(metadata_dict)

st.write('Based on your input, you have the following experimental conditions:')
experimental_conditions = []

for val_one in keywords_level_one:
    experimental_condition = ''
    experimental_condition_val_one = experimental_condition + ' ' + val_one
    for val_two in keywords_level_two:
        experimental_condition_val_two = experimental_condition_val_one + ' ' + val_two
        if keywords_level_three:
            for val_three in keywords_level_three:
                experimental_condition_val_three = experimental_condition_val_two + ' ' + val_three
                if keywords_level_four:
                    for val_four in keywords_level_four:
                        experimental_condition_val_four = experimental_condition_val_three + ' ' + val_four
                        experimental_conditions.append(experimental_condition_val_four)
                else:
                    experimental_conditions.append(experimental_condition_val_three)
        else:
            experimental_conditions.append(experimental_condition_val_two)

for exp_cond in experimental_conditions:
    st.write(exp_cond)


                        

# num_level_one = len(keywords_level_one)
# num_level_two = len(keywords_level_two)
# for i, val_one in enumerate(keywords_level_one):
#     for ii, val_two in enumerate(keywords_level_two):
#         st.write(val_one, ' ', val_two)
#         experimental_conditions.append([val_one, val_two])
#     #st.write(keywords_level_one[0])

is_correct = st.checkbox('Is this correct? If not, please go back and edit the information you entered.')

if is_correct:
    st.write('Great!')
    metadata_dict['testing'] = 'experimental_conditions'
    for i, experimental_condition in enumerate(experimental_conditions):
        #st.write(f'For experimental condition {experimental_conditions[i]}, please upload files')
        files = st.file_uploader(f'For experimental condition {experimental_conditions[i]}, please upload files', type="csv", accept_multiple_files=True, key=experimental_condition)
        if files is not None:
            st.write('You uploaded', len(files), 'files')
            #st.write(files[0].name) 


    

#st.write('You selected:', output_type, date_collected, magnification, frames_per_second, model_system, variable_1, variable_2, replicate_number) 


metadata_file = json.dumps(metadata_dict, indent=4)
st.write('Download your metadata file here!')
st.download_button(label="Download metadata file", data=metadata_file, file_name='metadata.json', mime='application/json')