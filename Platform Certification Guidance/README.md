
# Platform Certification Guidance

## 1. Overall Flow

<img src="Platform Certification Guidance/images/Overall flow.png" /><br>
    
## 2. Input

### 2.1 Certification Significant Input Blocks Introduction

#### 2.1.1. diagnosis_functions.diagnosis_reports.
> Customer need to pre-define all diagnosis reports at this section which need to be generated after plugin running successfully. For each diagnosis report, customer need to provide the corresponding report name and enable flag as inputs, please check Detail Introduction for more information.

#### 2.1.2. diagnosis_functions.diagnosis_fixings
>Customer need to pre-define desired fixing processes at this section which need to be triggered automatically to fix platform related issues after plugin running successfully. For each fixing actions, customer need to provide the corresponding action name and enable flag as inputs, please check Detail Introduction for more information.

#### 2.1.3. certification_inputs
>Customer needs to insert all detail information for each certification which will be included in current plugin. Certification name, enable flag and all detail inputs must be inserted.

#### 2.1.4. certification_inputs.inputs
>As the most important section of certification_inputs, customer must review all attributes which belongs current component in below table. Customer need to take more care of the "qualification" section, we provide three kinds of qualification methods totally:

>>1. gdr_qulification
>>2. patterns
>>3. regexes

>If multiple qualification methods included, customer need to provide the boolean_expression in method level accurately to represent the relationship between each qualification method. Similar with point c, if customer provide multiple conditions in gdr_qulification, the boolean_expression in gdr_qulification level also need to be inserted accurately.

#### 2.1.5. global_setting
>Customer need to insert all corresponding values for each attribute in this section. Please check Detail Introduction for more information.

### 2.2 Certification Input Attributes Detail Introduction

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
    
### 2.3 Certification Input Example with Yaml

