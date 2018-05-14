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

Figure 2 shows a geographical representation of the multiple access technologies deployed within Millennium Square and We The Curious, a science museum in the centre of Bristol. Connectivity terminates via fibre optic at distinct points in the square with onward links through the use of fixed wireless access mmWave radios. To allow for future expansion, termination locations have been over engineered with enough installed fibre and power capacity to allow the next generation of 5G connectivity. Space and power for mobile edge computing (MEC) has been provisioned at key locations around Millennium Square to allow the deployment of virtual network functions (VNF) and low latency real-time application processing close to the end user.



