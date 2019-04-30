<!-- TITLE: PPDR ONE -->
<!-- SUBTITLE: A quick summary of PPDR ONE -->

# PPDR ONE testbed, Internet Institute
## PPDR ONE Overview

Public Protection and Disaster Relief facility for Outdoor and iNdoor 5G Experiments (PPDR ONE) is an extension of the 5GINFIRE ecosystem with a 5G enabled telco-grade development, testing and verification facility for experimentation with 5G network architectures and services for Public Protection and Disaster Relief (PPDR). With PPDR ONE, 5GINFIRE covers the public safety sector and incorporates capabilities to conduct laboratory and field 5G experiments designed for the needs of emergency response, disaster relief, and critical infrastructure protection. Located at INTERNET INSTITUTE premises in Ljubljana, Slovenia, the facility comprises indoor and outdoor experimentation sites as well as a compact portable node for field experiments, ready to be shipped to any location in the EU.

## Features
PPDR ONE represents an all-in-one experimentation facility that delivers all components of a virtualised 5G-enabled PPDR environment – SDR-based radio and core mobile system with flexible configuration options powered by NFV, cloud backend infrastructure, a set of reference PPDR services and apps, a PPDR IoT kit, industrial and ruggedized end user devices as well as a test and validation toolkit.

The PPDR ONE facility offers:
* Indoor experimentation site, covering laboratory-based testing in all operational frequencies from 70 MHz up to 6 GHz,
* Outdoor experimentation site, supporting field operation in the 700 MHz and 4500 MHz bands
* PPDR ONE portable node, a portable compact mobile system ready to be shipped and deployed on the experimenter’s test site anywhere in the EU, covering indoor scenarios (bands from 70 MHz and up to 6.0 GHz) and field operation (based on the available frequencies at the experimenter’s location).

The PPDR ONE test bed features:
* an SDR-based mobile system (Rel.14) providing 5G-enabled PPDR infrastructure, 
* an OpenStack-based backend infrastructure incorporating NFV-ready orchestration to manage experimental instances using IaaS model,
* commercial and ruggedized user terminals and IoT devices to conduct the experiments, 
* iMON Intervention Monitoring System (www.imon.si) designed for a public safety use, providing a set of PPDR ONE services and apps available for demonstration and evaluation, 
* qMON Quality Monitoring System (www.qmon.eu), a telco-grade toolset for continuous network and service testing, verification and benchmarking.

## Architecture

The PPDR ONE facility acts as a VIM and NFVI provider, connected through a secure VPN connection with the 5TONIC core site. MANO is connected to PPDR ONE VIM via the OpenStack APIs. The EPC/eNB provisioning is realized through predefined mobile profiles (e.g. different frequency bands, bandwidth, QoS profiles etc.). Selected mobile profiles will be provisioned manually on demand via e-mail, Slack or some other tool such as Bugzilla. Compute monitoring (e.g. CPU/RAM) and network monitoring (e.g. RTT, DL/UL speed) is offered as a cloud-based service in Grafana/Kibana.

![Ppdrone Overview](/uploads/ppdrone/ppdrone-overview.png "Ppdrone Overview")
**Figure 1: Overview of PPDR ONE infrastructure**

## Infrastructure

The testbed provides two nodes:
* PPDR ONE Stationary (located in Ljubljana, Slovenia)
* PPDR ONE Portable (can be shipped at the experimenter site)

The site in Ljubljana provides cloud infrastructure over two dedicated physical servers (IBM x3550 M4), providing redundancy and migration mechanisms, and dedicated hardware Ethernet switches for data network connectivity. Additionally, 10G connectivity is provided between two host machines. 5G-ready mobile system is enabled on the dedicated physical server with integrated PCI-based SDR card with configurable parameters, such as RF channel bandwidth capability, band selection, etc. The mobile network provides connectivity from experimenters’ mobile clients (e.g., smartphone applications) to the VMs and VNFs hosted on the PPDR ONE cloud infrastructure. 

