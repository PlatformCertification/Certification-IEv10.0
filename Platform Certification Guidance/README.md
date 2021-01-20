
# Platform Certification Guidance

## 1. Overall Flow

![OverallFlow](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/Overall%20flow.png)
    
## 2. Input

### 2.1 Certification Significant Input Blocks Introduction

#### 2.1.1. Diagnosis Inputs Block
> **diagnosis_inputs**<br>
>Customer needs to insert all detail information for each certification which will be included in current plugin. Certification name, enable flag and all detail inputs must be inserted.

> **certification_inputs.inputs**<br>
>As the most important section of certification_inputs, customer must review all attributes which belongs current component in below table. Customer need to take more care of the "qualification" section, we provide three kinds of qualification methods totally:

>>1. gdr_qulification
>>2. patterns
>>3. regexes

>If multiple qualification methods included, customer need to provide the boolean_expression in method level accurately to represent the relationship between each qualification method. Similar with point c, if customer provide multiple conditions in gdr_qulification, the boolean_expression in gdr_qulification level also need to be inserted accurately.

#### 2.1.2. Diagnosis Function Block
> **diagnosis_functions.diagnosis_reports.**<br>
> Customer need to pre-define all diagnosis reports at this section which need to be generated after plugin running successfully. For each diagnosis report, customer need to provide the corresponding report name and enable flag as inputs, please check Detail Introduction for more information.

> **diagnosis_functions.diagnosis_fixings**<br>
>Customer need to pre-define desired fixing processes at this section which need to be triggered automatically to fix platform related issues after plugin running successfully. For each fixing actions, customer need to provide the corresponding action name and enable flag as inputs, please check Detail Introduction for more information.

#### 2.1.3. Global Settings Block
> **global_settings**<br>
>Customer need to insert all corresponding values for each attribute in this section. Please check Detail Introduction for more information.

### [2.2 Certification Input Attributes Detail Introduction](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/Certification%20Input%20Attributes%20Detail.md)
***Click on the title for detail information.***
    
### [2.3 Certification Input Example with Yaml](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/Certification%20Input%20Example%20with%20Yaml.md)
***Click on the title for detail information.***

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

![IPreport](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/image011.jpg)

### 4.2 Device Error Report
 
#### 4.2.1 Included columns**
> **Device:** the device hostname of current device which facing errors. <br> **ErrorCode Message:** the massage to describe the corresponding error code. <br> **ErrorCode:** the error code which occurred by current IP. <br> **CLI Command:** the CLI command which retrieve the current IP information. <br> **In System:** the corresponding represent value in NetBrain system of current device. <br> **In Certification:** the corresponding represent value in platform certification process of current device.

#### 4.2.2 Report Sample

![Devicereport](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/image012.jpg)

### 4.3 Interface Error Report
 
#### 4.3.1 Included columns
> **Device:** the device hostname of current device. <br> **Interface:** the interface name of current interface which facing errors. <br> **ErrorCode Message:** the massage to describe the corresponding error code. <br> **ErrorCode:** the error code which occurred by current IP. <br> **CLI Command:** the CLI command which retrieve the current IP information. <br> **In System:** the corresponding represent value in NetBrain system of current device. <br> **In Certification:** the corresponding represent value in platform certification process of current device.

#### 4.3.2 Report Sample

![InterfacePreport](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/image013.jpg)

### 4.4 Enhanced Seed File（To be Discovered）
 
#### 4.4.1 Included columns
> **IP List:** IPs which can be considered as a network device IP from device data( e.g. Routing table ) but only can be found in Unknown IP List.

#### 4.4.2 Report Sample

![SeedPreport](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/enhanced%20seed%20file.png)

### 4.5 Change Zone list
 
#### 4.5.1 Included columns
> **IP Subnet:** the IP subnet info which has been detected. <br> **Device:** the device hostname of current device which the IP subnet belongs to. <br> **Interface:** name of the interface which associate with current IP subnet. <br> **Interface IPMASK:** the IPMASK information of current interface. <br> **Zone Name:** name of the zone which the current IP subnet belongs to.

#### 4.5.2 Report Sample

![ZonePreport](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/image014.jpg)

### 4.6 To be deleted devices
 
#### 4.6.1 Included columns
> **Device List:** two or more devices configured same interface information with more than 80% and not set as HA devices.


## 5. NetBrain Library Generation From Diagnosis Inputs

Due to the Diagnosis Input structure we have defined now, it is very flexible and with a strong scalability. The purpose is we expect the original diagnosis input can be recursively extended by each engineer who has using it to diagnosis customer NetBrain system. Each customer would have unique legacy network conditions and the diagnosis inputs would be modified, enhanced and updated for accurately coincide with customer network phenomenon. With more and more different diagnosis inputs we can get from customer, after we merge all these inputs together, a general comprehensive almighty NetBrain Library would be grew up:

![NetBrainLibrary](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/NetBrain%20Library%20(1).png)

With the NetBrain Library enhanced, our engineers can much easier to find a corresponding diagnosis inputs template for new customer which means we can narrow down the involved Netbrain engineers numbers with new customer after we have enough inputs template in NetBrain Library. And also can reduce the meeting times with customer for collecting customer network info, trouble shooting unclassified diagnosis inputs and internal discussion. Which can speed up our Jumpstart program for new customer as we wished to involve Platform certification process into jumpstart program. 

## 6. Toolkit Operation Flow

### 6.1 Task and Framework

***Operator: Support/Solution/Platform Engineers***
Based on the results of many discussions, finally chose to use the plugins to manage the certification process, and execute them through the "Schedule Plugin Task".

![ScheduleTask](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/schedule%20plugin%20task.png)

### 6.2 Certification Input Definition

***Operator: Support/Solution/Platform Engineers***
The input format of the plugin is YAML format, which is used to define the necessary parameters and is used in the actual authentication process, detail design: InputDesign.

![certificationDefine](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/inputs%20design.png)

### 6.3 Generate Report

***Operator: Support/Solution/Platform Engineers***
Run this plugin and generate the certification report, and then engineers will solve the different issues separately.

![report](https://github.com/PlatformCertification/Certification-IEv10.0/blob/main/Platform%20Certification%20Guidance/images/certification%20report.png)

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
