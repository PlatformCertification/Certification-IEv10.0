## Certification Input Example with Yaml

```Yaml
---
dianosis_inputs:
- name: L3 Neighbor Data #'For diagnosis function: L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  inputs:
  - name: L3 Neighbor Data # Name of current data input.
    input_datas:
    - parser: ""
      system_table: ARP Table
      variable_mapping:
        Interface: Interface
        IP Address: Neighbor Interface IP
        MAC Address: Neighbor Interface MAC
      index_variables:
      - Interface
      - Neighbor Interface IP
      extend_common_variables:
    - parser: ""
      system_table: Route Table
      variable_mapping:
        OutIf: Interface
        NextHop: Neighbor Interface IP
      index_variables:
      - Interface
      - Neighbor Interface IP
      extend_common_variables:  
      
    - parser: "Shared Files in Tenant/Certification Tool Parsers/OSPF Neighbors Detail [Cisco IOS]"
      variable_mapping:
        intf: Interface
        intf_addr: Neighbor Interface IP
        area_id: Area ID
      index_variables:
      - Interface
      - Neighbor Interface IP
      extend_common_variables:
      
    qualification:
      gdr:
        conditions:
        - value: 'Cisco Router'
          operator: 4
          schema: subTypeName
        expression: A
      patterns:
      
      regexes:
      - "regex:router ospf [0-9]+"
      
- name: L2 Neighbor Data #'For diagnosis function: L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  inputs:
  - name: L2 Neighbor Data # Name of current data input.
    input_datas:
    - parser: ""
      system_table: NDP Table
      variable_mapping:
        Local Interface: Interface
        Interface Address: Neighbor Interface IP
        Interface Name: Neighbor Interface
        Device Name: Neighbor Device
      index_variables:
      - Interface
      - Neighbor Interface
      extend_common_variables:
      
    - parser: ""
      system_table: MAC Table
      variable_mapping:
        Port Name: Interface
        Mac Address: Neighbor Interface MAC
      index_variables:
      - Interface
      - Neighbor Interface MAC
      extend_common_variables:  
      
    qualification:
    
- name: Interface Data #'For diagnosis function: L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  inputs:
  - name: Interface Parser[Cisco] # Name of current data input.
    input_datas:
    - parser: "Shared Files in Tenant/Certification Tool Parsers/IP Interface [Cisco IOS]"
      system_table: 
      variable_mapping:
        intf: Interface
        ip_addr: Interface IP
      index_variables:
      - Interface
      extend_common_variables:
      
    - parser: "Shared Files in Tenant/Certification Tool Parsers/Interface [Cisco IOS]"
      system_table: 
      variable_mapping:
        intf: Interface
        mac_addr: Interface MAC
      index_variables:
      - Interface
      extend_common_variables:  
      
    qualification:
      gdr:
        conditions:
        - value: 'Cisco'
          operator: 4
          schema: subTypeName
        expression: A
      patterns:
      
      regexes:
      
  
diagnosis_functions:
  - L3 Neighbor Checking # Report Missing/Wrong L3 topology, Missing Devices..
  - L2 Neighbor Checking # Report Missing/Wrong L2 topology, Missing Devices..
  - Duplicate IP Checking
  - Multi-Vendor Collection
  #- Duplicate IP Fixing
global_setting:
  white_ip_list: []
  enable_whilte_ip_list: true
  debug_options:
    log_level: 0
    build_common_table_from_inputs: true
    build_digital_twin: true
    run_diagnosis: true
    use_parser_cache_data: false
```
