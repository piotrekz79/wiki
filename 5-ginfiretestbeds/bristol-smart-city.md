<!-- TITLE: Bristol Smart City -->
<!-- SUBTITLE: A quick summary of Bristol Smart City -->

# Smart Internet Lab, University of Bristol
## Testbed introduction
This test network enables network slicing as a service, as required by various stakeholders as the Network Operation use case. Using 5G network concepts we deliver several services based on different network slices operating concurrently. In one slice, we deliver services for the Enhanced Mobile Broadband use case; while in another network slice, we deliver high and/or low throughputs, demanding Ultra Low Latency Reliable Services as in the Critical Communications use case. Also, several virtual networks can be grouped for different business demands and serve many devices forming the Massive Internet of Things use case.

The University of Bristol’s Smart Internet Lab 5G Testbed comprises multiple levels of research ready SDN switches connecting diverse layers of access technologies, to high performance cloud compute resources via an innovate exchange and orchestration mechanism. The focus for this test network is to enable experimentation in network service virtualisation and innovative network function testing with access agnostic connectivity to end users.


In order to explore and validate the deployment of 5G in an architecture that combines existing technologies and innovations, University of Bristol have deployed a rich testbed comprised of several networking and computing technologies, interconnecting a significant area in the Bristol city centre. This testbed aims to provide a managed platform for the development and testing of new solutions delivering reliable and high-capacity services to several applications and vertical sectors. 

The University of Bristol’s 5G testbed is a multi-site network connected through a 10km fibre with several active switching nodes, that are depicted in Figure 2. The core network is located at the High-Performance Network (HPN) laboratory at the University of Bristol and an extra edge computing node is available in another central location, known as Watershed. As shown in Figure 1, the access technologies are located in two different areas in the city centre: Millennium Square for outdoor coverage and “We The Curious” science museum for indoor coverage.

![Figure 1](/uploads/figure-1.png "Figure 1")
**Figure 1: Distribution of the testbed access technologies**

## 	University of Bristol, Smart Internet Lab’s 5G Test Network Capability

A summary of the testbed constituent equipment and capabilities is:

•	Multi-vendor software-defined networking (SDN) enabled packet switched network
     o	Corsa switch (Corsa DP2100)
     o	Edgecore switch (Edgecore AS4610 series & AS5712-54X)
		 
•	SDN enabled optical (Fibre) switched network
     o	Polatis Series 6000 Optical Circuit Switch
		 
•	Multi-vendor Wi-Fi
     o	SDN enabled Ruckus Wi-Fi (T710 and R720)
     o	Nokia Wi-Fi (AC400)
		 
•	Nokia 4G and 5G NR
     o	4G EPC & LTE-A (Dual FDD licensed bands for 1800MHz and 2600MHz; with 15MHz of T&D licence in 2600MHz band)
     o	5G Core & 5G NR Massive MIMO (TDD band 42 at 3.5GHz; with 20MHz T&D licence)
		 
•	Self-organising multipoint-to-multipoint wireless mesh network
     o	CCS MetNet a 26GHz with 112MHz T&D licence providing 1.2Gbps throughput
		 
•	LiFi Access point
     o	pureLiFi LiFi access points supporting 43Mbps
		 
•	Cloud and NFV hosting
     o	Nokia Multi-access Edge Computing (MEC)
     o	Datacentre for Application/VNF hosting, built upon
		 
•	11x Dell PowerEdge T630 compute servers 700+ vCPU cores, 1TB+ RAM and 100TB of HDD storage.

•	Advanced fibre optics FPGA convergence of all network technologies enabling considerable flexibility, scalability and programmability of the front/back-haul, to provide experimentation with -
     o	Elastic Bandwidth-Variable Transponders
     o	Programmable Optical White-box
     o	Bandwidth-Variable Wavelength Selective Switches (BV-WSS)

The available equipment is controlled using a rich software stack (showed in Figure 2) that is composed by:
      
•	Two different NFV orchestration and management solutions:
    o	Open Source MANO release THREE (opensource)
    o	NOKIA CloudBand (proprietary based on a version of OSM and OpenStack, providing network slicing and virtualisation in rapid service creation) Available July 2018
		
•	Two cloud/edge computing solutions:
    o	Openstack Pike (opensource)
    o	Nokia MEC (proprietary)
		
•	one SDN controller responsible for providing connectivity:
    o	NetOS (proprietary, based on the Open Daylight opensource)
		
			
