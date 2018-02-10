<!-- TITLE: 5GinFIRE Portal User Guide -->
<!-- SUBTITLE: User Guide for the Web Portal -->

# 5GinFIRE Portal User Guide

Welcome to the 5GinFIRE Portal User Guide.
5GinFIRE offered services and tools target to accommodate the following envisaged user roles. All users are assumed to be Authenticated:
* Experimenter: This role represents the user that will utilize our services and tools to deploy an experiment. That is the experiment description in terms of e.g.: NSD (Network Service Descriptor) or TOSCA Specification (in future versions)
* VxF developer: This role is responsible to upload  VNF and NSD Descriptors in the 5GinFIRE services
* Testbed provider: This role represents users that are responsible for testbed administration, configuration, integration, adaptation, support, etc
* Services administrator: This role represents the user that are responsible for maintenance of the 5GinFIRE services

Finally an anonymous user role exists who has some really simple usage scenarios (e.g. signup through the portal)

## Terminology
Please see the used terminology at the [architecture pages](5-gin-fire-terminology-experimentation-workflow-and-architecture#terminology)

## Supported processes
The process to upload/onboard VNFs, Experiements in terms of NSDs are as follows:

### 	Uploading a VxF

![Portal Diag 1](/uploads/portal-diag-1.png "Portal Diag 1")
During this process (see Figure ) the following occurs:
•	A VxF developer submits a VxF archive (he can later manage if needed some metadata)
•	The administrator can manage the VxF (e.g. edit it)
•	The administrator On-Boards the VxF to the target MANO
•	The administrator can optionally mark the VxF:
o	As public in order to be publicly visible by all portal users
o	As Certified which means this is certified by a certain entity


### Uploading an Experiment Descriptor/NSD


![Portal Diagtwo](/uploads/portal-diagtwo.png "Portal Diagtwo")
During this process (see Figure ) the following occurs:
•	An experimenter submits an experiment in terms of an NSD archive (he can later manage if needed some metadata)
•	The administrator can manage the NSD (e.g. edit it)
•	The administrator on-boards the NSD to the target MANO
•	The administrator can optionally mark the VxF:
o	As valid, which means this NSD can be indeed deployed to VIMs
o	As public in order to be publicly visible by all portal users


### Request a new experiment deployment

![Portal Diagthree](/uploads/portal-diagthree.png "Portal Diagthree")

During this process (see Figure ) the following occurs:
•	An experimenter requests a new experiment deployment (which NSD, tentative dates, target infrastructure, etc.). The request is marked as UNDER_REVIEW
•	The administrator is notified about the new request and he has the following options:
o	Schedule the deployment for the requested dates or propose other dates. The request is marked as SCHEDULED
o	Reject the request for some reason. The Request is marked as REJECTED
o	Deploy the request to target VIM(s). The Request is marked as RUNNING
o	Finalize the deployment and release resources. The Request is marked as COMPLETED
On every change of the request-lifecycle the experimenter is notified.


## Architecture

The Figure  displays a detailed architecture of the portal together with the related interfaces. The portal consists of two main components: The portal web frontend and the portal API backend. The Web front end communicates with the backend via a RESTful API. 
Moreover, the portal backend implements: An interface towards the OSM API in order to on-board VxF and NSDs to the OSM repository and get related information, and an interface towards an identity provider and a portal repository that reflects the artefacts of the OSM repository

Please check the [portal Architecture and Design](portalArchitectureDesign) section



