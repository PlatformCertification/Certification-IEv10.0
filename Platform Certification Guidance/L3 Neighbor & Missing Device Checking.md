## L3 Neighbor / Missing Device Checking

### 1.Certification Input
#### 1.1 Input for ARP Table
```yaml
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
```

#### 1.2 Input for Route Table
```yaml
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
```

#### 1.3 Input from Parser
```yaml
name: 'OSPF Neighbor Parser[Cisco]'
input_datas:
  - parser: >-
      Shared Files in Tenant/Certification Tool Parsers/OSPF Neighbors Detail [Cisco IOS]
    cli_cmds:
      - show ip ospf neighbor detail
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
```

#### 1.4 Input for Qualification Setting
```yaml
qualification:
  gdr:
    conditions:
      - expression: Cisco Router
        operator: 4
        schema: subTypeName
    expression: A
  patterns: []
  regexes:
    - 'regex:router ospf [0-9]+'
```

### 2. Certification Logic

#### 2.1 Build Common Table and Digital Twin Table

![BuildDigitalTwin](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/L3%20Neighbor%20-%20Build%20Degitial%20Twin.png)

#### 2.2 Diagnosis Checking Logic

![CheckingLogic](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/Certification-Diagnosis%20Logic%20Checking.png)

### 3. Important
1. OSPF neighbors across devices are not considered
2. If the neighbor device and neighbor interface cannot be found in the digital twin table, then it is not considered
