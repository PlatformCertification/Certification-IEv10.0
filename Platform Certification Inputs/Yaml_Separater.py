import yaml
import json
import os
from os import listdir
from os.path import isfile, join
import sys

# root_path = os.path.dirname(os.path.realpath(__file__))
# modify the root path to where you save the yaml file, also update the file name in main function 
root_path = 'D:\\Temp Folder for File Transfer\\Yaml Separator test'
final_json = {}
variable_mapping_checker = {
    'Common Interface Table': ['Device', 'Intf', 'IntfMac', 'IntfIP'],
    'Common L2 Neighbor Table': ['NbrDev', 'NbrIntfIP', 'NbrIntf', 'Intf'],
    'Common L3 Neighbor Table': ['AreaID', 'Intf', 'NbrIntfIP', 'NbrIntfMAC']
}

def yaml_loader(path):
    result = {}
    with open(path) as file:
        result = yaml.load(file)
    return result 

def yaml_writer(file_name, temp_json, file_path):
    with open(file_path + '\\{}.yaml'.format(file_name), 'w') as file:
        yaml.dump(yaml.load(json.dumps(temp_json)), file, default_flow_style=False)
        
def createFolder(folder_path):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except OSError:
        print ('Error: Creating folder_path. ' +  folder_path)

def vm_word_checking(checking_list, vm_json):
    if vm_json: 
        for key, value in vm_json.items():
            if value not in checking_list:
                print("value ===== ", value)
#                 raise Exception(value+ " from variable_mapping wrong, expect: " + str(checking_list))
                return False
            continue
        return True
        
        
def folder_file_builder(temp_json, folder_name):
    sub_folder = root_path + '\\' + folder_name
    createFolder(sub_folder)
    sub_common_setting = {}
    sub_common_setting['common_table_name'] = temp_json['common_table_name']
    checking_list = variable_mapping_checker[temp_json['common_table_name']]
    sub_common_setting['enable'] = temp_json['enable']
    sub_common_setting['name'] = temp_json['name']
    sub_common_setting['inputs'] = []
    yaml_writer('Common Settings', sub_common_setting, sub_folder)
    inputs = temp_json['inputs']
    if len(inputs) >= 1:
        for _input in inputs:
            flag = True
            input_datas = _input['input_datas']
            sub_file_name = _input['name']
            for input_data in input_datas:
                vmapping_json = input_data['variable_mapping']
                flag = vm_word_checking(checking_list, vmapping_json)
                if flag:
                    continue
                else:
                    break
            if flag:
                yaml_writer(sub_file_name, _input, sub_folder)
            else:
                raise Exception('Syntax error in your variable_mapping of => ' + temp_json['name'] + " => " + sub_file_name)

if __name__ == "__main__":    
    yaml_path = root_path + '\\combined_yaml.yaml'  #update your file name here.      
    full_input_json = yaml_loader(yaml_path)
    full_common_setting = {}
    full_common_setting['diagnosis_functions'] = full_input_json['diagnosis_functions']
    full_common_setting['global_setting'] = full_input_json['global_setting']
    full_common_setting['diagnosis_inputs'] = []
    yaml_writer("Common Settings", full_common_setting, root_path)

    diagnosis_inputs = full_input_json['diagnosis_inputs']
    if len(diagnosis_inputs) >= 1:
        for diagnosis_input in diagnosis_inputs:
            folder_name = diagnosis_input['name']
            folder_file_builder(diagnosis_input, folder_name)
