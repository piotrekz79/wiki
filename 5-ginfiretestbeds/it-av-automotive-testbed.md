<!-- TITLE: IT-Av Automotive Environment -->
<!-- SUBTITLE: A quick summary of IT-Av Automotive Environment -->

# Testbed Introduction

![Vanet](/uploads/automotive/vanet.jpg "Vanet"){.align-center}

## Architecture

![It Av Testbed V 2](/uploads/automotive/it-av-testbed-v-2.png "It Av Testbed V 2"){.align-center}
## 

![Obu](/uploads/automotive/obu.png "Obu"){.align-center}

## 5GinFIRE and IT-Av Testbed Datacenter

VIM: based on OpenStack Ocata.
NFVI:
1x server computer: 24 cores, 192GB memory, 4 x 1Gbps interfaces (passthrough, DPDK and SR-IOV), 2 x 1TB SAS3 hard drives. 
1x server computer: 16 cores, 256 GB memory, 4 x 1Gbps interfaces (passthrough), 2 x 1TB SAS2 hard drives. 
1x 24-port 1Gbps switch, interconnecting the infrastructure.


# Use Case: Assisted Driving with Video Transcoder
To demonstrate the potential of the 5GinFIRE automotive testbed located in IT-Aveiro, and to validate the workflow for new experimenters to deploy new VNFs, a VNF video transcoding camera-based car overtaking scenario was evaluated. In this scenario, illustrated in the Figure X, each vehicle contains an OBU that provides the communication between vehicles and between each vehicle and the infrastructure. The OBU is also connected to an Android device, which can be a smartphone or a tablet, through WiFi, providing visual information for the driver. The vehicle contains a video camera on its front side. This information will be used by the driver to take decisions on driving, more specifically in overtaking situations. Regarding to the communication interfaces, each OBU is able to communicate with the infrastructure (RSUs) using the IEEE 802.11p/WAVE or IEEE 802.11g/WiFi, or using the 4G LTE cellular technology (C-RAN). The VNF video transcoding was available on site and deployed at the edge of the infrastructure. 

![Cars 5 Ginfire](/uploads/automotive/cars-5-ginfire.png "Cars 5 Ginfire"){.align-center} 
Figure X - 5GinFIRE assisted driving use case

During the use case validation we were able to stream a live video from the front vehicle to the RSU through IEEE 802.11p/WAVE, being transcoded by the VNF video transcoding located at the edge of the infrastructure, and then being transmitted again to the rear vehicle using the same communication technology. Another version of this use case, still waiting for validation, aims to cope with situations where the vehicles are not in range of RSUs, and the video is transmitted through 4G to the C-RAN at the edge of the infrastructure, where the VNF video transcoding is located. For this scenario to be evaluated, another VNF needs to be deployed and integrated with OSM for automatic deployment, which is the Unifier Gateway (UGW).

# Experimentation
Experimenters will have access to real OBUs, RSUs, In-Car Node Processors, ESP8266 devices and video cameras, having also the possibility to create and deploy their own VNFs from the 5GinFire portal within the IT-Av automotive testbed. Initially experimenters will have access to a controlled environment in the lab, with the possibility to evaluate and validate their own automotive VNFs services in terms of V2X communication performance and metrics (e.g., latency vs overhead, throughput vs packet loss, etc.), and test their own automotive VNFs within the car with its diversity of contextual-aware information gathered from extra sensors (traffic signals) and from OBUs internal sensors available (accelerometers, heading, speed, link quality connection, GPS, compass, RSSI, car neighbor’s density, etc.). In a later stage experiments will be performed through real experimentations in a controlled and outside environment.

Possible VNFs to be included and tested comprise Li-Fi communication between cars, car crash detection and emergency info dissemination, On-Board Diagnosis for self-repairing, collision avoidance (with machine learning techniques) and others.
# Contact
Susana Sargento (susana@ua.pt) and Miguel Luís (nmal@av.it.pt)
Instituto de Telecomunicações, Aveiro, Portugal (IT-Av)
Campus Universitário de Santiago, 3810-193 AVEIRO – PORTUGAL