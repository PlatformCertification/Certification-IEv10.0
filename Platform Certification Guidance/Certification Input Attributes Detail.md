## Certification Yaml Attributes Detail Introduction

|Name|Type|Description|
| --- | --- | --- |
| diagnosis_methods | List of Python files | Define the entire data inputs for the entire following diagnosis process. Each Python file only contains a large string with yaml structure to define one stream data resource. For detail information of each element in diagnosis_inputs, please check the following sub [table](#subTable).|
| run_setting | Object | Set the certification plugin running process. | 
| run_setting.qualification | Object | Switch of qualification process. |
| run_setting.qualification.enable | Boolean | Define whether the qualification process will be considered during current plugin running. true: considered, false: un-considered |
| run_setting.qualification.names | String | The function name in back end, cannot be modified by customer.  |
| run_setting.benchmark | Object | Switch of benchmark process. |
| run_setting.benchmark.enable | Boolean | Define whether the benchmark process will be considered during current plugin running. true: considered, false: un-considered |
| run_setting.benchmark.names | String | The function name in back end, cannot be modified by customer. |
| run_setting.diagnosis_checking | Object | Switch of diagnosis checking process. |
| run_setting.diagnosis_checking.enable | Boolean | Define whether the diagnosis checking process will be considered during current plugin running. true: considered, false: un-considered |
| run_setting.diagnosis_checking.names | List of String | List all provided diagnosis functions for current platform certification plugin by diagnosis checking name. All diagnosis checking functions will be triggered automatically when the plugin start to run. If customer desire to apply partial functions in current plugin, please comment out the functions which will be ignored. |  
| run_setting.diagnosis_fixing | Object | Switch of diagnosis fixing process. |
| run_setting.diagnosis_fixing.enable | Boolean | Define whether the diagnosis fixing will be considered during current plugin running. true: considered, false: un-considered |
| run_setting.diagnosis_fixing.names | List of String | List all provided fixing functions for current platform certification plugin by diagnosis function name. All diagnosis fixing precesses will be triggered automatically when the plugin start to run. If customer desire to apply partial fixing functions in current plugin, please comment out the functions which will be ignored. |  
| run_setting.diagnosis_undo | Object | Switch of diagnosis undo process. |
| run_setting.diagnosis_undo.enable | Boolean | Define whether the diagnosis undo process will be considered during current plugin running. true: considered, false: un-considered |
| run_setting.diagnosis_undo.names | List of String | Specify which fixing method considered in diagnosis fixing will be re-covered in current undo process.  |
| run_setting.data_collection | Object | Switch of data collection process. Purpose is to collect all devices information for customer environment (e.g. device vondor, etc). |
| run_setting.data_collection.enable | Boolean | Define whether the data collection process will be considered during current plugin running. true: considered, false: un-considered |
| run_setting.data_collection.names | String | The function name in back end, cannot be modified by customer. |
| white_ip_list | One Python File with one string | Represent all IPs that need to be ignored by the current plugin during plugin running. |
| data_collection | String name of the Python file | Define the device scope and map size for the data_collection block in run_seeting. <br> dev_source:<br>1: Error Device List, Certification_Device, Certification_Interface, {"devName":1}<br>2: Error Devices with neighbors, device same as above, include l2/l3, deepth:hard code to 1<br>3: All device of duplicate ip<br>settings:<br> max_dev_number_pre_map: maximum the number of device pre map<br>max_map_count: maximum the number of map<br>each_vendor_numbers: maximum the number of each vendor<br>|
| white_mac_list | One Python File with one string | Represent all MACs that need to be ignored by the current plugin during plugin running. |
| white_interface_list | One Python File with one string | Represent all Interfaces that need to be ignored by the current plugin during plugin running. |
| device_scope | Object | Represent the device scope information of current plugin. |
| device_scope.scope_option | Integer | Represent the type of device scope which will considered in current plugin. 0 All device, 1 Device Group, 2 Site, 3 Device Name.|
| device_scope.scope_names | string | depands on which device scope will be inserted in current plugin. If the value of scope_option is 0, no need to insert this value, if scope_option is 1 then a device group name must be provided. |
| cert_db_reset | Boolean | Define whether we need to clean the digital twin database, ture: clean the digital databse, false: do not clean digital twin database. |
| debug_options | Object | Define the debug features of current diagnosis process. |
| debug_options.build_common_table_from_inputs | Boolean | Represent whether build the common table base on customer inputs. |
| debug_options.build_digital_twin | Boolean | Represent whether build the digital twin table base on customer inputs. |
| debug_options.run_diagnosis | Boolean | Represent whether trigger the diagnosis process base on customer inputs. |
| debug_options.use_parser_cache_data | Boolean | Represent whether trigger the entire plugin use parser cache data. |
| debug_options.log_level | Integer | Represent the level that the customer wants to apply to the plugin running logs. (0: DEBUG, 1: INFO, 2: WARNING, 3: ERROR) |

## Certification Input Attributes Detail Introduction <a name="subTable"/>

|Name|Type|Description|
| --- | --- | --- |
| name | String | Represent the corresponding diagnosis function which will use the data as data source that defined by this diagnosis_inputs block in current plugin. |
| enable | Boolean | Represent whether this data input would be enabled in the current plugin. |
| common_table_name | String | Represent the name of the current common which will be generated per all input_datas in current diagnosis.| 
| inputs | List of Object | Define all detail information of required inputs for current data source retrieving. |
| inputs.name | String | Define a name for current input block |
| inputs.input_datas | List of Object | Represent detail parsers or system table information, define the mapping relationship between data source table and common report table.<br> ***Note:*** During one input_datas block, can only using parsers or only using system table as data source, parsers and system tables cannot both exist in one input_datas block.|
| inputs.input_datas.parser | String | Define one parser which will be considered as data source for current diagnosis function by using parser file path in NetBrain System.  ***Note:*** if customer provide values for "parser" element, then "system_table" cannot be filled.|
| inputs.input_datas.system_table | String | Define one system table which will be considered as data source for current diagnosis function by using system table name. ***Note:*** only one system table can be defined in each input_datas, if customer provide values for "system_table" element, then "parser" cannot be filled.|
| inputs.input_datas.variable_mapping | Object | Define column relationships between parser table and common table. Note: the common table is the result data table which will be generated as diagnosis result per current inputs block. |
| inputs.input_datas.index_variables | List of String | Define the index rule of current common table specify the common table column title, support muilti-column.  |
|inputs.input_datas.extend_common_variables | List of String| List the columns which will be appended into common table as additional data from the parser or system table defined in "parsers" and "system_table" elements by column titles.|
| inputs.qualification | Object | Define the filters for all data which will be used in current daignosis function. |
| inputs.qualification.gdr | Object | Represent the GDR which will be considered as a filter for devices, e.g. vendor name, device type, etc. |
| inputs.qualification.gdr.expression | Boolean | Represent the logic relationship between each gdr_qulification conditions. (A AND B OR C AND D...) |
| inputs.qualification.gdr.conditions | List of String  | Represent which GDRs would be considered as conditions for qualification. ["vendor", "device_type", ...] |
| inputs.qualification.gdr.conditions.value | String | Define the value corresponding to the schema which inserted in current "condition". |
| inputs.qualification.gdr.conditions.operator | Integer | Define the operator of current condition. E.g. {subTypeName(schema) 4(operator) Cisco(value)} ==> {subTypeName = Cisco}<br>  Operator: {Match = 0, NotMatch = 1, Equal = 2, NotEqual = 3, Contain = 4, NotContain = 5, GreatThan = 6, LessThan = 7, GreateThanOrEqual = 8, LessThanOrEqual = 9}|
| inputs.qualification.gdr.conditions.schema | String | Define current GDR key, check GDR management in tenant management page. |
| inputs.qualification.patterns | List of String | Represent the config patterns which will be considered as a filter for daignosis data. |
| inputs.qualification.regexes | List of String | Represent the regex rules which will be considered as a filter for diagnosis data. |

***For input sample, please click [here](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/Certification%20Input%20Example%20with%20Yaml.md).***