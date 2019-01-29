<!-- TITLE: Exploring SURROGATES VNFs -->

# Introduction
In the SURROGATES experiment the ITAv OBU capabilities regarding network mobility are exploited to offer 11p/4G hybrid communications as a base enabler to offload processing tasks from the same unit. This is carried out by virtualizing OBU instances at the edge of the 5GINFIRE cloud. A base monitoring system considering sensor data from the vehicle sends raw information to an OBU virtual instance. Here, pre-processing, aggregation and pattern recognition tasks can be carried out. Processed information is then available for global Cooperative Intelligent Transportation Systems (C-ITS) services.

The idea is to offload data analytics tasks from OBUs, which should focus on actions of higher priority such as maintaining vehicle connectivity, managing communication flows or applying security measures to data traffic. As can be seen in Figure 1, the approach chosen in SURROGATES is to create virtualized images of OBUs near the edge of the network, where raw data sent from in-vehicle sensors is processed. Hence, a monitoring middleware is considered for the OBU to gather continuously raw data that are sent to the data processing functions delegated into the cloud-edge. Data analytics tasks envisaged include pre-processing, aggregation and pattern recognition. Processed or cached information are accessed by vehicular services requiring a global view of the road. An OBU manager module has been defined to be the initial contact point from physical OBUs wanting to connect to its virtual counterpart. This manager is also an NFV module, and communicates with OSM to indicate the need for a virtual OBU instance. OSM is in charge of creating and managing these instances, which could be potentially instantiated on demand. Data to be collected from the OBUs consider navigation information, diagnosis and mechanical monitoring details of the car, and readings from other sensors connected to the OBU.

![Surr Architecture](/uploads/surrogates/surr-architecture.png "Surr Architecture")
Figure 1 - Architecture of SURROGATES.

## Information collected through OBD-II

The information collected through OBD-II from in-vehicles sensors is highly dependent on the brand an model of each vehicle. However, it is expected that most of the information listed below will be available for diagnosis and mechanical monitoring:
* TIMESTAMP,seconds	
* STATUS_MIL,boolean	
* STATUS_DTC_COUNT,integer	
* STATUS_IGNITION_TYPE,string	
* ENGINE_LOAD,percent	
* COOLANT_TEMP,degC	
* INTAKE_PRESSURE,kilopascal	
* RPM,revolutions_per_minute	
* SPEED,kph	
* TIMING_ADVANCE,degree	
* INTAKE_TEMP,degC	
* MAF,gps	
* THROTTLE_POS,percent	
* DISTANCE_W_MIL,kilometer

# Running the Experiment
## Connection
This experiment requires the use of 3 VNFs, two of them deployed in ITAv, the vOBU and the vOBU manager, and one deployed in 5TONIC, the data analytics VNF. After requesting the deployment of the related NSD, one should access the VNFs through the jump machine provided by the 5GinFIRE network management, along with the VPN credentials.
## Setup
### vOBU

### OBU manager
The source code is located at /home/debian/surrogates-manager/
The read-only key to access the repository is present in /home/debian/.ssh/id_rsa
The repository has already a README.md
#### Configuration
The configuration is already prepared for listening in any address. The only change needed is in manager.conf the *listening port from 8070 to 8071* because there is a nginx proxy in front of the python to provide IPv6 support as well as queuing mechanisms. Therefore, the *nginx is the one that holds the IP addresses*.
In /etc/nginx/sites-available/manager the IPv4 and IPv6 addresses for the instantiated VNF need to be updated in the *server_name param*. The listening port is set in the image already to 8071.
#### Executing
The manager has a systemd script that is in charge of launching the service: *systemctl restart manager*
The logs are present at /home/debian/surrogates-manager/output.log but some output might also go to /var/log/syslog (such as exceptions backtraces).
The nginx is managed as usual with systemd as well: *systemctl restart nginx*

### Data analytics

### OBU

