<!-- TITLE: 5GinFIRE Terminology Experimentation Workflow And Architecture -->
<!-- SUBTITLE: Architectural approach, processes and envisaged roles and usage scenarios of 5GinFIRE platform -->

# Terminology Experimentation Workflow And Architecture

The section presents 5GinFIRE architectural approach, processes and envisaged roles and usage scenarios of 5GinFIRE platform. It is comprised by technical and non-technical perspectives.

## Actors and terminology
### Actors
5GinFIRE offered services and tools target to accommodate the following envisaged user roles. All users are assumed to be of an Authenticated role:
•	**Experimenter**: This role represents the user that will utilize our services and tools to deploy an experiment. That is the experiment description in terms of e.g.: NSD (Network Service Descriptor) or TOSCA Specification
•	**VxF developer**: This role is responsible to upload  VNF and NSD Descriptors in the 5GinFIRE services
•	**Testbed provider**: This role represents users that are responsible for testbed administration, configuration, integration, adaptation, support, etc
•	**Experiment Mentor**: responsible for monitoring the progress of an experiment, resource usage and allowing or not the deployment of an experiment
•	**Services administrator**: This role represents the user that are responsible for maintenance of the 5GinFIRE services
Finally an anonymous user role exists who has some really simple usage scenarios (e.g. signup through the portal)


### Terminology
**Experiment**:  In 5GinFIRE it is defined as a set of experimentation activities that will be conducted during an allocated time-slot (probably spanning for several days); the experiment may probably involve multiple 5GinFIRE test-beds; it might require the utilization of several network services, which will be indicated during the experiment definition and will be validated by the 5GinFIRE operations; these network services may be used by the experimenter during the allocated timeslot. it is a set of experimentation activities that will be conducted during an allocated time-slot (probably spanning for several days); 
**VxF**: complex constellations of virtual functions, all running on a mix of real and virtual network or computing elements. We refer to virtual functions as VxFs when we do not want to distinguish between network-centric functions and vertical-centric functions.



## 5GinFIRE Experimentation Workflow

![Workflow](/uploads/workflow.png "Workflow")

The Figure displays an  overview of the workflow process. 
There are three main horizontal lines: the experimenter, the 5GinFIRE operations and the 5GinFIRE testbed providers that interact during an experimentation life-cycle. At the simplest case, users signed-up to the platform via the portal. To perform an experiment on top of the 5GinFIRE infrastructure at its simplest form the user needs to create an experiment, e.g. select available VNFs or deploy new ones. The VNF developer verifies that the VNF can be onboarded to the 5GinFIRE "mirror platform" or download a 5GinFIRE Virtual Machine containing tools such as OSM FOUR. If succesful, the developer can proceed with submitting the VNF. Otherwise, the developer should fix any error regarding the VNF packages or descriptors, until on-boarding is successful.  Then he needs to compose the experimentation solution. This can be done as an ETSI Yang Modelled Network Service Descriptor and make an archive. As soon as NSD is in validated and onboarded, the experimenter makes a Deployment Request by selecting the target testbed facility (see the 5GinFIRE testbeds) based on resource availability, VNF configuration and placement, and requested dates.
5GinFIRE prepares a process for validating an experiment in terms of various rules such as schedule, resource availability, etc. The validation process is closely performed together with the target testbed providers. The Experiment Mentor checks the feasibility of the experiment iterativaly in various cycles involving the experimenter by either asking questions or modifying any experiment details and parameters.
As soon as an experiment is approved, it is scheduled automatically by 5GinFIRE operations for deployment. At certain date/time OSM orchestrates it (trigger the services instantiation). After deployment the resources are available and accessible to the experimenter via VPN access. In the end of the experiment schedule, the resources of the experiment are released, and access is revoked. We expect though that any available results of the experiment will be available to the experimenter.


## Architecture 

![Architecture](/uploads/architecture.png "Architecture")
The figure displays the core architectural components implemented so far in 5GinFIRE together with their connections. Next section describes each component and its interfaces


### Portal 
A portal in terms of web application that end users (Experimenters, VxF developers) can subscribe, manage experiments, browse our repository, monitor experiment results, etc. It will also offer services that will allow admins to manage the offered 5GInFIRE platform as well as to manage the repository. It will provide Access to the 5GInFIRE repository of VxFs metadata and templates, categorized in EVIs through well specified APIs. Finally it will contain a
AAA mechanism with other FIRE testbeds via the Fed4FIRE AAI technology, thus accepting seamlessly FIRE users allowing the creation of federated experiments and facilitate integration of existing FIRE facilities
**Interfaces of Portal**
**OSM**: uses this interface to communicate with OSM via the OSM API in order to push experiment descriptions, VxF descriptors, etc
**IDP**; An identity provider mechanism for authenticating 5GinFIRE users
**Public VxF descriptors repository**: contains all VxFs registered by 5GinFIRE users
**OSM VxF descriptors repository**: It is the OSM repository where VxF that will be instantiated need to be commited

### IDP 
An Identity provider (IdP), used to provide identifiers for users that will interact with 5GinFIRE services and provide other information about the user 
**Interfaces of IDP**
**Portal**: authenticating portal users
**Support tools**: Ticketing system authentication