```Yaml
---
inputs_definition:
- name: L3 Neighbor Data
  description: 'For diagnosis function: L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  inputs:
  - name: System Table Inputs[All Vendors]
    description: ''
    devices:
    - OSPFv3-R33
    input_datas:
    - parser: ''
      cli_cmds:
      - show arp table
      system_table: ARP Table
      variable_mapping:
        Interface: Interface
        IP Address: Neighbor Interface IP
        MAC Address: Neighbor Interface MAC
      common_tables_defines:
      - index_variables:
        - Interface
        - Neighbor Interface IP
        table_variables:
        - Interface
        - Neighbor Interface IP
        - Neighbor Interface MAC
        common_table_name: Common L3 Neighbor Table
    - parser: ''
      cli_cmds:
      - show ip route
      system_table: Route Table
      variable_mapping:
        OutIf: Interface
        NextHop: Neighbor Interface IP
      common_tables_defines:
      - index_variables:
        - Neighbor Interface IP
        - Interface
        table_variables:
        - Neighbor Interface IP
        - Interface
        common_table_name: Common L3 Neighbor Table
    qualification:
      gdr:
        conditions:
        - expression: 'Cisco '
          operator: 4
          key: subTypeName
        expression: A
      patterns: []
      regexes: []
  - name: OSPF Neighbor Parser[Cisco]
    devices:
    - OSPFv3-R33
    - bjta002444-SW13
    - bjta002440-SW11
    input_datas:
    - parser: Shared Files in Tenant/Certification Tool Parsers/OSPF Neighbors Detail
        [Cisco IOS]
      cli_cmds:
      - show ip ospf neighbor detail
      system_table: ''
      variable_mapping:
        intf: Interface
        intf_addr: Neighbor Interface IP
        area_id: Area ID
      common_tables_defines:
      - index_variables:
        - Interface
        - Neighbor Interface IP
        table_variables:
        - Interface
        - Neighbor Interface IP
        - Area ID
        common_table_name: Common L3 Neighbor Table
  - gdr:
      conditions:
      - expression: Cisco Router
        operator: 4
        schema: subTypeName
      expression: A
    patterns: []
    regexes:
    - regex:router ospf [0-9]+
  - name: OSPF Neighbor Parser[Juniper]
    devices:
    - EX2200-1
    - EX2200-2
    input_datas:
    - parser: ospf parser
      cli_cmds:
      - show ospf neighbor
      system_table: ''
      variable_mapping:
        intf: Interface
        ip: Neighbor Interface IP
        area_id: Area ID
      common_tables_defines:
      - index_variables:
        - Interface
        - Neighbor Interface IP
        table_variables:
        - Interface
        - Neighbor Interface IP
        - Area ID
        common_table_name: Common L3 Neighbor Table
    qualification:
      gdr:
        conditions:
        - expression: 'Juniper '
          operator: 4
          schema: subTypeName
        expression: A
      patterns: []
      regexes:
      - 'mregex:ospf[0-9]* { area '
- name: L2 Neighbor Data
  description: 'For diagnosis function: L2 Neighbor Checking'
  enable: true
  inputs:
  - name: System Table Inputs[All Vendors]
    description: ''
    devices:
    - BJ_L2_test_1
    input_datas:
    - parser: ''
      cli_cmd:
      - show cdp neighbor
      system_table: NDP Table
      variable_mapping:
        Local Interface: Interface
        Interface Address: Neighbor Interface IP
        Interface Name: Neighbor Interface
        Device Name: Neighbor Device
      common_tables_defines:
      - index_variables:
        - Interface
        - Neighbor Interface
        table_variables:
        - Interface
        - Neighbor Interface IP
        - Neighbor Interface
        - Neighbor Device
        common_table_name: Common L2 Neighbor Table
    - parser: ''
      cli_cmd:
      - show mac table
      system_table: MAC Table
      variable_mapping:
        Port: Interface
        Mac Address: Neighbor Interface MAC
      common_tables_defines:
      - index_variables:
        - Neighbor Interface MAC
        - Interface
        table_variables:
        - Neighbor Interface MAC
        - Interface
        common_table_name: Common L2 Neighbor Table
    qualification: {}
- name: Interface Data
  description: 'For diagnosis function: L2/L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  inputs:
  - name: Interface Parser[Cisco]
    devices:
    - OSPFv3-R33
    input_datas:
    - parser: Shared Files in Tenant/Certification Tool Parsers/IP Interface [Cisco
        IOS]
      cli_cmds:
      - show ip interface
      system_table: ''
      variable_mapping:
        intf: Interface
        ip_addr: Interface IP
      common_tables_defines:
      - index_variables:
        - Interface
        table_variables:
        - Interface
        - Interface IP
        common_table_name: Common Interface Table
    - parser: Shared Files in Tenant/Certification Tool Parsers/Interface [Cisco IOS]
      cli_cmds:
      - show interface
      system_table: ''
      variable_mapping:
        intf: Interface
        mac_addr: Interface MAC
      common_tables_defines:
      - index_variables:
        - Interface
        table_variables:
        - Interface
        - Interface MAC
        common_table_name: Common Interface Table
    qualification:
      gdr:
        conditions:
        - expression: 'Cisco '
          operator: 4
          schema: subTypeName
        expression: A
      patterns: []
      regexes: []
diagnosis_functions:
  diagnosis_reports:
  - action: L3 Neighbor Checking
    description: Report Missing/Wrong L3 topology, Missing Devices..
    enable: true
  - action: L2 Neighbor Checking
    description: XXXXX
    enable: true
  - action: Multi-Vendor Collection
    description: XXXXX
    enable: true
  - action: Duplicate IP Checking
    description: XXXXXX
    enable: true
  diagnosis_fixings:
  - action: Duplicate IP Fixing
    enable: false
global_setting:
  white_ip_list: []
  enable_whilte_ip_list: true
  log_level: 3
  debug_options:
    build_common_table_from_inputs: true
    build_digital_twin: true
    run_diagnosis: true
    use_parser_cache_data: false
```
## 3. Diagnosis List
| Diagnosis Name | Diagnosis Target |
| --- | --- |
|L3 Neighbor / Missing Device Checking | 1. Detecting all L3 missing devices in customer legacy network. <br>2. Generating reports for further analysis. |
|L2 Neighbor Checking | 1. Detecting all L2 missing devices in customer legacy network. <br>2. Generating reports for further analysis. |
|Duplicate IP Checking | 1. Detecting all duplicate IPs in customer NetBrain processing domain after discovery all legacy devices. <br>2. Generating reports for further analysis. |
|Fix Duplicate IP | 1. By detect all existing duplicate IP interfaces. <br>2. Base on the data source in Digital Twin DB which generated rely on the diagnosis inputs customer provided. <br>  3. Set device name, interface name and interface IP as search key to find L3 Topo records and separate IPs into different groups per L3 Topo. <br> 4. Then assign the duplicate IPs into different zones per L3 Topo groups.|
|Multi-Vendor Collection| 1. Collecting customer vendor capacity. <br>2. Checking supported vendors per built in driver. <br>3. Generating reports for further analysis.|
|Fixing LAN Subnet Issue |   1. Base on data source from digital twin DB. <br> 2. Separate neighbor pair into groups. <br> 3. Filter out duplicate subnet. <br> 4. Compare the duplicate subnet and group interface information with the subnet and interface info in  Netbrain DB, then separate the subnet MP L3 topology. |
|To Be deleted device  | Delete following devices: <br> 1. Hostname changed devices. <br> 2. Rogue SNMP devices.  <br> 3. Single island devices. <br> 4. Build digital twin topology error devices. |
|Device/Interface GDR diagnosis| Ongoing|
|L2 Topology diagnosis| Ongoing|

## 4. Export Reports

### 4.1 IP Error Report
 
