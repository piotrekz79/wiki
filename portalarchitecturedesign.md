<!-- TITLE: Portal architecture and design -->
<!-- SUBTITLE: A description of Portal architecture and design -->

# Portal architecture and design

![Portal Architecture](/uploads/portal/portal-architecture.png "Portal Architecture")
The architecture in Figure supports: i) automation and multiple services, ii) the evolution of components as well as iii) to transform the portal into a BSS/OSS system as defined in the ETSI reference architecture. 

These are the services that the portal service needs to interact with:
-	The Continuous Integration service that will perform the validation of submitted VNFs and NSDs
-	OSM: There is a continuous evolution of OSM, which has a roadmap to provide new versions of OSM almost every 6 months. This evolution involves the North Bound API that the portal consumes which usually changes. The portal needs to support various version of OSM to ease the process between testing and production. 
-	Issue management system - Bugzilla: the portal needs to notify the 5GinFIRE operations automatically via the issue management system for various events, such as reporting 
-	VNF Images repositories: These repositories contain the VNF images that need to be deployed in target VIMs 
-	Policies/Rule engine: This service should keep various rules, such as which VNFs are allowed to be placed on target testbeds, roles permissions, etc
-	Infrastructure health status services, central logging and alerting: the portal reports its health status as well as some information logging or generate alerts
-	VIM monitoring information: VIMS might report information to the portal about their status
-	OAuth 2.0 mechanisms: to support authentication from 3rd parties
-	The FIRE Aggregation Manager service: to support access of FIRE users to 5GinFIRE testbed

Having the above needed interfacing, the portal service consists of the following components:
•	Portal model: contains the model of entities, their definitions and associations of the portal entities like users, VxF/NSD experiment metadata, categories, etc.
•	Persistence and DB: a persistence layer based on OpenJPA [1] to keep entities permanently available through the database system based on MySQL .
•	User identity: This is based on Openstack Keystone  service [2]
•	AA: Authentication and authorization mechanism(s) to allow access to the portal API based on Apache SHIRO [3]
•	Webservice REST API: implementation of the portal API server based on Apache CXF [4]
•	OSM models and clients: implementation of a client and its model that communicates with OSM via the Northbound API, in order to on-board VxF and NSDs to the OSM repository and get related information, instantiate NSDs, etc. Each supported OSM version (e.g. TWO, THREE, FOUR) as well as future version might have multiple client connectors to support backward connectivity and future migration from testing to production systems
•	OAuth 2.0 Client API AA: implementation of a client that can communicate with service(s) to authenticate/authorize users via OAuth 2.0
•	A messaging/routing service bus: This is used to route messages to various services and is based on Apache Camel

![Portal Architecture 2](/uploads/portal/portal-architecture-2.png "Portal Architecture 2")
The above Figure  displays the architecture of the [portal API](/portalarchitecturedesign/portal-api). It consists of the following components:
•	Portal model: contains the model of entities, their definitions and associations of the portal entities like users, VxF/experiment metadata, categories, etc.
•	Persistence and DB: a persistence layer to keep entities permanently available  through a database system.
•	AA: Authentication and authorization mechanism(s) to allow access to the portal API
•	RESTAPI: implementation of the portal API server
•	OSM client API: implementation of a client that communicates with OSM via the OSM API
•	Client API AA: implementation of a client that is capable of communicating with another AA service(s) to authenticate/authorize users

The web frontend architecture consists of the following components:
•	The Angular framework which supports the web implementation
•	The UI web pages facing the end users
•	The controllers for each page
•	The services that correspond to model entities (VxF, User, Experiment, etc.) and provide communication means with the API backend