![Bristolisland](/uploads/bristolisland.png "Bristolisland")
	**	Figure 2: Software used for management and orchestration of the testbed resources**
	
		
Within any of our projects, the aforementioned structure will be used to support different verticals demonstrators, such as entertainment, finance, manufacturing and automotive testing.

The diverse range of access technologies are interconnected in sharing the same underlying system while being used by 5GinFIRE framework to provide connectivity for the demonstrators, showcasing seamless integration between heterogeneous network components, an important concept in 5G. Additionally, the alternative and innovative technologies available, such as pureLiFi for fixed access, can be used to demonstrate the principle of access-agnosticism, also important for the 5G vision.

The state of the art radio access technologies deployed in Millennium Square deliver high-bandwidth, high-bitrate and high-reliability connections to the user equipment, therefore enabling the usage of the network-intensive distributed applications developed by demonstrators. In particular, the availability of LTE-Advanced (LTE-A) and future installations of 5G access points (Nokia 5G NR) will be especially important in demonstrating applications that require mobility while keeping user experience continuity.

The SDN capabilities expressed by the NetOS controller, will facilitate network slicing through optical, electrical and radio technologies via on-demand SSID creation, demonstrating another key concept in the 5G architecture that will be explored by projects to provide a multi-tenant environment, where the multiple demonstrators, or even final users, can coexist independently with different connectivity specifications.

The high performance and edge computing capabilities will power resource-intensive applications developed by demonstrators. In these applications, hardware acceleration and GPU-processing will be used to deliver enhanced performance and enable low-latency/real-time user interaction.

Finally, University of Bristol 5G testbed will deliver an automated and programmable environment, that will be used by any projects southbound interface to create fully integrated orchestration for both application components and network services.
	
	
## Testbed architecture 
The University of Bristol Smart Internet Lab 5G testbed is a multi-site solution connected through a city-wide single mode fibre ring with several active switching nodes. The core network is located at the High-Performance Network (HPN) research group laboratory at the University of Bristol with access technologies located in Millennium Square for outdoor coverage and We The Curious science museum for indoor coverage.


### 	Network Connectivity
The University of Bristol’s testbed has been futureproofed by delivering a wholly-uncontended, privately managed fibre network in the Millennium Square public space. The testbed’s optical-connectivity asset is comprised of a hub-and-spoke network of 96F single-mode fibre cables installed at each radio test tower, terminated at a central distribution node inside the We The Curious museum.

![Opticalspoke](/uploads/opticalspoke.png "Opticalspoke")
**Figure 10: Termination of single optical spoke in distribution node**

Being wholly owned and managed by the Smart Internet Lab, this optical connectivity asset can expand to support dozens of optical applications per radio test tower, each delivering up to 40Gbit/s uncontested throughput rates with current transceivers. This futureproofing means the testbed will be ready for whatever bandwidth and latency requirements may need to be tested and experimented upon for years to come.

Multiple urban testbed locations within Bristol is possible through the city-wide single-mode optical fibre network. This allows the island to quickly scale-out with potential deployments to include additional locations, such as the SS Great Britain and M-Shed tourist hubs. The entire datapath network within the island is switched via a distribution network of Edgecore 4610P and 5610-52X SDN switches to provide full network slicing and segmentation via a centralized NetOS SDN controller. This test network is further connected to 5G Exchange in Slough Vitus datacentre managed by 5GUK test and trial programme for national and international test network connectivity beyond one city.

![Bristolisland](/uploads/bristolisland.png "Bristolisland")
**Figure 11: Bristol’s Island Control and Management Network**

### Cloud and NFV Hosting
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
			
The cloud environment of the UNIBRIS consists of an OpenStack Pike instance that operates on top of Ubuntu 16.04 Server operating system. The controller node is available for the project through the address 10.154.24.3 within the address range 10.154.24.0/21 for the university site.

•	Controller, Computer and Storage node: 1 server machine Intel Xeon 2.40GHz 14 cores, 128GB RAM, 800GB HD
•	Storage node: 1 server machine Intel Xeon 2.40GHz 14 cores, 128GB RAM, 800GB HD
•	One switch: Corsa DP2100 with 32 10Gb Ports 

![Bristolnfvi](/uploads/bristolnfvi.png "Bristolnfvi")
**Figure 14: UNIVBRIS’ Network Function Virtualization Infrastructure**

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
 
