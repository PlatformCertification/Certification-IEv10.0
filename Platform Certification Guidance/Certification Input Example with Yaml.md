## Certification Inputs Example with Yaml

### Certification Plugin Sample in IE
![image](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/Certification%20Plugin%20Sample%20in%20IE.png)

### Inputs Yaml Sample

```Yaml
---
diagnosis_methods:
  - nb_dm_system_table
  - nb_dm_alcatel_lucent_service_router
  - nb_dm_alcatel_omniswitch_os
  - nb_dm_arista
  - nb_dm_aruba
  - nb_dm_brocade_switch
  - nb_dm_checkpoint
  - nb_dm_cisco_asa
  - nb_dm_cisco_catalyst
  - nb_dm_cisco_firepower_ngfw
  - nb_dm_cisco_firepower_ngfw_ftd
  - nb_dm_cisco_ios
  - nb_dm_cisco_ios_xr
  - nb_dm_cisco_nxos
  - nb_dm_cisco_wlc
  - nb_dm_f5_load_balancer
  - nb_dm_fortinet_fortigate_firewall
  - nb_dm_hp_comware_swicth
  - nb_dm_hp_procurve
  - nb_dm_juniper_srx_firewall
  - nb_dm_junos
  - nb_dm_palo_alto_panorama
  - nb_dm_palo_alto
  - nb_dm_riverbed_wan_optimizer
  - nb_dm_silverpeak_wan_optimizer
  - nb_dm_ubiquiti
  #- my_dm_cisco_ios # copy from nb_cert_cisco_ios
  #- my_dm_1 # write the new, include nxos, xr
  #- my_dm_2 # mixed input
run_folder: reports
run_setting:
  qualification:
    enable: true
    names:
      - cert_qualification
  benchmark:
    enable: false
    names:
      - cert_benchmark_data
  diagnosis_checking:
    enable: false
    names:
      - dx_checking_enhanced_seed_ip
      - dx_checking_l3_neighbor
      - dx_checking_l2_neighbor
      - dx_checking_device_integrity
      #- dx_checking_device_datas
      - dx_checking_duplicate_ip
      - dx_checking_duplicate_subnet
  diagnosis_fixing:
    enable: false
    names:
      - dx_fixing_duplicate_ip
      - dx_fixing_duplicate_subnet
      - dx_fixing_gdr
      - dx_fixing_topo
  diagnosis_undo:
    enable: false
    names:
      - dx_undo_duplicate_ip
      - dx_undo_duplicate_subnet
      - dx_undo_fixing_gdr
      - dx_undo_fixing_topo
  data_collection:
    enable: false
    names:
      - cert_data_collection
white_ip_list: white_ip_list
data_collection: data_collection
white_mac_list: white_mac_list
white_interface_list: white_interface_list
device_scope:
  scope_option: 0 #  0 All device, 1 Device Group, 2 Site Path Name, 3 Device Name.
  scope_names:
    #- device_group1
cert_db_reset: false
debug_options:
  log_level: 1
  build_common_table_from_inputs: true
  build_digital_twin: true
  run_diagnosis: true
  use_baseline: true # default is true, get paeser cli from cert benchmark baseline
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