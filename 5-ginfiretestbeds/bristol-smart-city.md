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

