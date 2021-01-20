## Certification Input Example with Yaml

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