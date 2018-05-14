<!-- TITLE: Bristol Smart City -->
<!-- SUBTITLE: A quick summary of Bristol Smart City -->

# Smart Internet Lab, University of Bristol
## Testbed introduction
This test network enables network slicing as a service, as required by various stakeholders as the Network Operation use case. Using 5G network concepts we deliver several services based on different network slices operating concurrently. In one slice, we deliver services for the Enhanced Mobile Broadband use case; while in another network slice, we deliver high and/or low throughputs, demanding Ultra Low Latency Reliable Services as in the Critical Communications use case. Also, several virtual networks can be grouped for different business demands and serve many devices forming the Massive Internet of Things use case.

The University of Bristol’s Smart Internet Lab 5G Testbed comprises multiple levels of research ready SDN switches connecting diverse layers of access technologies, to high performance cloud compute resources via an innovate exchange and orchestration mechanism. The focus for this test network is to enable experimentation in network service virtualisation and innovative network function testing with access agnostic connectivity to end users.

Permanently installed in Millennium Square and the Smart Internet Lab are five heterogeneous, 5G ready wireless access technologies connected via dedicated, high capacity optical fibres, Edgecore and Corsa SDN switches and mmWave radio. A dedicated out of band management network provides flexibility of configuration and control of all active devices in the network. Control of network architecture is made available to NetOS, an intelligent SDN controller.

The cloud infrastructure at the Smart Internet Lab is built on OpenStack with a virtualised Evolved Packet Core (EPC) from Nokia. This allows virtual network functions to be deployed as a mobile edge computing service close to the edge of the network providing performance enhancements to the user.

Connectivity to additional 5G testbeds is provided through the 5G UK Exchange, a novel architecture for orchestration of virtual network functions and SDN configuration. This exchange resides in a neutral datacentre with 10Gbit connectivity through JANET to connected partners. The purpose of the 5G UK Exchange allows researchers to dynamically provision both virtual and physical network functions in each testbed from a catalogue of available services. This will allow end-to-end 5G research to take place across the globe.

## 	University of Bristol, Smart Internet Lab’s 5G Test Network Capability
The University of Bristol testbed showcases and facilitates research on the following technology capabilities.
•	Multi-vendor SDN enabled packet switched network
	o	Corsa switch (Corsa DP2100)
	o	Edgecore switch (Edgecore AS4610 series) 
•	SDN enabled optical (Fibre) switched network
	o	Polatis Series 6000 Optical Circuit Switch
•	Multi-vendor Wi-Fi
	o	SDN enabled Ruckus Wi-Fi (T710 and R720)
	o	Nokia Wi-Fi (AC400)
•	Nokia 4G and 5G NR
	o	4G EPC & LTE-A (Dual FDD in licensed bands for 1800MHz and 2600MHz; with 15MHz T&D licence)
	o	5G Core & 5G NR Massive MiMO (TDD band 42 at 3.5GHz; with 20MHz T&D licence) 
	o	28Ghz fixed-wireless access demonstrator for two-weeks exhibition only
•	Self-organising multipoint-to-multipoint wireless mesh network 
	o	CCS MetNet. A 26GHz with 112MHz T&D licence providing 1.2Gbps throughput
•	Massive MIMO NR radio demonstrator
	o	National Instruments (NI) Massive MIMO demonstrator 128 antenna base station
	o	12 client UE devices (TDD band 42 at 3.5GHz with 20MHz bandwidth) 
•	LiFi Access point 
	o	pureLiFi LiFi access points supporting 43Mbps
•	Cloud and NFV hosting
	o	Nokia Multi-access Edge Computing and Nokia Cloudband for network slicing and virtualisation
	o	Opensource MANO (OSM) datacentre release THREE
	o	Openstack Pike VIM datacenter for MEC VNF hosting, built upon
	o	11x Dell PowerEdge T630 compute servers with GPU support; 700+ vCPU cores, 1TB+ RAM and 100TB of HDD storage.
•	Inter-island Interconnectivity 
	o	10Gbit/s Ethernet VPLS NetPath+ from JISC to each exchange Island
	o	Dedicated secure hosting of the 5G UK Exchange in Virtus Datacentre
	o	Corsa DP2200 SDN Switch provided inter-island connectivity via OpenFlow 1.3
•	Advanced fibre optics FPGA convergence of all network technologies enabling considerable flexibility, scalability and programmability of the front/back-haul, to provide experimentation with -
	o	Elastic Bandwidth-Variable Transponders
	o	Programmable Optical White-box
	o	Bandwidth-Variable Wavelength Selective Switches (BV-WSS)
	