### Public VxF descriptors repository 
It will hold a catalog of all registered VxF descriptors. These descriptors will be available to be used by experimenters. It can have a YAML format and be compliant with other efforts like the one from the SONATA project.
**Interfaces of Public VxF descriptors repository**
**Portal**: Will accept request of managing VxF descriptors and their archives

### 5GinFIRE MANO platform 
MANO (Management and Orchestration) is one of the core concepts of the ETSI NFV reference architectural framework, in charge of allocating and configuring the infrastructure resources used by a virtualized network service, deploying and interconnecting the associated virtual network functions (VNFs) and their components, and managing the lifecycle of these functions and services on the NFV infrastructure. Considering our detailed state-of-the-art analysis on the open-source MANO frameworks currently under development, we have chosen Open Source MANO (OSM) as the base software platform to build the MANO component of the 5GinFIRE architecture 
The MANO platform of 5GinFIRE will receive orchestration actions from the 5GinFIRE portal (e.g., to create/delete a VNFD in/from the OSM catalog, to create/delete an NSD in/from the OSM catalog, to instantiate a NS, etc.). Through this interaction with the portal, the Network Service Orchestrator (NSO) of the OSM stack will receive appropriate information to instantiate the different network services comprising a given experimentation scenario, and the corresponding events related to the lifecycle of the services. The NSO will take care of the delivery of the services, interacting with the Resource Orchestrator (RO) and the VNF Configuration & Abstraction components of the OSM architecture. The RO will coordinate the allocation and setup of the computing, storage and network resources, which are necessary for the instantiation and interconnection of VxFs, interacting with the appropriate Virtualized Infrastructure Managers (VIM) available at the experimental infrastructures connected to it


**Evolution of OSM and relation to 5GinFIRE**
The short and medium term evolution of OSM aims at making new releases of the MANO software stack to be “deployment ready”, and is governed by the requirements that for each successive release are agreed by the OSM EUAG (End User Advisory Group). 5GinFIRE will put in place a continuous integration mechanism for the MANO platform, able to guarantee the availability of a state-of-the-art MANO platform as the OSM software base evolves, making it compatible with the specific requirements of an experimental facility like 5GinFIRE. The main directions identified by the OSM community for Release TWO and beyond are
·	Support of dynamic VNF and network service definition.
·	Service assurance features.
·	Enhanced security with role-based access control and authentication.
·	Support of new components via the plugin model, already present in Release ONE for incorporating new VIM components.
·	Support of different approaches to service chaining.
·	Support of recursive Network Services, allowing the creation of complex services from simple templates.
·	Enhancing user experience.
·	Modeling of VNFs and Network Services. In this particular aspect, the OSM community is committed to follow ETIS NFV results, and therefore the foreseen convergence among different data models for VNF and service descriptors.
Interfaces of the 5GinFIRE MANO platform 
**Portal**: this interface is based on the REST API of OSM, and enables the MANO platform to receive requests from the portal to execute orchestration actions.
**VIMs**: interfaces towards the VIM endpoints, to request the allocation and release of computing, storage and network resources at the partners' NFV Infrastructures.

### VIMs 
Following the architectural design of the Figure above , each partner providing an experimental infrastructure to 5GinFIRE will be in charge of the deployment and maintenance of a Virtualized Infrastructure Manager (VIM) supported by the 5GinFIRE MANO platform. Being based on the current release of OSM, release TWO, our MANO platform will natively support OpenVIM (the reference VIM of OSM), OpenStack and VMware’s vCloud Director.
This way, each VIM deployed at a partner infrastructure domain, will provide a compliant northbound API that may be used by the 5GinFIRE MANO deployment to control and manage the allocation of computing, storage and network resources at the partner NFV Infrastructure (NFVI). 
**Interfaces of VIMs**
**5GinFIRE MANO**: Support the interactions with the 5GinFIRE MANO platform.
**Testbed resources**: to control and manage the computing, storage and network resources of a partner NFVI.



### Exposed VxFs and APIs to the experimenters : 5G-In-A-Box

Different UEs can connect from Wi-Fi and/or 4G radio to b<>com * Unifier GW * . b<>com * Unifier GW * manages authentication, sessions establishment and provides IP connectivity (IPv4 only) to:
·	other servers hosting application(s) and/or 
·	Internet access.
Thanks to this IP Connectivity provided to Applications, the Application providers (e.g. OpenCall) can provide features to the connected UE using different protocols on top of this IP Connectivity.
Examples applications are: 
·	web server (http, ftp, … protocols), 
·	sip phone server (tcp/sip, udp/rtp protocols for instance), 
·	Video streaming or others. 
It can be used also by other specific Applications using information from the connected UE (localization information, information from UE camera …) to aggregate them and/or provide contextual service to the users.
In conclusion, the b<>com * Unifier GW * does not have any APIs to expose to the experimenters. However the b<>com * Unifier GW * simplify connection to APIs available either on its access networks either on PDNs that it provides.


## Resources reservation 

For the initial versions of the 5GinFIRE platform there will be not any specific automated resource reservation mechanism. We do not expect this to be a barrier since most experimentation deployments will be elastically deployed to cloud infrastructures. Nevertheless, the experiments will be validated and scheduled if there is a limited resource capability and as the work continues we will revisit the issue.





