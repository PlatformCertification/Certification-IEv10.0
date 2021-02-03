## Certification Inputs Example with Yaml

### Certification Plugin Sample in IE
![image](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/Certification%20Plugin%20Sample%20in%20IE.png)

### Inputs Yaml Sample

```Yaml
---
certificate_methods:
  - nb_cert_method_system_table
  - nb_cert_method_cisco_ios
  - nb_cert_method_cisco_ios_xr
  - nb_cert_method_cisco_nxos
  - nb_cert_method_f5_load_balancer
  - nb_cert_method_junos
  - nb_cert_method_checkpoint
  #- nb_cert_method_arista_switch
  #- nb_cert_method_alu_router
  #- nb_cert_method_wlc
  #- nb_cert_method_fortinet_firewall
  #- nb_cert_method_palo_alto_firewall
  #- nb_cert_method_asa
  - my_cert_method_cisco_ios # copy from nb_cert_cisco_ios
  - my_cert_method_1 # write the new, include nxos, xr
  - my_cert_method_2 # mixed input
diagnosis_precheck:
  - dx_precheck_qualification_coverage
diagnosis_checking:
  - dx_checking_enhanced_seed_ip
  - dx_checking_l3_neighbor
  - dx_checking_l2_neighbor
  - dx_checking_duplicate_ip
  - dx_checking_duplicate_subnet
dignosis_fixing:
  - dx_fixing_duplicate_ip
  - dx_fixing_duplicate_subnet
data_collection: data_collection
white_ip_list: white_ip_list
run_mode: 1 # 0:only pre-check,1:checking, 2:fixing, 3: collect data
device_scope:
  scope_option: 0 #  0 All device, 1 Device Group, 2 Site, 3 Device Name.
  scope_names:
    #- site_name
debug_options:
  log_level: 0
  build_common_table_from_inputs: true
  build_digital_twin: true
  run_diagnosis: true
  use_parser_cache_data: false
```

### White IP List Python Sample

**white_ip_list.py**
```python 
white_ip_list = """
    127.1.1.1
    127.1.1.2, IP from Internet"""
```

### Diagnosis Inputs Samples

**nb_cert_cisco_ios.py**
```python
cert_input = '''
- name: L3 Neighbor Data # 'For diagnosis function: L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  common_table_name: Common L3 Neighbor Table
  inputs:
  - name: OSPF Neighbor Parser[Cisco]
    input_datas:
    - parser: Built-in Files/Certification Tool/Cisco IOS/OSPF Neighbors Detail[Cisco IOS]
      variable_mapping:
        $intf: Intf
        $intf_addr: NbrIntfIP
        $area_id: AreaID
      index_variables:
      - Intf
      - NbrIntfIP
      cli_cmds:
      - show ip ospf neighbor detail
    qualification:
      gdr:
        conditions:
        - value: 'Cisco '
          operator: 4
          schema: subTypeName
        expression: A
      patterns: []
      regexes:
      - regex:router ospf [0-9]+
- name: Interface Data # 'For diagnosis function: L2/L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  common_table_name: Common Interface Table
  inputs:
  - name: Interface Parser[Cisco]
    input_datas:
    - parser: Built-in Files/Certification Tool/Cisco IOS/IP Interface [CiscoIOS]
      variable_mapping:
        $intf: Intf
        $ip_addr: IntfIP
      index_variables:
      - Intf
      cli_cmds:
      - show ip interface
    - parser: Built-in Files/Certification Tool/Cisco IOS/Interface [Cisco IOS]
      variable_mapping:
        $intf: Intf
        $mac_addr: IntfMac
      index_variables:
      - Intf
      cli_cmds:
      - show interface
    qualification:
      gdr:
        conditions:
        - expression: 'Cisco '
          operator: 4
          schema: subTypeName
        expression: A
      patterns: []
      regexes: []
'''
```

**nb_cert_system_table.py**
```python
cert_input = '''
- name: L3 Neighbor Data # 'For diagnosis function: L3 Neighbor Checking, Duplicate IP Fixing'
  enable: true
  common_table_name: Common L3 Neighbor Table
  inputs:
  - name: System Table Inputs[All Vendors]
    input_datas:
    - system_table: ARP Table
      variable_mapping:
        Interface: Intf
        IP Address: NbrIntfIP
        MAC Address: NbrIntfMAC
      index_variables:
      - Intf
      - NbrIntfIP
    - system_table: Route Table
      variable_mapping:
        OutIf: Intf
        NextHop: NbrIntfIP
      index_variables:
      - NbrIntfIP
      - Intf
- name: L2 Neighbor Data # 'For diagnosis function: L2 Neighbor Checking'
  enable: true
  common_table_name: Common L2 Neighbor Table
  inputs:
  - name: System Table Inputs[All Vendors]
    description: ''
    input_datas:
    - system_table: NDP Table
      variable_mapping:
        Local Interface: Intf
        Interface Address: NbrIntfIP
        Interface Name: NbrIntf
        Device Name: NbrDev
      index_variables:
      - Intf
      - NbrIntf
      cli_cmd:
      - show cdp neighbor
    - system_table: MAC Table
      variable_mapping:
        Port Name: Intf
      index_variables:
      - Intf
'''
```