## Testbed architecture 
The University of Bristol Smart Internet Lab 5G testbed is a multi-site solution connected through a city-wide single mode fibre ring with several active switching nodes. The core network is located at the High-Performance Network (HPN) research group laboratory at the University of Bristol with access technologies located in Millennium Square for outdoor coverage and We The Curious science museum for indoor coverage.

### Wireless Access Technologies
Figure 1 presents the high-level architecture of the University of Bristol testbed. The design of this architecture may be described in a number of distinct technical areas:

![Control And Physical Plane Diagrams](/uploads/control-and-physical-plane-diagrams.png "Control And Physical Plane Diagrams")
**Figure 1: University of Bristol top level system architecture**

Figure 2 shows a geographical representation of the multiple access technologies deployed within Millennium Square and We The Curious, a science museum in the centre of Bristol. Connectivity terminates via fibre optic at distinct points in the square with onward links through the use of fixed wireless access mmWave radios. To allow for future expansion, termination locations have been over engineered with enough installed fibre and power capacity to allow the next generation of 5G connectivity. Space and power for mobile edge computing (MEC) has been provisioned at key locations around Millennium Square to allow the deployment of virtual network functions (VNF) and low latency real-time application processing close to the end user.


![Millennium Square](/uploads/millennium-square.png "Millennium Square")
**Figure 2: Location of the Access Points at Millennium Square and We the Curious science museum.**


![Nokia Rrh](/uploads/nokia-rrh.png "Nokia Rrh")
**Figure 3: Nokia AirScale RRH & Antenna	**


![Aps](/uploads/aps.png "Aps")
**Figure 4: Wi-Fi APs in Millennium Square	** 

![Melnet](/uploads/melnet.png "Melnet")
**Figure 5: CSS Metnet**

This testbed has combined wireless access technologies from multiple vendors across four 5G pioneer radio bands into a dynamic and flexible architecture allowing for future reconfiguration and experimentation with innovative radio architectures and waveforms. Connectivity is provided through the following solutions.

1. To provide a grounding for Nokia’s upcoming 5G NR product, Nokia have delivered and demonstrated their most advanced 4G LTE-A product, which was used in all the public demonstrators during the Layered Realities weekend. This LTE-A solution delivers a 15MHz 4x4 MIMO radio access network to our experimenters and has been tested at reliably delivering 100Mbit/s download (30Mbit/s upload) from our NFV datacentre through the Millennium Square (based on given licenced spectrum and user profile configured in the EPC).

Ongoing developments include a 5G NR Massive MIMO (TDD band 42 at 3.5GHz), which will deliver even greater network throughput rates and bandwidth sharing functionality.  Figure 3 shows the split baseband radio architecture provided by Nokia to support future migration to 5G NR through software upgrades to the System Module and replacement of the remote radio head (RRH). Two RRHs are installed in Millennium Square allowing experimentation and testing of 4G technologies with a robust roadmap to 5G.

2. To facilitate truly ubiquitous wireless connectivity for new and legacy devices, Wi-Fi networks can be provisioned using eight multi-vendor 2.4GHz and 5GHz access point (AP) deployments. The APs supplied by Nokia (shown top in Figure 4) integrate with the Nokia FlexiZone controller allowing for seamless handover between LTE and Wi-Fi, a key concept in 5G RAN design. 
 
The APs provided by Ruckus (shown middle in Figure 4) are 802.11ac Wave 2 devices utilizing 4x4 MIMO with BeamFlex+ technology for adaptive beam steering and over 1Gbps data rate per user. All Ruckus APs are controlled via an integrated SmartZone access point controller, hosted in the cloud infrastructure detailed below. This AP controller provides a North Bound interface allowing direct access by the NetOS SDN controller. This architecture facilitates network-slicing through optical, electrical and radio technologies via on-demand SSID creation.

Wi-Fi featured heavily throughout the Layered Realities weekend as a demonstration of network segmentation and as the primary radio access network for two of the public demonstrations. 

3.	The Layered Realities 5G showcase weekend demonstrated the proof of concept prototype for 5G NR Fixed Wireless Access solution providing high capacity link between the balcony and the marquee in the Millennium square. (see Figure 6 ). The solution encompassed an EPC emulator, the Nokia AirScale baseband on the AirFrame blade connected over CPRI interface to the antenna, which is a 16×16, 256 element unit. The Intel 5G MTP test UE was in the marquee. The system deployed 2 component carrier aggregation based on the available license, for a total of 200MHz channel bandwidth. This demonstrated throughput of 680Mbps observed within the marquee.

