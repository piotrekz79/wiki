<!-- TITLE: Ehealth -->
<!-- SUBTITLE: A quick summary of Ehealth -->

# eHealth testbed, PSNC
## eHealth EVI instance overview
eHealth5G facility (located in Poznan Supercomputing and Networking Center, Poznan, Poland) is a new testbed created thanks to accepted 5GinFIRE open call infrastructure project and will be available for experimenters from December 2018. eHealth5G facility extends the current 5GinFIRE architecture with a new eHealth Experimental Vertical Instance (eHealth EVI) providing 5GinFIRE experimenters with the possibility of performing experiments in the area of eHealth and telemedicine in a remotely accessible testbed designed for testing technical and usability aspects of services running on top of 5G NFV infrastructure composed of small Edge Cloud, being very closed to eHealth devices, and Core Cloud accessible via MPLS/Optical Service Provider network. The eHealth Vertical Industry infrastructure located in PSNC consists of cutting-edge eHealth equipment enabling eHealth cloud applications, products or services implementation and testing for hospitals, clinics, medical universities, medical or sports professionals.

## Architecture
The eHealth Vertical Industry infrastructure that PSNC makes accessible to experimenters via the 5GinFIRE facilities consists of eHealth devices aggregated into 3 functional groups: the operating room lab, the physiological parameter sensors lab and the patient wellbeing sensor lab & living lab:

1. The operating room laboratory includes very specialized surgical equipment equipped with video cameras.
1. The physiological parameter sensors laboratory contains hi-tech devices used by a medical professional or patient supervised by a medical professional to gather data about the patient’s physiological parameters.
1. The patient wellbeing sensor lab & living-lab are low prices devices for the private usage as wearables and indoor elements.

The eHealth laboratories will be connected via access networks with the PSNC R&D testbed emulating a modern Communication Service Provider (CSP) network attached to Edge and Core Clouds (see Figure 14). The network infrastructure backbone is based on ADVA FSP 3000R7 DWDM optical systems (with 10G/100G client-side interfaces) for both Metro and Core networks. On top of the optical layer, layer 2/3 services are provided by Juniper MX480 nodes controlled by a Juniper NorthStar SDN WAN controller. Edge and Core NFV/Cloud computing is provided by the PSNC SDN laboratory composed of HP Proliant DL380 and IBM

System x3550 M3 rack servers, interconnected using a set of Pica8 and NoviFlow OpenFlow switches, and controlled by two OpenStack instances enabled for the 5GinFIRE OSM.

External access to the facility as well as communication with other 5GinFIRE facilities will be established using VPN gateway. Moreover, high-bandwidth data transmissions with other  5GinFIRE facilities will be available thanks to the GÉANT networking services.

![Control And Physical Plane Diagrams](/uploads/control-and-physical-plane-diagrams.png "Control And Physical Plane Diagrams")
**Figure 1: University of Bristol top level system architecture**

NFV infrastructure hardware details:
* 2x HP ProLiant DL380 Gen 9 compatible with Intel DPDK
* 4x IBM System x3550 M3
* 4x Pica8 P-5101 with OpenFlow 1.3/1.4
* 2x NoviSwitch 2128 ‑ Carrier-grade OpenFlow 1.3 switch based on EZchip NP-5 with experimental extensions (DPI, metadata injection, VXLAN, security
* 2x Juniper MX480 (universal service provider edge router) offering IP routing/Ethernet switching, MPLS, L2/L3 VPNs (VPLS, EVPN, MPLSoGRE, VXLAN) equipped with MS-DPC cards for advanced network traffic processing and analyzing (e.g.: traffic sampling, packet inspection)
* 2x Adva Optical FSP 3000R7 equipped with high-speed multimedia SDI cards (10TCC-PCN-3GSDI+10G) allowing for multiplexing and real-time transport of digital SD and HD video content in native optical OTN format (technology essential for support any high-resolution video streams like UHDTV 4k/8k, requiring up to 50Gbps bitrate or for any video 3D technology which is to be used in modern telemedicine solutions)

## eHealth equipment