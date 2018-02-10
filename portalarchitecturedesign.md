<!-- TITLE: Portal architecture and design -->
<!-- SUBTITLE: A description of Portal architecture and design -->

# Portal architecture and design

![Portal Architecture](/uploads/portal-architecture.png "Portal Architecture")
The Figure  displays a detailed architecture of the portal together with the related interfaces. The portal consists of two main components: The portal web frontend and the portal API backend. The Web front end communicates with the backend via a RESTful API. 
Moreover, the portal backend implements: An interface towards the OSM API in order to on-board VxF and NSDs to the OSM repository and get related information, and an interface towards an identity provider and a portal repository that reflects the artefacts of the OSM repository