![5 Gnr](/uploads/5-gnr.png "5 Gnr")
**Figure 6 5GNR 28GHz Proof of Concept**

4.	mmWave communications are an important part of the 5G standardisation process. To showcase this technology in the University of Bristol, Smart Internet Lab 5G testbed, commercial devices provided by CCS were deployed in the network. The CCS Metnet nodes operate at 26GHz and form a self-organising mesh network for fixed wireless access with gigabit connectivity. 

Seven Metnet nodes are deployed in the testbed, connected to the Edgecore SDN switches. This architecture allows dynamic configuration of connectivity, either providing Wi-Fi backhaul over the mmWave mesh network or through the installed fibre network to the NFV cloud datacentre. With no radio planning, the CCS network is able to autonomously organise itself into a high-performance distribution and access network, demonstrating its ability to provide low-configuration last-mile access in a congested environment.

The Metnet nodes are managed and configured via an element management system (EMS) allowing allocation of bandwidth to specific high demand nodes or viewing of the current mesh topology. The CCS EMS resides in the cloud infrastructure at the University of Bristol and is accessible from the testbed’s management network. 

5.	The LTE-A network provided the 4G air interface using 15MHz bandwidth from BT in 2.6GHz spectrum and provided device connectivity for various demonstrations during the public demonstration. For validation we tested this network for throughput using a video on demand 5G network slice service towards a mix of 4G terminals receiving high definition video clips from the network simultaneously. This is shown in Figure 7 where one laptop with a 4G dongle and 5 x Samsung S8 handsets received HD video on demand simultaneously. Figure 7 shows different tests and capture of the information from the BTS or EPC management system.

![Lta](/uploads/lta.png "Lta")
**Figure 7: LTE-A service test validation**

6.	In collaboration with National Instruments (NI) and University of Bristol’s Communication Systems and Networks (CSN) research group, the future 5G air interface technology Massive MIMO has been integrated with the 5G testbed. This system comprises a 128 antenna base station and 12 client devices. Operating in the pioneer band of 3.51GHz TDD, simultaneous transmission to all clients in 20MHz bandwidth yields over 80bits/second/hertz spectral efficiency (see Figure 8). 

![Massivomimo](/uploads/massivomimo.png "Massivomimo")
**Figure 8: Massive MIMO test network at the Smart Internet Lab**

![Lifi](/uploads/lifi.png "Lifi")
**Figure 9: LiFi client dongle**

7.	To showcase the 5G principle of access-agnosticism with novel access modes, the pureLiFi AP has been integrated with the core and distribution network of the testbed. Inside the public foyer of the We The Curious museum, an exhibit has been revealed to the public demonstrating the behaviour of a network stream encoded in visible light, and the effects of blocking it with curtains. 
 
The architecture of a LiFi network is similar to Wi-Fi whereby access points communicate with clients within visible range. For LiFi, an AP resembles a ceiling light (and its secondary purpose is lighting) whilst a client is embedded within a USB dongle, creating a network bridge for any USB host (Figure 9). 

Multiple LiFi APs are controlled via an EMS residing in the University of Bristol cloud infrastructure. This entity controls all APs within the network including those based in We The Curious and the University of Bristol.

## 	Network Connectivity
The University of Bristol’s testbed has been futureproofed by delivering a wholly-uncontended, privately managed fibre network in the Millennium Square public space. The testbed’s optical-connectivity asset is comprised of a hub-and-spoke network of 96F single-mode fibre cables installed at each radio test tower, terminated at a central distribution node inside the We The Curious museum.

![Opticalspoke](/uploads/opticalspoke.png "Opticalspoke")
**Figure 10: Termination of single optical spoke in distribution node**

Being wholly owned and managed by the Smart Internet Lab, this optical connectivity asset can expand to support dozens of optical applications per radio test tower, each delivering up to 40Gbit/s uncontested throughput rates with current transceivers. This futureproofing means the testbed will be ready for whatever bandwidth and latency requirements may need to be tested and experimented upon for years to come.

Multiple urban testbed locations within Bristol is possible through the city-wide single-mode optical fibre network. This allows the island to quickly scale-out with potential deployments to include additional locations, such as the SS Great Britain and M-Shed tourist hubs. The entire datapath network within the island is switched via a distribution network of Edgecore 4610P and 5610-52X SDN switches to provide full network slicing and segmentation via a centralized NetOS SDN controller. This test network is further connected to 5G Exchange in Slough Vitus datacentre managed by 5GUK test and trial programme for national and international test network connectivity beyond one city.

![Bristolisland](/uploads/bristolisland.png "Bristolisland")
**Figure 11: Bristol’s Island Control and Management Network**