#### 4.1.1 Included columns
> **IP:** the IPs which will be considered as duplicate IPs. <br> **ErrorCode Message:** the massage to describe the corresponding error code.<br> **ErrorCode:** the error code which occurred by current IP.<br> **Source Device:** the device which current IP belongs to.<br> **CLI Command:** the CLI command which retrieve the current IP information.

#### 4.1.2 Report Sample

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

### 4.2 Device Error Report
 
#### 4.2.1 Included columns**
> **Device:** the device hostname of current device which facing errors. <br> **ErrorCode Message:** the massage to describe the corresponding error code. <br> **ErrorCode:** the error code which occurred by current IP. <br> **CLI Command:** the CLI command which retrieve the current IP information. <br> **In System:** the corresponding represent value in NetBrain system of current device. <br> **In Certification:** the corresponding represent value in platform certification process of current device.

#### 4.2.2 Report Sample

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

### 4.3 Interface Error Report
 
#### 4.3.1 Included columns
> **Device:** the device hostname of current device. <br> **Interface:** the interface name of current interface which facing errors. <br> **ErrorCode Message:** the massage to describe the corresponding error code. <br> **ErrorCode:** the error code which occurred by current IP. <br> **CLI Command:** the CLI command which retrieve the current IP information. <br> **In System:** the corresponding represent value in NetBrain system of current device. <br> **In Certification:** the corresponding represent value in platform certification process of current device.

#### 4.3.2 Report Sample

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

### 4.4 Enhanced Seed File（To be Discovered）
 
#### 4.4.1 Included columns
> **IP List:** IPs which can be considered as a network device IP from device data( e.g. Routing table ) but only can be found in Unknown IP List.

#### 4.4.2 Report Sample

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

### 4.5 To be deleted devices
 
#### 4.4.1 Included columns
> **Device List:** two or more devices configured same interface information with more than 80% and not set as HA devices.

### 4.6 Change Zone list
 
#### 4.6.1 Included columns
> **IP Subnet:** the IP subnet info which has been detected. <br> **Device:** the device hostname of current device which the IP subnet belongs to. <br> **Interface:** name of the interface which associate with current IP subnet. <br> **Interface IPMASK:** the IPMASK information of current interface. <br> **Zone Name:** name of the zone which the current IP subnet belongs to.

#### 4.6.2 Report Sample

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

## 5. NetBrain Library Generation From Diagnosis Inputs

Due to the Diagnosis Input structure we have defined now, it is very flexible and with a strong scalability. The purpose is we expect the original diagnosis input can be recursively extended by each engineer who has using it to diagnosis customer NetBrain system. Each customer would have unique legacy network conditions and the diagnosis inputs would be modified, enhanced and updated for accurately coincide with customer network phenomenon. With more and more different diagnosis inputs we can get from customer, after we merge all these inputs together, a general comprehensive almighty NetBrain Library would be grew up:

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

With the NetBrain Library enhanced, our engineers can much easier to find a corresponding diagnosis inputs template for new customer which means we can narrow down the involved Netbrain engineers numbers with new customer after we have enough inputs template in NetBrain Library. And also can reduce the meeting times with customer for collecting customer network info, trouble shooting unclassified diagnosis inputs and internal discussion. Which can speed up our Jumpstart program for new customer as we wished to involve Platform certification process into jumpstart program. 

## 6. Toolkit Operation Flow

### 6.1 Task and Framework

***Operator: Support/Solution/Platform Engineers***
Based on the results of many discussions, finally chose to use the plugins to manage the certification process, and execute them through the "Schedule Plugin Task".

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

### 6.2 Certification Input Definition

***Operator: Support/Solution/Platform Engineers***
The input format of the plugin is YAML format, which is used to define the necessary parameters and is used in the actual authentication process, detail design: InputDesign.

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

### 6.3 Generate Report

***Operator: Support/Solution/Platform Engineers***
Run this plugin and generate the certification report, and then engineers will solve the different issues separately.

<img src="REST APIs Documentation/Device Access Control/DeviceAccessImage.JPG" /><br>

### 6.4 Fix the Issues and Re-Run certification
#### 6.4.1 Fix the Issues
>After getting the certification report, the Support/Solution/Platform Engineer who received the report can directly communicate with the customer to solve the problem. <br> Support/Solution Engineers can solve the live setting issues directly, Missing devices issues need to communicate with the customer. <br> Platform Engineer can also solve the live setting issues directly, the driver/topology/path issues we will fix them via Knowledge Cloud

#### 6.4.2 Re-Run Benchmark
>After solving all the issues, Support/Solution/Platform Engineers need to re-run the Discover and benchmark. <br> Re-Run the discover to add the missing devices into the domain. <br> Re-run the benchmark to add the missing topology

#### 6.4.3 Re-Run Certification
>After the new discovery/benchmark finished, need to re-run the certification and check the new possible issues. <br> If the issues have been solved, we can deliver to the service engineer for the next step. <br> if there are new issues, need to loop the whole process

## 7. Route Map



```python

```
