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


