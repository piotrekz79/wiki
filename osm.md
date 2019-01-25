<!-- TITLE: The 5GinFIRE MANO platform -->
<!-- SUBTITLE: A description of the 5GinFIRE MANO platform -->

# The 5GinFIRE MANO platform
The 5GinFIRE MANO platform is the system that enables the management and orchestration of network services (NS), potentially composed of multiple VxFs, across the NFV experimental infrastructures provided by 5GinFIRE partners. To fulfill this objective, the platform offers a northbound interface to the 5GinFIRE portal, enabling the operations that are needed to support the execution of experiments (e.g., onboarding a NS and a VxF). A simplified overview of the 5GinFIRE MANO platform is depicted in the figure below.

![Mano Platformv 2](/uploads/5-tonic/mano-platformv-2.png "Mano Platformv 2")

The platform is based on the ETSI-hosted [Open Source MANO (OSM) project](https://osm.etsi.org/), which has been adopted by 5GinFIRE to provide the functionalities of a NFV orchestrator, supporting the management and coordination of computing, storage and network resources at the diverse experimental infrastructures, as well as the lifecycle management of network services. With this purpose, the OSM stack interacts with the Virtualized Infrastructure Managers (VIMs) deployed by 5GinFIRE partners. 

The MANO platform supports multi-site experimentation activities across different vertical domains:

1)	An infrastructure at the global 5G Telefonica Open Innovation Laboratory (5TONIC), made available by TID and UC3M, to support experimentation with NFV functions and services.
2)	An experimentation facility located at ITAv, providing access to an automotive testbed in the city of Aveiro (Portugal).
3)	An infrastructure made available by UNIVBRIS, supporting experimentation activities over a smart city environment in the city of Bristol (UK).
4)	An experimentation facility at UFU, located at Uberlândia (Brazil), enabling trialling with 5G applications with a particular consideration on the edge network resources.
5)	An infrastructure provided by the NITOS testbed, i.e., 5GVINO, hosted by the University of Thessaly (Greece), which provides access to programmable resources for wireless networking, SDN and cloud computing facilities.
6)	An eHealth experimental vertical facility, eHealth5G, hosted by the Poznan Supercomputing and Networking Center (Poland); this facility supports experimentation in the area of telemedicine and eHealth, offering access to: realistic eHealth equipment; a small Edge Cloud, close to eHealth devices; and a core cloud accessible via MPLS/Optical service provider network.
7)	A reconfigurable radio testbed at Trinity College Dublin (Ireland), Iris, supporting radio hardware, cloud-RAN, NFV, and SDN technologies. This testbed has been extended and made available for experimentation activities in 5GinFIRE. We refer to this testbed extension as WINS_5G.

The current version of the 5GinFIRE MANO platform is based on OSM Release FOUR, being the OSM stack hosted at 5TONIC. Inter-site communications among 5GinFIRE sites are enabled by an overlay network architecture based on VPNs (to simplify operations, the primary VPN server is hosted at the same site as the MANO stack, i.e. 5TONIC). This overlay network provides authorized partners a secure access with certificate-based authentication to 5TONIC, enabling the establishment of the following types of data exchanges: (a) communications between the OSM stack and the VIMs; (b) communications between the OSM stack and the VxFs, to support their configuration; (c) inter-site data communications among VxFs. 

The technical solution adopted by 5GinIFIRE also supports the flexible incorporation of other sites (e.g., coming from the Open Call process of 5GinFIRE), as long as they support a compliant VIM[^1] and they set up the appropriate VPN based inter-site connection mechanisms (see the information below).

[^1]: OSM Release FOUR supports multiple types of VIMs through a plugin model, including OpenVIM, OpenStack, VMWare vCloud Director, and Amazon Web Services Elastic Compute Cloud.


## Addressing plan
Enabling effective network communications among multiple sites has required a careful definition of the IP address space to be used by interconnecting entities. In this respect, the following agreements have been taken by 5GinFIRE:

1)	Entities connecting to the 5GinFIRE MANO platform will use the private address space **10.154.0.0/16** for control and data plane communications.
2)	5TONIC will use the private address space **10.4.0.0/16** to support control and data plane communications.

The 5GinFIRE network operations center will be in charge of the allocation of IP address ranges to entities within the address space 10.154.0.0/16. The current allocation of IP addresses to sites is summarized as follows:

- **5TONIC**: 10.4.0.0/16.
- **ITAv**:	10.154.0.0/20.
- **UNIVBRIS & BIO**:	10.154.16.0/20.
- **Reserved for administrative purposes:** 10.154.255.0/23

Any potential issues related with the allocation of IP addresses to external sites that connect to the MANO platform will be treated on a case-by-case basis.

## Requirements to support the interconnection of external sites
Beyond any particular requirements that may be identified when facing the interconnection of specific external sites, which will be treated on a case-by-case basis, in the following we indicate a non-exhaustive list of requirements that must be fulfilled by external entities to connect to the 5GinFIRE MANO platform:

1) Utilization of a compliant VIM solution, i.e., compliant with OSM Release TWO[^2].
2) Obtaining an appropriate IP address space, along with VPN credentials to gain a secure access to 5TONIC, from the 5GinFIRE network operations center. 
3) Configuration of the site with the allocated IP address space.
4) Configuration of any necessary VPN endpoints, to connect the site to the overlay network of the 5GinFIRE MANO platform. These endpoints will then support the exchange of control and data-plane information with the other NFV components of 5GinFIRE (OSM stack, VxFs, etc.).
5) Configuration of the appropriate VIM networks to enable control and data-plane communications with the VxFs deployed at the entity’s datacenter,
and using the allocated IP address space.
6) Support routing of control and data plane information across the local network segments of the external entity, to support communications between the VPN endpoints and the VIMs/VxFs and vice versa.

