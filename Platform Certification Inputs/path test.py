import yaml
import json
import os
from os import listdir
from os.path import isfile, join
import sys

root_path = os.path.dirname(os.path.realpath(__file__))
final_json = {}
with open(root_path + '\\' + 'Common Settings.yaml') as file:
    final_json = yaml.load(file)
final_json['diagnosis_inputs'] = []
folder_list = [fp[0] for fp in os.walk(root_path)]
for folder in folder_list:
    if folder != root_path:
        onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
        if 'Common Settings.yaml' in onlyfiles:
            temp_json = {}
            with open(folder + '\\' + 'Common Settings.yaml') as file:
                temp_json = yaml.load(file)
            if 'inputs' in temp_json.keys():
                inputs = temp_json['inputs']
                for file_name in onlyfiles:
                    if file_name != 'Common Settings.yaml':
                        input_block = {}
                        with open(folder + '\\' + file_name) as file:
                            input_block = yaml.load(file)
                        inputs.append(input_block)
                final_json['diagnosis_inputs'].append(temp_json)
# print(final_json)
# print(yaml.dump(yaml.load(json.dumps(final_json)), default_flow_style=False))
with open(root_path + '\\combined_yaml.yaml', 'w') as file:
    yaml.dump(yaml.load(json.dumps(final_json)), file, default_flow_style=False)