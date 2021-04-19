import pandas as pd
import json

def convert_json_files_to_df(files: list):
    """Helper function to convert all Json files in the list to a pandas Dataframe"""

    json_lst = []
    for filename in files:
        with open(filename, 'r') as FILE:
            json_data = json.load(FILE)
            json_lst.append(json_data)

    return pd.json_normalize(json_lst)