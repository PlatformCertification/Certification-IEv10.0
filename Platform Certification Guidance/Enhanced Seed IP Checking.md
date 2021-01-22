## Enhanced Seed IP Checking

### 1.Certification Input
#### 1.1 Input for ARP Table
```yaml
system_table: ARP Table
variable_mapping:
    Interface: Interface
    IP Address: Neighbor Interface IP
    MAC Address: Neighbor Interface MAC
- index_variables:
    - Interface
    - Neighbor Interface IP
```

#### 1.2 Input for Route Table
```yaml
system_table: Route Table
variable_mapping:
  OutIf: Interface
  NextHop: Neighbor Interface IP
- index_variables:
  - Neighbor Interface IP
  - Interface
```

#### 1.3 Input from Parser
```yaml
name: 'OSPF Neighbor Parser[Cisco]'
input_datas:
  - parser: 
      Shared Files in Tenant/Certification Tool Parsers/OSPF Neighbors Detail [Cisco IOS]
    variable_mapping:
      intf: Interface
      intf_addr: Neighbor Interface IP
      area_id: Area ID
    - index_variables:
      - Interface
      - Neighbor Interface IP
```
#### 1.4 Input for NDP Table
```yaml
system_table: NDP Table
variable_mapping:
    Local Interface: Interface
    Interface Address: Neighbor Interface IP
    Interface Name: Neighbor Interface
    Device Name: Neighbor Device
- index_variables:
    - Interface
    - Neighbor Interface
```

#### 1.5 Input for MAC Table
```yaml
system_table: MAC Table
variable_mapping:
  Port Name: Interface
- index_variables:
  - Interface
```

#### 1.6 Device Qualification
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

![BuildDigitalTwin](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/Certification-Enhanced%20Seed%20IP%20Checking.png)
***Note:*** From the **Digital Twin L2 Topology Table**, for device R1 interface E2, the neighbor interface IP is 3.3.3.3 as shown in the image. Although from the NDP table we can find the corresponding neighbor deivce is R4, but before we build the Digital Twin DB, the back end script will query each IP we have got from common table by internal API to detect whether there is a device object can be returned base on current IP. If there is no device object can be get then the current IP would be considered as a missing IP and inserted into the final enhanced IP report. And the corresponding neighbor device infomration(Neighbor Device, Neighbor Interface) also will be removed from Digital Twin Table.

#### 2.2 Diagnosis Checking Logic

![CheckingLogic](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/Enhanced%20Seed%20IP%20Checking.png)