## Cloud and NFV Hosting
A primary consideration when selecting a cloud environment for NFV hosting and orchestration was to deliver a heterogeneous datacentre of multi-vendor assets. To this end the University of Bristol has implemented both an Opensource MANO (OSM) datacentre, a Nokia MEC platform and Nokia Cloudband solution. 
The OSM datacentre employs an Openstack Pike Virtualized Infrastructure Manager (VIM) for orchestration, hosting and storage of VNFs as either KVM virtual machines, or LXC containers. To integrate a network service’s VNF, Openstack Neutron provider networks, Open Daylight and NetOS SDN controllers are used. Zeetta Networks’ NetOS has allowed the testbed to extend VNFs to terminations such as Physical Network Function endpoints (e.g. Wi-Fi SSIDs). This NFV cloud solution was used in the March Layered Realities public demonstration to host network functions enjoyed by the public. This NFV cloud is built upon industry standard and popular technologies such as KVM virtualization. The Openstack cloud environment adopted by our Opensource MANO solution made use of SR-IOV passthrough techniques to give direct access to time-slices of valuable hardware (e.g. network interface cards). The VNFs were configured during instantiation using Cloud-Init scripts.


Nokia’s LTE-A solution and planned 5G NR extensions, include a MEC platform that allows the deployment and integration of virtualized cloud applications directly within the Evolved Packet Core of the network. This allows the direct connection of novel network applications at the S1 interface of the LTE-A network, eliminating almost all network-path latency from the user’s application experience. The Nokia MEC is based on established industry standard virtualization technologies already familiar to researchers and enterprises. We expect the uptake of this MEC to be as quick as the familiarization of our OSM cloud.

Lastly, Nokia’s competitor to the OSM NFV setup Cloudband is finalizing its deployment inside our testbed network. Cloudband is an ETSI MANO compatible NFV solution based on Openstack-orchestrated KVM virtualization, and Nokia Nuage SDN networking of VNFs. The finalized deployment of this platform will open to research some of Nokia’s most advanced network virtualization technologies such as distributed.

# Smart City Safety Use Case

Given the critical importance of security in cities, innovations advances in wireless communication system are increasingly improving the safety of city inhabitants. New services such as audio and video monitoring of public areas and automated municipality rule infraction detection allow a quicker response to threats and anomalies prevent reoccurrence. Based on this context UNIVBRIS has deploying a smart city safety use case, as a proof of concept, to identify suspicious activities in the city. The basic components of this use case are listed below and they are connected together to the Internet through a WiFi Interface.

* Bike rider helmet
* Raspberry PI
* 360 degree camera e audio

![Smart City Arch](/uploads/smart-city-arch.png "Smart City Arch")
**Figure 12: High level smart city safety architecture**

Figure 12 shows a high level architecture of the smart city safety use case. The bike rider carries his helmet, which has attached the Raspberry PI and the 360-degree camera. Along of his path video and audio is capturing and send via WiFi to the Mobile Edge Computing (MEC) or Cloud to be processed. Once the audio and video has been processed and any suspicious activity has been detected a notification is generated and sent to the different security agents.

## Smart City Safety Architecture

Many of today’s municipalities are becoming test beds for the smart city experimentation where technological capabilities are addressing daily needs from parking, water treatment to city security. University of Bristol is working to provide through 5GinFIRE platform a smart city safety use case which has been deployed according to the architecture shown in Figure 13. Figure 13 shows the main building blocks that make the smart city safety use case a reality. Note that only open-source frameworks (OpenStack, OpenDayLigh, etc) are being used to deploy the use case.

![Smart City Arch High](/uploads/smart-city-arch-high.png "Smart City Arch High")
**Figure 13: The main building blocks of UNIVBRIS Testbed Architecture**

The testbed is a physical and virtualized infrastructure that has been deployed as part of 5GinFIRE overall architecture. One of the main challenges in the design of VNF architecture is how to cope with multi-site orchestration and end-to-end VNF connectivity. This testbed has been deployed to operate cross-domain between ITAv and UC3M testbed. The UNIVBRIS testbed deployment will also provide VxF for FIRE testbed, providing a unique testbed that is able to assess the proposed VNF in a variety of different domains, providing excellent testing sites for heterogeneous experimentations. In particular the testbed purpose is:

•	to provide computational resources or/and slicing for hosting, deploying, instantiating and supporting VxF’s life cycle serving as a platform for conducting rigorous, transparent and replicable testing of NFV ecosystem.

## Smart City Testbed Topology/ Datacenter Topology

