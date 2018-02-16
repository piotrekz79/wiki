<!-- TITLE: Open Source MANO -->
<!-- SUBTITLE: A  summary of OSM -->

# The 5GinFIRE MANO platform
The 5GinFIRE MANO platform is the system that enables the management and orchestration of network services (NS), potentially composed of multiple VxFs, across the NFV experimental infrastructures provided by 5GinFIRE partners. To fulfill this objective, the platform offers a northbound interface to the 5GinFIRE portal, enabling the operations that are needed to support the execution of experiments (e.g., onboarding a NS and a VxF). A simplified overview of the 5GinFIRE MANO platform is depicted in the figure below.

![Mano Platform](/uploads/mano-platform.png "Mano Platform")

The platform is based on the ETSI-hosted [Open Source MANO (OSM) project](https://osm.etsi.org/), which has been adopted by 5GinFIRE to provide the functionalities of a NFV orchestrator, supporting the management and coordination of computing, storage and network resources at the diverse experimental infrastructures, as well as the lifecycle management of network services. With this purpose, the OSM stack interacts with the Virtualized Infrastructure Managers (VIM) deployed by 5GinFIRE partners. There are currently three sites deploying the components and functionalities required to operate the 5GinFIRE MANO platform, each providing an NFV experimental infrastructure: (a) an infrastructure at the global 5G Telefonica Open Innovation Laboratory (5TONIC) [2], made available by TID (founding member of 5TONIC) and UC3M (member of 5TONIC); (b) an infrastructure located at ITAv; and (c) an infrastructure made available through a collaborative agreement by UNIVBRIS and BIO. 

The first stable version of the 5GinFIRE MANO platform is based on OSM Release TWO, being the OSM stack hosted at 5TONIC (the team is currently working on the migration to OSM Release THREE). Inter-site communications among 5GinFIRE sites are enabled by an overlay network architecture based on VPNs (to simplify operations, the primary VPN server is hosted at the same site as the MANO stack, i.e. 5TONIC). This overlay network enables the establishment of the following types of data exchanges: (a) communications between the OSM stack and the VIMs; (b) communications between the OSM stack and the VxFs, to support their configuration; (c) inter-site data communications among VxFs. 

The technical solution adopted by 5GinIFIRE also supports the flexible incorporation of other sites (e.g., coming from the Open Call process of 5GinFIRE), as long as they support a compliant VIM[^1] and they set up the appropriate inter-site connection mechanisms (see the information below).

##
In the following, we summarize the main NFV components and infrastructures that have been made available for the 1st Open Call for experimentation by 5GinFIRE testbed providers. 


[^1]: OSM Release TWO supports multiple VIMs through a plugin model, including OpenVIM, OpenStack, VMWare vCloud Director and Amazon Web Services Elastic Compute Cloud.


