<!-- TITLE: Portal architecture and design -->
<!-- SUBTITLE: A description of Portal architecture and design -->

# Portal architecture and design

![Portal Architecture](/uploads/portal-architecture.png "Portal Architecture")
The Figure  displays a detailed architecture of the portal together with the related interfaces. The portal consists of two main components: The portal web frontend and the portal API backend. The Web front end communicates with the backend via a RESTful API. 
Moreover, the portal backend implements: An interface towards the OSM API in order to on-board VxF and NSDs to the OSM repository and get related information, and an interface towards an identity provider and a portal repository that reflects the artefacts of the OSM repository

![Portal Architecture 2](/uploads/portal-architecture-2.png "Portal Architecture 2")
Above Figure  displays the architecture of the portal API. It consists of the following components:
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


## The Portal API backend
The portal API backend is written in Java. The design described here is also reflected in the code


The backend API is under <serverURL>/5ginfireportal/services/api/repo/* and <serverURL>/5ginfireportal/services/api/repo/repo/admin/* for authorized requests. For example, since our portal will be under https://portal.5ginfire.eu you can request towards: https://portal.5ginfire.eu/5ginfireportal/services/api/repo/* 
The API, Produces("application/json") and Consumes("application/json") except some POSTs that Consume("multipart/form-data") All requests should be to the /repo of the webservice. 

> 
The API endpoint is at:
https://portal.5ginfire.eu/5ginfireportal/services/api/repo/*
The API has an OpenAPI [3] specification under: 
https://portal.5ginfire.eu/5ginfireportal/services/api/swagger.json
A complete API documentation can be found at:
https://5ginfire.github.io/eu.5ginfire.portal.api/doc/html2-client/ 

