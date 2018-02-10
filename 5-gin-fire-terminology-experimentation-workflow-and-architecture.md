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
•	**Services administrator**: This role represents the user that are responsible for maintenance of the 5GinFIRE services
Finally an anonymous user role exists who has some really simple usage scenarios (e.g. signup through the portal)


### Terminology
Experiment:  In 5GinFIRE it is defined as a set of experimentation activities that will be conducted during an allocated time-slot (probably spanning for several days); the experiment may probably involve multiple 5GinFIRE test-beds; it might require the utilization of several network services, which will be indicated during the experiment definition and will be validated by the 5GinFIRE operations; these network services may be used by the experimenter during the allocated timeslot. it is a set of experimentation activities that will be conducted during an allocated time-slot (probably spanning for several days); the experiment may probably involve multiple 5GinFIRE test-beds; it might require the utilization of several network services, which will be indicated during the experiment definition and will be validated by the 5GinFIRE operations; these network services may be used by the experimenter during the allocated timeslot.
VxF: complex constellations of virtual functions, all running on a mix of real and virtual network or computing elements. We refer to virtual functions as VxFs when we do not want to distinguish between network-centric functions and vertical-centric functions.



## 5GinFIRE Experimentation Workflow

![Workflow](/uploads/workflow.png "Workflow")

The Figure displays an  overview of the workflow process. There are three main horizontal lines: the experimenter, the 5GinFIRE operations and the 5GinFIRE testbed providers that interact during an experimentation life-cycle. At the simplest case, users signed-up to the platform via the portal will be approved by 5GinFIRE Operations. To perform an experiment on top of the 5GinFIRE infrastructure at its simplest form the user needs to create an experiment, e.g. some experiment metadata, scheduling, purpose, etc and select available VNFs or deploy new ones. Then he needs to compose the experimentation solution. This can be done either as an OSM Network Service Descriptor or in terms of a TOSCA specification (in future versions). In a first version of the architecture, the user will provide an OSM-supported YAML description of the network service, potentially aided by a graphical composer. Subsequent refinements of the architecture may consider the utilization of TOSCA-based NFV descriptions, which would be mapped to into OSM-supported YAML by specific 5GinFIRE middleware (this development will depend on the availability of specification for VNF descriptors based on the TOSCA model, which is currently being addressed by both OASIS and ETSI NFV). As soon as everything is in place for an experiment description, the experimenter selects the testbed facility based on resource availability after the experiment is submitted for validation.
5GinFIRE prepares a process for validating an experiment in terms of various rules such as schedule, resource availability, etc. The validation process is closely performed together with the target testbed providers. We expect this to be iterative in various cycles involving the experimenter by either asking questions or modifying any experiment details and parameters.
As soon as an experiment is approved, it is scheduled by 5GinFIRE operations for deployment. Through the portal or OSM the 5GinFIRE operations will create a deployment (i.e. uploading descriptors etc) and OSM will later on orchestrate it (trigger the services instantiation). We expect that there will be a close collaboration during the management of the orchestration/deployment with the testbed providers. After deployment the resources are available and accessible to the experimenter.
In the end of the experiment schedule, the resources of the experiment are released and access is revoked. We expect though that any available results of the experiment will be available to the experimenter.

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