Figure 14 shows the overall  Network Function Virtualization Infrastructure  (NFVI) deployed at University of Bristol facility which is part of 5GinFIRE multi-site orchestration.  
	 	 	
			![Bristiol Nfvi](/uploads/bristiol-nfvi.png "Bristiol Nfvi")
**Figure 14: UNIVBRIS’ Network Function Virtualization Infrastructure**
			
The cloud environment of the UNIBRIS consists of an OpenStack Pike instance that operates on top of Ubuntu 16.04 Server operating system. The controller node is available for the project through the address 10.154.24.3 within the address range 10.154.24.0/21 for the university site.

•	Controller, Computer and Storage node: 1 server machine Intel Xeon 2.40GHz 14 cores, 128GB RAM, 800GB HD
•	Storage node: 1 server machine Intel Xeon 2.40GHz 14 cores, 128GB RAM, 800GB HD
•	One switch: Corsa DP2100 with 32 10Gb Ports 

Currently, the provider and provider2 networks are configured in Openstack and are isolated from each other. The network provider has the address 10.154.28.0/24 and the network provider2 has the address 10.154.29.0/24 that will be used as data and management network.
In the UNIBRIS site is also available the 5G Unifier Gateway at 10.154.24.5 address.
All of these features are available to the consortium through a VPN connection that has HUB as the site of 5GTONIC, which is responsible for providing credentials for connecting other partners.

# Experimentation

In the context of NVF experimentation, an experimenter in the testbed follow the phases.
•	Experiment design. The user defines the VNF at a high-level using YAML description files.
•	Auto configuration software (OSM MANO) maps this high-level description into a virtual/physical topology.
•	According to the resource availability the testbed will support the specific VxF/VNF
•	Orchestration tool is in charge of controlling the node booting process, disk image loading, and execution of VxF
•	Data collection for analysis can also be programmed using the descriptor


# Conclusions and recommendations for future work

The University of Bristol Smart Internet Lab has successfully procured, deployed and commissioned an extensive 5G test network within the heart of a growing Smart City, further boosting the already vibrant and innovative tech sector within Bristol and the surrounding the region. Although facilitating a wide range of 5G ready research capabilities from mmWave and Wi-Fi radio access networks to software defined networking and cloud computing architectures,this testbed is primarily focussed on delivering an access agnostic fixed-mobile convergence through network function virtualisation, network slicing and end-to-end service orchestration.

The key to the success of 5G resides in the seamless interoperation of heterogeneous wireless access technologies providing an integrated and cohesive level of service to a wide variety of users, both human and machine. This is enabled through tight coupling of virtualised core network services and network slicing with physical network functions. The unique aspect of the University of Bristol testbed, is that it facilitates both discrete levels of research development with each layer of technology but also across the entire stack. The novel introduction of the 5G UK Exchange through MANO presents a catalogue of network services for both local and remote experimentation. With high speed connectivity via the orchestration datacentre in Slough, new users and testbeds can connect to the multidisciplinary platform to undertake their defined research activity.

The rapid deployment of this testbed by the Smart Internet Lab across two cutting edge research groups has transformed our processes for both internal and external stakeholder management. From the intricacies of procurement and project management all the way to cyber security, artistic direction and fibre installation, this project has redefined and streamlined our methodologies, paving the way for future projects and collaboration. 

The following points summarise this project from the University of Bristol’s perspective:

•	Provisioning of cloud datacentre for edge computing and NFV hosting 
•	Creation of MANO end-to-end orchestration platform for multi-island interoperation
•	Installation of high capacity fibre connectivity for future testbed expansion
•	Deployment of five wireless access technologies for public experimentation in an urban environment
•	Platform management and support of 5G experimentation and research in service innovations

Throughout this project several items of future work have been highlighted, these recommendations are detailed below:

•	Further engineering and effort to expand 5GExchange functionalities
•	Expand the current network to cover more locations within Bristol and surrounding locations
•	Upgrade the virtual EPC core network software to 5G core once the 3GPP specifications are frozen
•	Work with network experimenters in delivery of the network slices
•	Work towards a large-scale city deployment
•	Explore links with other test networks for experimentation via the 5GExchange in Slough
•	Security and management of the network
•	Integration of external networks and internet for experimentation
•	Research in 5G NR handset prototype or commercial equipment acquisition
•	Explore other virtualisation methods (e.g. different VIMs)


# Contact

Aloizio P. Silva (aloizio.eisenmann.dasilva@bristol.ac.uk)
Merchant Venturers Building, High Performance Network Laboratory
University of Bristol – UK
Woodland Road BS8 1UB
 
