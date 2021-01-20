## Certification Input Attributes Detail Introduction

|Name|Type|Description|
| --- | --- | --- |
| diagnosis_inputs | List of Object | Define the entire data inputs for the entire following diagnosis process. |
| diagnosis_inputs.name | String | Represent which certification will be considered in current plugin |
| diagnosis_inputs.description | String | Represent the breif explanation of current diagnosis inputs |
| diagnosis_inputs.enable | Boolean | Represent whether this data input would be enabled in the current plugin. |
| diagnosis_inputs.inputs | List of Object | Define all detail information of required inputs for current data source retrieving. |
| diagnosis_inputs.inputs.name | String | Represent the corresponding table of current inputs |
| diagnosis_inputs.inputs.description | String | RepresentÂ the description of the current data source,Â  for example, the protocol will be used. |
| diagnosis_inputs.inputs.devices | List of String | Point out all devices which would be considered as data sources for current diagnosis process. |
| diagnosis_inputs.inputs.input_datas | List of Object | Represent further detail inputs data for current diagnosis. |
| diagnosis_inputs.inputs.input_datas.parser | String | Point out the parsers which will be used during diagnosis data sources. |
| diagnosis_inputs.inputs.input_datas.cli_cmds | List of String | RepresentÂ the commands that will be used for cusrrent diagnosis data retrieving . |
| diagnosis_inputs.inputs.input_datas.system_table | String | Represent the system table which will be considered as a data source for diagnosis purpose. |
| diagnosis_inputs.inputs.input_datas.variable_mapping | Object | Define column relationships between parser table and common table. Note: the common table is the result data table which generated per current inputs block. |
| diagnosis_inputs.inputs.input_datas.variable_mapping.<variable from parser> | Data Pair | Point out the connections between parser column and common table column. E.g. "Interface" column in parser is corresponding to the "Interface" column in common table. |
| diagnosis_inputs.inputs.input_datas.common_table_definition | Object | Point out the common tables which would be generated per entire inputs block. |
| diagnosis_inputs.inputs.input_datas.common_table_definition.common_table_name | String  | Represent the current common table name.  |
| diagnosis_inputs.inputs.input_datas.common_table_definition.index_variables | List of String | Define the index of current common table base on common table column title, support muilti columns.  |
| diagnosis_inputs.inputs.input_datas.common_table_definition.table_variables | List of String | Define current common table schema by column titles. |
| diagnosis_inputs.inputs.qualification | Object | Represent the column that will be considered as a filter for devices. |
| diagnosis_inputs.inputs.qualification.expression | String | Represent the logic relationship betweenÂ gdr_qulification,Â patterns, andÂ regexes. (A AND B OR C) |
| diagnosis_inputs.inputs.qualification.gdr | Object | Represent the GDR which will be considered as a filter for devices, e.g.Â vendor name, device type, etc. |
| diagnosis_inputs.inputs.qualification.gdr.expression | Boolean | Represent the logic relationship betweenÂ eachÂ gdr_qulification conditions. (A AND B OR C AND D...) |
| diagnosis_inputs.inputs.qualification.gdr.conditions | List of StringÂ  | Represent which GDRs would be considered as conditions for qualification.Â ["vendor", "device_type", ...] |
| diagnosis_inputs.inputs.qualification.gdr.conditions.value | String | Define the current condition value. |
| diagnosis_inputs.inputs.qualification.gdr.conditions.operator | Integer | Define the operator of current condition |
| diagnosis_inputs.inputs.qualification.gdr.conditions.key | String | Define current GDR key, check GDR management in tenant management page. |
| diagnosis_inputs.inputs.qualification.patterns | List of String | Represent the config patterns which will be considered as a filter for daignosis data. |
| diagnosis_inputs.inputs.qualification.regexes | List of String | Represent the regex rules which will be considered as a filter for diagnosis data. |
| diagnosis_functions | Object | The body to describe the entire diagnosis requirements.Â  |
| diagnosis_functions.diagnosis_reports | List of Object | The list represents all customer required plugin checks. |
| diagnosis_functions.diagnosis_reports.description | String | Describe the purpose and adventage of current diagnosis report. |
| diagnosis_functions.diagnosis_report.action | String | Define all included actions which would be triggered during current diagnosis process. |
| diagnosis_functions.diagnosis_report.enable | Boolean | Represent whether the current diagnosis report would be enabled. true: enabled, false: disabled. |
| diagnosis_functions.diagnosis_fixings | List of Object | Represent the fixing process base on customer requirements. |
| diagnosis_functions.diagnosis_fixing.action | String | Represent which fixing process can be applied to the customer environment. |
| diagnosis_functions.diagnosis_fixing.enable | Boolean | Represent whether the fixing process will be enabled. |
| global_setting | Object | Represent the global settings for current pluginÂ  |
| debug_options | Object | Define the debug features of current diagnosis process. |
| debug_options.global_setting.build_common_table_from_inputs | Boolean | Represent whether build the common table base on customer inputs. |
| debug_options.global_setting.build_digital_twin | Boolean | Represent whether build the digital twin table base on customer inputs. |
| debug_options.global_setting.run_diagnosis | Boolean | Represent whether trigger the diagnosis process base on customer inputs. |
| debug_options.global_setting.use_parser_cache_data | Boolean | Represent whether trigger the entire plugin use parser cache data. |
| global_setting.white_ip_list | List of String | Represent all IPs that need to be ignored by the current plugin during plugin running. |
| global_setting.enable_whilte_ip_list | Boolean | Represent whether the customer needs to enable theÂ white_ip_list feature. |
| global_setting.log_level | Integer | Represent the level that the customer wants to apply to the plugin running logs. (0: DEBUG, 1: INFO, 2: WARNING, 3: ERROR) |