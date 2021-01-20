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