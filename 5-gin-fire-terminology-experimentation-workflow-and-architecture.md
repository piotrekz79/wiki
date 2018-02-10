<!-- TITLE: 5GinFIRE Terminology Experimentation Workflow And Architecture -->
<!-- SUBTITLE: Architectural approach, processes and envisaged roles and usage scenarios of 5GinFIRE platform -->

# 5GinFIRE Terminology Experimentation Workflow And Architecture

The section presents 5GinFIRE architectural approach, processes and envisaged roles and usage scenarios of 5GinFIRE platform. It is comprised by technical and non-technical perspectives.

## 5GinFIRE actors and terminology
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


