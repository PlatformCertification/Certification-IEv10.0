## Certification Input Example with Yaml

```Yaml
---
dianosis_inputs:
- name: L3 Neighbor Data #'For diagnosis function: L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  inputs:
  - name: System Table Inputs[All Vendors] # Using parser or system table: Route Table, MAC Table, ARP Table, CDP Table, NCT Table
    input_datas:
    - parser: "Shared Files in Tenant/Certification Tool Parsers/OSPF Neighbors Detail [Cisco IOS]"
      system_table: ARP Table
      variable_mapping:
        Interface: Interface
        IP Address: Neighbor Interface IP
        MAC Address: Neighbor Interface MAC
        Area ID: Interface Area ID
      index_variables:
      - Interface
      - Interface IP
      extend_common_variables:
      - Interface Area ID
    qualification:
      gdr:
        conditions:
        - expression: 'Cisco'
          operator: 4
          schema: subTypeName
        expression: A
      patterns:
      - "interface $str:intfName1"
      - "ip address $ip:ip1 $ip:mask1"
      regexes:
      - "regex:router ospf [0-9]+"
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
    log_level: 3
    build_common_table_from_inputs: true
    build_digital_twin: true
    run_diagnosis: true
    use_parser_cache_data: false
```
