## Certification Input Attributes Detail Introduction

|Name|Type|Description|
| --- | --- | --- |
| diagnosis_inputs | List of Object | Define the entire data inputs for the entire following diagnosis process. |
| diagnosis_inputs.name | String | Represent the corresponding diagnosis function which will use the data as data source that defined by this diagnosis_inputs block in current plugin. |
| diagnosis_inputs.enable | Boolean | Represent whether this data input would be enabled in the current plugin. |
| diagnosis_inputs.inputs | List of Object | Define all detail information of required inputs for current data source retrieving. |
| diagnosis_inputs.inputs.name | String | Define a name for current input block |
| diagnosis_inputs.inputs.input_datas | List of Object | Represent detail parsers or system table information, define the mapping relationship between data source table and common report table.<br> ***Note:*** During one input_datas block, can only using parsers or only using system table as data source, parsers and system tables cannot both exist in one input_datas block.|
| diagnosis_inputs.inputs.input_datas.parser | String | Define one parser which will be considered as data source for current diagnosis function by using parser file path in NetBrain System.  ***Note:*** if customer provide values for "parser" element, then "system_table" cannot be filled.|
| diagnosis_inputs.inputs.input_datas.system_table | String | Define one system table which will be considered as data source for current diagnosis function by using system table name. ***Note:*** only one system table can be defined in each input_datas, if customer provide values for "system_table" element, then "parser" cannot be filled.|
| diagnosis_inputs.inputs.input_datas.variable_mapping | Object | Define column relationships between parser table and common table. Note: the common table is the result data table which will be generated as diagnosis result per current inputs block. |
| diagnosis_inputs.inputs.input_datas.index_variables | List of String | Define the index rule of current common table specify the common table column title, support muilti-column.  |
|diagnosis_inputs.inputs.input_datas.extend_common_variables | List of String| List the columns which will be appended into common table as additional data from the parser or system table defined in "parsers" and "system_table" elements by column titles.|
| diagnosis_inputs.inputs.qualification | Object | Define the filters for all data which will be used in current daignosis function. |
| diagnosis_inputs.inputs.qualification.gdr | Object | Represent the GDR which will be considered as a filter for devices, e.g. vendor name, device type, etc. |
| diagnosis_inputs.inputs.qualification.gdr.expression | Boolean | Represent the logic relationship between each gdr_qulification conditions. (A AND B OR C AND D...) |
| diagnosis_inputs.inputs.qualification.gdr.conditions | List of String  | Represent which GDRs would be considered as conditions for qualification. ["vendor", "device_type", ...] |
| diagnosis_inputs.inputs.qualification.gdr.conditions.value | String | Define the value corresponding to the schema which inserted in current "condition". |
| diagnosis_inputs.inputs.qualification.gdr.conditions.operator | Integer | Define the operator of current condition. E.g. {subTypeName(schema) 4(operator) Cisco(value)} ==> {subTypeName = Cisco} |
| diagnosis_inputs.inputs.qualification.gdr.conditions.schema | String | Define current GDR key, check GDR management in tenant management page. |
| diagnosis_inputs.inputs.qualification.patterns | List of String | Represent the config patterns which will be considered as a filter for daignosis data. |
| diagnosis_inputs.inputs.qualification.regexes | List of String | Represent the regex rules which will be considered as a filter for diagnosis data. |
| diagnosis_functions | List of String | List all provided diagnosis functions for current platform certification plugin by diagnosis function name. All diagnosis functions will be triggered automatically when the plugin start to run. If customer desire to apply partial functions in current plugin, please comment out the functions which will be ignored. |
| global_setting | Object | Represent the global settings for current plugin  |
| debug_options | Object | Define the debug features of current diagnosis process. |
| global_setting.debug_options.build_common_table_from_inputs | Boolean | Represent whether build the common table base on customer inputs. |
| global_setting.debug_options.build_digital_twin | Boolean | Represent whether build the digital twin table base on customer inputs. |
| global_setting.debug_options.run_diagnosis | Boolean | Represent whether trigger the diagnosis process base on customer inputs. |
| global_setting.debug_options.use_parser_cache_data | Boolean | Represent whether trigger the entire plugin use parser cache data. |
| global_setting.white_ip_list | List of String | Represent all IPs that need to be ignored by the current plugin during plugin running. |
| global_setting.enable_whilte_ip_list | Boolean | Represent whether the customer needs to enable the white_ip_list feature. |
| global_setting.log_level | Integer | Represent the level that the customer wants to apply to the plugin running logs. (0: DEBUG, 1: INFO, 2: WARNING, 3: ERROR) |