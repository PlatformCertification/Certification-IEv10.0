import yaml
import json
import os
from os import listdir
from os.path import isfile, join
import sys

root_path = os.path.dirname(os.path.realpath(__file__))
# root_path = 'D:\\GitHub\\Certification-IEv10.0\\Platform Certification Inputs'
final_json = {}

def yaml_loader(path):
    result = {}
    with open(path) as file:
        result = yaml.load(file)
    return result 

def yaml_writer(file_name, temp_json):
    with open(root_path + '\\{}.yaml'.format(file_name), 'w') as file:
        yaml.dump(yaml.load(json.dumps(temp_json)), file, default_flow_style=False)
        
if __name__ == "__main__":
    diagnosis_setting_path = root_path + '\\' + 'Common Settings.yaml'
    final_json = yaml_loader(diagnosis_setting_path)
    final_json['diagnosis_inputs'] = []
    folder_list = [fp[0] for fp in os.walk(root_path)]
    for folder in folder_list:
        if folder != root_path:
            onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
            if 'Common Settings.yaml' in onlyfiles:
                temp_json = {}
                input_setting_path = folder + '\\' + 'Common Settings.yaml'
                temp_json = yaml_loader(input_setting_path)
                if 'inputs' in temp_json.keys():
                    inputs = temp_json['inputs']
                    for file_name in onlyfiles:
                        if file_name != 'Common Settings.yaml':
                            input_block = {}
                            input_data_path = folder + '\\' + file_name
                            input_block = yaml_loader(input_data_path)
                            inputs.append(input_block)
                    final_json['diagnosis_inputs'].append(temp_json)
    yaml_writer('combined_yaml', final_json)