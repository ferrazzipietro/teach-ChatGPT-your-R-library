import openai
import pandas as pd
import subprocess
import os
import json
from parse_R_functions import from_file_to_df

# Read the JSON file
with open('config.json') as f:
    config = json.load(f)

# Convert the JSON fields to variables
API_KEY = config['api_key']
model_engine = config['model_engine']
source_functions_loc1 = config['source_functions_loc1']
ENV_NAME = config['ENV_NAME']
suffix = config['suffix']

# Print the variables
print("api_key:", api_key)
print("model_engine:", model_engine)
print("source_functions_loc1:", source_functions_loc1)
print("ENV_NAME:", ENV_NAME)
print("suffix:", suffix)

df = from_file_to_df(source_functions_loc1)
df.to_csv('prepared_data.csv', index=False)

subprocess.run('conda run -n {ENV_NAME}; openai tools fine_tunes.prepare_data --file prepared_data.csv --quiet', shell=True)
subprocess.run( f"conda run -n {ENV_NAME}; openai -k {API_KEY} api fine_tunes.create -t 'prepared_data_prepared (1).jsonl' --model {model_engine} --suffix {suffix}", shell=True)