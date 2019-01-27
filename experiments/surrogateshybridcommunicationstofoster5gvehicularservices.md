<!-- TITLE: SURROGATES -->
<!-- SUBTITLE:  Hybrid Communications to Foster 5G Vehicular Services -->

# SURROGATES - Hybrid Communications to Foster 5G Vehicular Services
![Surr](/uploads/surrogates/surr.png "Surr")
**Organization**
University of Murcia - http://www.um.es
## Experiment description
In vehicular scenarios, on-board units (OBU) have evolved from specific purpose units designed for telematic services such as fleet management or road tolling, to generic networked nodes capable of interconnecting other in-vehicle devices, acting as mobile routers. Although virtualization of network and computing nodes is a reality in cloud deployments, it is expanding to the edge of the access network in scenarios involving multi-access edge computing. This scenario presents a good frame to offload data analytics tasks from OBUs, which should focus on actions of higher priority such as maintaining vehicle connectivity, managing communication flows or applying security measures to data traffic.

SURROGATES aims at virtualizing regular OBU tasks requiring a high computing load, on the basis of a hybrid communication system that allows a proactive connection between the real OBU and a virtual one. Over this channel, all sensor data collected from the vehicles are reported. The virtual OBU provides pre-processed information to be used by cloud services in the area of mobility and pollution, which will be accessible as a telematic service by final users.

In the multi-homed scenario considered, the OBU selects the most convenient interface at the same time seamless handovers are performed using Proxy Mobile IP (PMIP) with IPv6 support. An OBU manager module has been defined to be the initial contact point from physical OBUs wanting to connect to its virtual counterpart. As can be seen, data processing functions are delegated into the cloud-edge. Processed or cached information are accessed by vehicular services requiring a global view of the road. This solves the issue of accessing the physical OBU from multiple services and requiring monitoring data when the OBU is temporally offline.

## Results
With the aim of both validating the SURROGATES platform and assess its performance, the solution has been tested under real driving conditions. This has been done, as said above, using the vehicular testbed of IT-Av after testing in laboratory the good operation of all modules. The vehicle OBU, provided with the monitoring software to access an OBD-II interface and report the data collected, was in charge of registering with its virtual counterpart (vOBU) and then continuously send data to it.


A Grafana system allows end users to check the past and current status of the vehicles. Additionally, the OBU/vOBU was periodically asked about particular parameters using the Android app, in order to measure the performance of the network in terms of request losses and resolution delay. The next figure shows the results obtained in one of the test rounds performed, including plots for the speed, RPM, engine temperature and intake pressure.

The RTT results obtained after a test involving six rounds at the IT-Av premises are included in the next figure. This time is measured from the service point of view. Here it can be seen clearly the speed up of the SURROGATES proposal when the requests are processed locally by the vOBU. The extra time needed in the wrong case of OBU access failure is due to the TCP timeouts involved in the process.


In general, it can be said that the whole platform has been validated and the performance results indicate speed ups from 80 ms required in a regular (successful) OBU access to 2 ms when using the NFV-powered vOBU.

## Conclusions
SURROGATES presents advantages in the area of high-performance data processing from OBUs. The solution has been successfully deployed within the 5GINFIRE ecosystem, using the IT-Av and 5TONIC domains to onboard the different modules, at the same time the base vehicular communication system provided by IT-Av is used to maintain vehicle connectivity. The test performed under real driving conditions have served to validate the solution, successfully checking the correct operation of SURROGATES, and measuring the performance of the system in terms of the delay observed to access OBU and the availability of vehicle data considering the challenging scenario of vehicular networks, which unusually suffer from disconnection periods and/or low throughput connections. The results show that an improvement of several or orders of magnitude (from 80 ms to 2 ms) can be obtained if it is not necessary to ask the physical OBU for a data that can be given by the vOBU. Further improvements could be achieved it higher processing loads would be moved from the OBU to its virtual counterpart. Hence, SURROGATES presents interesting results subject to further research in the area of vehicular edge computing and 5G.
