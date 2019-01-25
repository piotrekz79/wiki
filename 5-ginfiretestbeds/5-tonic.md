<!-- TITLE: 5 Tonic -->
<!-- SUBTITLE: A quick summary of 5 Tonic -->

# The 5TONIC laboratory
The global 5G Telefonica Open Network Innovation Centre (5TONIC) [1](https://www.5tonic.org) has been established in Madrid (Spain) as a leading European hub for knowledge sharing and industry collaboration in the area of 5G technologies. The laboratory provides an open research and innovation ecosystem for industry and academia that promotes joint project development, joint entrepreneurial ventures, discussion fora, and a site for events and conferences, all in an international environment of the highest impact. 5TONIC also serves to evaluate and demonstrate the capabilities and interoperation of pre-commercial 5G equipment, services and applications. Currently, the 5TONIC laboratory has ten members: Telefonica, Institute IMDEA Networks, Ericsson, Intel, Commscope, Universidad Carlos III de Madrid, Cohere Technologies, InterDigital, Altran, and RedHat.


## Organization 
The 5TONIC laboratory, as a multipurpose environment, counts with multiple racks, which may be flexibly interconnected according to any experimentation requirements, along with a common infrastructure to aid experimentation, trials, and demonstrations with 5G products and services. In particular, secure access to external sites can be provided via VPN gateways, allowing different solutions to support management, control and data operations from remote network locations, depending on specific requirements. In the following, we describe the main infrastructure and equipment that is available at 5TONIC to support experimentation activities in the context of 5GinFIRE. A schematized overview of this infrastructure is shown in the figure below.

![5 Tonic Organization](/uploads/5-tonic/5-tonic-organization.png "5 Tonic Organization")

Regarding the orchestration service, the 5GINFIRE MANO platform provides a dual orchestration software stack, supporting Releases TWO [2] and FOUR [3] of the OSM software. This enables the coexistence of network services, and VxFs developed under both versions of OSM (due to different design criteria, Releases FOUR and TWO of OSM are not fully compatible), as well as the re-creation of experiments carried out during the second year of 5GinFIRE (when only Release TWO was available). Following this dual stack approach, two installations of OSM (one for Release TWO and another one for Release FOUR) run in independent virtual machines on a server computer with 16 cores, 128 GB RAM, 2 TB NLSAS hard drive and a network card with 4 GbE ports and DPDK support.

The same server computer hosts a VIM instance based on OpenStack Ocata [4], which allows allocating experiments to an NFV infrastructure composed by two high-profile servers, each equipped with eight cores in a NUMA architecture, 128GB RDIMM RAM, 4TB SAS and eight 10Gbps Ethernet optical transceivers with SR-IOV capabilities. These servers are currently interconnected in the data plane by a 24-port 10Gbps Ethernet switch. This NFVI forms part of the infrastructure of the IMDEA Networks Institute at 5TONIC, hence its utilization is coordinated and shared with other projects and demonstration activities.

An additional and independent instance of OpenStack Ocata is deployed in a separate server computer with six cores, 32GB of memory, 2TB NLSAS, and a network card with four GbE ports and DPDK support. This VIM controls a dedicated NFVI that is solely allocated to experimentation activities within 5GINFIRE. This infrastructure consists of a set of three server computers, each with the same hardware characteristics as the server computer hosting the VIM. These servers are interconnected by a GbE data-plane switch.

In both VIM instances, the OpenStack networking service was installed to support layer-3 services, and the ML2 plug-in of OpenStack was configured to use Linux bridges. The terms and conditions that govern the utilization the aforementioned NFV infrastructures are detailed in the 5GinFIRE website [4].

Finally, the experimentation infrastructure offered to 5GinFIRE includes some server computers (not shown in the figure) to support complementary functionalities, e.g., hosting client applications, deploying a network management system, and performing access-control functionalities. Regarding the latter, a physical jump machine serves to control the access of the 5GinFIRE experimenters to the NFV infrastructures (see []()).


5TONIC: an open research and innovation laboratory focusing on 5G technologies: https://www.5tonic.org