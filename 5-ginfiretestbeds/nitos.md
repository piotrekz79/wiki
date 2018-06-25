<!-- TITLE: NITOS -->
<!-- SUBTITLE: Network Implementation Testbed Using Open Source platforms -->

NITOS is a highly heterogeneous testbed, located in the premises of University of Thessaly in Volos, Greece. The facility is an addition to the 5GInFIRE testbed offering, accepted as a 1st Open Call infrastructure project. Through the integration of the NITOS testbed, 5GinFIRE users will have the opportunity to take advantage of several highly programmable cutting-edge resources for wireless networking (such as mmWave, SDR, LTE networks and WiFi), bundled with Software Defined Networking and Cloud Computing resources. The incorporation of this new equipment will allow the evaluation of several vertical applications for 5G over the 5GinFIRE infrastructure, including cloud based Virtual/Augmented Reality applications, wireless eHealth critical applications, wireless home entertainment, and Smart City experimentation.
# Testbed Equipment and Architecture
NITOS testbed is one of the largest single-site open experimental facilities in Europe, allowing users from around the globe to take advantage of highly programmable equipment. The testbed is an integral part of larger federations of resources, such as OneLab and Fed4FIRE, enabling experiments with more heterogeneous resources. NITOS has an established user base of over 4000 users in the past years, with over 20 researchers using the infrastructure in a daily basis. In short, the current offering of the testbed is the following:

![Nitos 1](/uploads/nitos/nitos-1.jpg "Nitos 1")

* Over 100 nodes equipped with IEEE 802.11 a/b/g/e/n/ac compatible equipment, and using open source drivers. The nodes are compatible also with the IEEE 802.11s protocol for the creation of wireless mesh networks. The nodes feature multiple wireless interfaces, and are high-end computers, with quad-core Intel Core i5 and Core i7 processing capabilities, 4/8 GBs of RAM and SSD disks.
* Commercial off-the-shelf (COTS) LTE testbed, consisting of a highly programmable LTE macrocell, multiple femtocells, an experimenter configurable EPC network and multiple User Equipment (UE), such as USB dongles and Android Smartphones.
* Open Source LTE equipment, running over commodity Software Defined Radio (SDR) equipment, by the adoption of the OpenAirInterface (www.openairinterface.org) platform. The platform is allowing multiple configurations for creating highly customizable beyond 4G networks. 
* COTS WiMAX testbed, based on a highly programmable WiMAX base station in standalone mode (no ASN-GW component), along with several open source WiMAX clients. 
* A Software Defined Radio (SDR) 5G testbed, consisting of 10 USRPs N210, 12 USRPs B210, 4 USRPs X310 and 4 ExMIMO2 FPGA boards. MAC and PHY algorithms are able to be executed over the SDR platforms, with very high accuracy.
* A millimeter wave testbed, operating in the V-band (60GHz), based on six nodes. The platforms support high data-rate point-to-point setups, with beam steering capabilities of up to 90 degrees with a step of 7.5 degrees.
* The nodes are interconnected with each other via 5 OpenFlow hardware switches, sliced using the FlowVisor framework. 
* A Cloud Computing testbed, consisting of 96 Cores, 286 GB RAM and 10 TBs of hardware storage. For the provisioning of the cloud, OpenStack is used.
* Multiple WSN clusters, supporting the IEEE 802.15.4, 802.11 and LoRaWAN protocols, gathering measurements such as temperature, luminosity, air quality, radiation emission, etc. 

![Nitos 2](/uploads/nitos/nitos-2.png "Nitos 2")


# Experimentation
NITOS is providing the testbed resources based on the Metal as a Service paradigm. In the context of 5GInFIRE, the end users will be able to instantiate VNFs from the 5TONIC orchestrator, on top of the physical infrastructure of NITOS, and send their traffic over different wireless networks. The deployed VNFs are using a wireless virtual link to other VNFs, as connected through the OSM User Interface. 

![Vnfs Over Nitos](/uploads/nitos/vnfs-over-nitos.png "Vnfs Over Nitos")      ![4 Nitos 4](/uploads/nitos/4-nitos-4.png "4 Nitos 4")      ![5 Nitos 5](/uploads/nitos/5-nitos-5.png "5 Nitos 5")

The process for experimentation is the following:
* Reserve NITOS node and equipment related to wireless experimentation
* Create and deploy from the portal and orchestrator VNFs attached to different wireless technologies
* Deploy VNFs that can intercommunicate with VNFs located at other sites of 5GInFIRE
* Get access on the VNFs and host machine while running their experiment
* Collect measurements related to their experiment for further analysis

All the resources of the testbed are remotely accessible and programmable, based on the guidelines for the different types of equipment, as shown here: http://nitlab.inf.uth.gr/doc

# Contact
Nikos Makris (nimakris@uth.gr)
Christos Zarafetas (hrzarafe@uth.gr)
Thanasis Korakis (korakis@uth.gr)