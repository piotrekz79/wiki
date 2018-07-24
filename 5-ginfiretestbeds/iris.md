<!-- TITLE: Iris -->
<!-- SUBTITLE: 5G radio and future networks experimentation platform -->

Iris - the reconfigurable radio testbed at Trinity College Dublin provides virtualized radio hardware, software virtualisation, Cloud-RAN, Network Functions Virtualisation (NFV), and Software Defined Networking technologies to support the experimental investigation of the interplay between 5G radio and future networks. Our facility pairs underlying flexible radio and computations resources with various hypervisors in the form of software radio frameworks, virtualized network functions (VNFs), and network slicing capabilities to realize various research and testing configurations. These platforms are connected to a private computational cloud, allowing us to deploy an array of computational environments. To expose the functionality of these platforms for a variety of applications, we employ a variety of radio hypervisors that freely enable prototyping of wireless systems, as exemplified by GNURadio. These radio hypervisors combined with dynamic distributed network functions supported by LXC, LXD and Docker containers, enable the realization of heterogeneous radio platforms that can support malleable and adaptable networks. Iris is ideally equipped to investigate the combination of network slicing, virtualisation functions, and physical layer approaches into coexisting and coherent next-generation commercial networks, including, but not limited to, 5G.
# 5G Testbed Architecture and Equipment
A high-level overview of WINS_5G testbed architecture is depicted in Fig. 1. The functional elements layer, at the bottom, represent the tangible resources including servers, switches, USRPSs, and so forth, at the Iris testbed. The virtualisation layer in the middle is supported by virtualisation technologies including OpenStack to support cloud computing, OpenFlow to slice the network, and HyDRA to virtualise the radio. The vertical resource layer at the top, supported by the Open Source Network Function Virtualization (NFV) Management and Orchestration (MANO) (OSM) software stack, will interact with the physical and virtualisation layers to instantiate EVIs. These technologies interact with the FUTEBOL EU project Container Orchestration and Provisioning Architecture (COPA) virtual machine instances  to support monitoring NFV functions in wireless, packet and optical networks, Ubuntu Containers (LXC), and GNU Radio images, exposing the functionality of physical resources to applications and across different 5G verticals.


![Fig 1 Functional Layers](/uploads/fig-2-functional-layers.png "Fig 1 Functional Layers")


Logically, the WINS_5G testbed can be thought of as consisting of five functional layers, as illustrated in Fig. 2. These include:
* Functional Elements: The bottom layer represents the physical resources, such as servers, switches, N210 USRPs, etc. These elements are sliced by the hypervisor layer.
* Virtualisation Layer: To expose the functionality of physical equipment for applications, WINS_5G employs a variety of hypervisor tools and technologies. This layer provides support for open source cloud virtualisation technologies (OpenStack), SDN techniques (OpenFlow, and Open vSwitch), and Software-Defined Radio (SDR) elements (GNU Radio with HyDRA).
* NFV Layer: OSM supports the deployment of EVIs across the Virtualisation and Functional Layer elements, by supporting the creation of virtual machine instances and instantiation of communication between virtual machines in physical rack servers. These elements provide a fully functional orchestrator for EVIs at Iris.
* Virtualised Experiments: The next layer correspond to the virtualised testbed resources, allocated to the experimenter for a specific period of time.
* Experiments / 5G Application: This layer sits at the top and is defined and controlled by the experimenter. It is the EVI environment that supports a 5G end-to-end application that can fully utilise the virtualised resources offered by the lower layers. 


# Experimentation


# Contact
Diarmuid Collins (wireless.testbed@connectcentre.ie)
