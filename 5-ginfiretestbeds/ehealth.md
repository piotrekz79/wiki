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

The eHealth laboratories will be connected via access networks with the PSNC R&D testbed emulating a modern Communication Service Provider (CSP) network attached to Edge and Core Clouds (see Figure 14). The network infrastructure backbone is based on ADVA FSP 3000R7 DWDM optical systems (with 10G/100G client-side interfaces) for both Metro and Core networks. On top of the optical layer, layer 2/3 services are provided by Juniper MX480 nodes which will controlled by a Juniper NorthStar SDN WAN controller (not installed yet). Edge and Core NFV/Cloud computing is provided by the PSNC SDN laboratory composed of HP Proliant DL380 and IBM System x3550 M3 rack servers, interconnected using a set of Pica8 and NoviFlow switches, and controlled by two OpenStack instances enabled for the 5GinFIRE OSM.

External access to the facility as well as communication with other 5GinFIRE facilities will be established using two VPN gateway. First OpenVPN gateway provides access to eHealth5G Core Cloud, whearas the second OpenVPN gateway provides access to eHealth5G Edge Core Cloud and eHealth EVI. Moreover, high-bandwidth data transmissions with other 5GinFIRE facilities can be available on demand by utilizing the GÉANT network connectivity services.

![Ehealth Overview](/uploads/ehealth/ehealth-overview.png "eHealth overview")
**Figure 1: Overview of eHealth5G infrastructure**

## Infrastructure

NFV infrastructure hardware details:
* 1x HP ProLiant DL380 Gen 9 compatible with Intel DPDK
* 2x IBM System x3550 M3
* 2x Pica8 P-5101 with OpenFlow 1.3/1.4 (currently configured statically)
* 1x NoviSwitch 2128 (currently configured statically) ‑ Carrier-grade OpenFlow 1.3 switch based on EZchip NP-5 with experimental extensions (DPI, metadata injection, VXLAN, security)
* 2x Juniper MX480 (universal service provider edge router) offering IP routing/Ethernet switching, MPLS, L2/L3 VPNs (VPLS, EVPN, MPLSoGRE, VXLAN) equipped with MS-DPC cards for advanced network traffic processing and analyzing (e.g.: traffic sampling, packet inspection)
* 2x Adva Optical FSP 3000R7 equipped with high-speed multimedia SDI cards (10TCC-PCN-3GSDI+10G) allowing for multiplexing and real-time transport of digital SD and HD video content in native optical OTN format (technology essential for support any high-resolution video streams like UHDTV 4k/8k, requiring up to 50Gbps bitrate or for any video 3D technology which is to be used in modern telemedicine solutions)

![Ehealth5G Data Plane](/uploads/ehealth/ehealth-5-g-data-plane.png "eHealth5G infrastructure connectivity")
**Figure 2: eHealth5G infrastructure connectivity**

## eHealth equipment
The goal of eHealth EVI is to enable the 5GinFIRE experimenters to execute a various eHealth experimental scenarios within the eHealth EVI, and for this reason, PSNC is providing a broad set of eHealth devices. Most of eHealth devices can be operated only by humans and are not network connected (doesn’t contain LTE or WiFi modules inside) thus medical/sensor data must be manually downloaded from the devices and enabled for 5GinFIRE using some mobile or stationary nodes being part of the labs.

Most of the eHealth devices are part of PSNC’s dedicated living lab space, so the sensors can be used by actual end users if a given experiment demands that. PSNC collaborates with a number of organizations and institutions within the city of Poznań, including hospitals as well as NGOs and municipal offices, which may be able to intermediate in contacting end users appropriate for the needs of a specific experiment.

**The operating room lab** contains cutting-edge endoscope and macroscopic camera, which are sources of medical video streams. This video can be delivered to processing nodes defined by the experimenter in both compressed or uncompressed form. Additionally, the operating room lab contains a H.323/SIP videoconferencing node, so the scenarios may include live audio-video interaction, e.g. for remote medical consultations:

* Storz Vitom Full HD – macroscopic surgical camera being part of high definition imaging systems for research and surgical imaging applications used for microsurgery and microdissection.
* Storz 3D endoscope ‑ contains two Full HD cameras at the tip of the endoscope, representing the left and right eye, processes to a three-dimensional view.

**The physiological parameters sensor lab** includes a set of hi-tech devices that can be used by a medical professional or patient supervised by a medical professional to gather data about the patient’s physiological parameters. This equipment includes a stomatological camera, portable ECG monitor, electronic stethoscope, mobile ultrasound tool, digital podoscope and a baropodometric platform.

* VistaCam iX ‑ a dental camera with interchangeable heads for: intraoral images, magnifying images 120x, visualizing caries and plaque, as well as light hardening
* Bittium Faros 360 ‑ a lightweight, portable 3-channel ECG for cardiac monitoring.
* Littmann 3200 ‑ an electronic stethoscope with the ability to listen remotely.
* GE Vscan – a handheld, pocket-sized ultrasound tool that provides real-time black-and-white anatomic and color-coded blood flow images at the touch of a button.
* Podoscan 2D FootCAD ‑ an advanced digital podoscope for digital analysis of footprints and plantar loads.
* FreeMed ‑ a digital baropodometric platform for static, dynamic and stabilometric analysis.

**The wellbeing sensor lab & living-lab** includes devices meant for acquiring data about the environment of a patient. Those will include various wearable sensors as well as integrated and miniature indoor sensors, activity monitoring devices and cameras.

* CubeSensor – small, connected devices that help maintain a healthy and productive indoor environment by monitoring temperature, humidity, air quality, light, noise, pressure, and movement.
* Wearable sensors ‑ health sensors integrated into various wearable accessories (garments, hats, wrist bands, eyeglasses, wristwatches, smartphones).
* Mother Sen.se – a family of small smart sensors that can be affixed to almost anything in order to detect and analyze the specific movements of every activity,  as well as measure temperature and detect the presence of people or objects at a defined location.



## Experimentation
Experimentation activities will be supported in the eHealth5G EVI through the 5GinFIRE portal. The experimenters will be able to:
* reserve eHealth device(s) for ensuring device availability and proper human staff support,
* reserve laboratory to conduct on-site experimentation with own hardware devices,
* create and deploy, from the 5GinFIRE portal, virtual functions at the eHealth5G Edge and Core Cloud, which will process data ingest from eHealth devices,
* deploy virtual machines at the eHealth5G Edge or Core Cloud infrastructure,
* monitor performance metrics of VxF execution and connectivity/traffic monitoring,
* request high-speed network connection (up to 1Gbps) to other 5GinFIRE facility allowing for combining resources and functionalities of different 5GinFIRE facilities,
* accessing experiment results stored in the Cloud.

When the eHealth5G vertical resources will be successfully reserved, the experimenters will also be able to access them physically in PSNC premises in Poznan on specified dates, or PSNC could arrange one or more people who will use the sensors, follow experimenters’ instructions and whose health and wellbeing information will be sent for further processing in the Cloud.

## Contact
**Damian Parniewicz** (damianp@man.poznan.pl)

Poznań Supercomputing and Networking Center (PSNC), Poznan (Poland)
Polish Optical Internet Research Center building, ul. Jana Pawła II 10, 61-139 Poznan