![Ppdrone Stationary](/uploads/ppdrone/ppdrone-stationary.png "Ppdrone Stationary")
**Figure 2: PPDR ONE Stationary**

The aim of the portable PPDR ONE node is to offer the same type of PPDR related infrastructure capabilities and services but on a limited performance scale due to the compact portable hardware and therefore limited resources being available. The solution includes a physical rack-mounted server in a portable transport box capable of hosting OpenStack-based cloud, provide L2/L3 network services and host 5G-ready mobile system based on a PCI SDR card. 

![Ppdrone Portable](/uploads/ppdrone/ppdrone-portable.png "Ppdrone Portable")
**Figure 3: PPDR ONE Portable**

Nodes are using separate VPN connection to 5TONIC central site and act as a separate VIM to the 5GINFIRE ecosystem.

![Facility Detailed Architecure](/uploads/ppdrone/facility-detailed-architecure.png "Facility Detailed Architecure")
**Figure 4: PPDR ONE Infrastructure**

**PPDR ONE Stationary node hardware details:**

* 2x IBM System x3550 M4	Rack server (cloud infrastructure)
	* 2x Intel Xeon E5-2660v2 10 Core / 20 Threads / 2.2GHz / 25MB Cache
	* 128GB RAM, 6x 600GB 10k SAS
	* 4x 1GbE, 2x 10GbE
	* 1x FC Dual Port 8Gb
* 1x MikroTik RM Cloud Router Switch CRS328 edge switch/router (data connectivity,	24x 1GbE (PoE), 4x 10GbE, IP routing/Ethernet switching, L2/L3 VPNs
* 1x Shuttle SH370R6	Mini tower server (mobile system)	Intel(R) Core(TM) i7-7700K CPU @ 4.20GHz, 8GB RAM, 2x 1GbE
* Amarisoft LTE/EPC software (3GPP Release 14)
* 1x Amarisoft SDR card	PCI-based SDR card with 4 antennas, GPS time synchronization option	LTE, LTE-Advanced, NB-IoT, LAA, frequencies from 70 MHz and up to 6.0 GHz including PPDR band 700 MHz flexible RF channel bandwidth from 200 kHz (NB-IoT) and up to 56 MHz

**PPDR ONE Mobile node hardware details:**

* 1x iBase FWA8708-C
	* multi-purpose industrial rack server (cloud infrastructure, data connectivity, mobile system)	6x Intel Xeon E-2174G 3.8GHz / 4.7GHz
	* 32 GB RAM
	* 128 GB SSD
	* SSD 1.92TB Enterprise Entry SATA 2.5in (1.92TB Available in RAID 1)
	* IP routing/Ethernet switching
	* Amarisoft LTE/EPC software (3GPP Release 14)
	* 1x Amarisoft SDR card	SDR card with 4 antennas, GPS time synchronization option	LTE, LTE-Advanced, NB-IoT, LAA, frequencies from 70 MHz and up to 6.0 GHz including PPDR band 700 MHz flexible RF channel bandwidth from 200 kHz (NB-IoT) and up to 56 MHz

**PPDR ONE networking**

PPDR ONE network infrastructure is segmented via VLANs and IP subnets. IP pool was assigned to PPDR ONE test bed and is further segmented to allow different network paths for PPDR ONE stationary and portable nodes. 

In general, three subnets are defined:
* Management network for VIM (used by OSM to manage life cycle of a VM in OpenStack)
* Management network for VM/VxF (use by OSM to run VNF configuration, i.e. charms)
* Data network for VM/VxF (allows communication between VM/VxF between different 5GINFIRE sites)

The current IP addressing configuration is as follows:

**Ljubljana site:**
* Management Network for VIM	10.154.96.0/24
* Management Network for VM/VxF	10.154.97.0/24
* Data Network for VM/VxF	10.154.98.0/24

**Portable node:**
* Management Network for VIM	10.154.104.0/24
* Management Network for VM/VxF	10.154.105.0/24
* Data Network for VM/VxF	10.154.106.0/24

Mobile EPC core (Amarisoft) can be configured to run in different network segments.




