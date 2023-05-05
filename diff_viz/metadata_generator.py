"""
    This script is used to generate the metadata for the diff_viz app.       
"""     

import json

def read_json(file_path):
    """
        Reads in a json file and returns the data as a dictionary.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def write_json(data, file_path):
    """
        Writes a dictionary to a json file.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def generate_metadata(data):

    


# with open('/Users/nelsschimek/Documents/nancelab/diff_viz/diff_viz/tests/testing_data/example_metadata.json', 'r') as f:
#     data = json.load(f)

