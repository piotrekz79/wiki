<!-- TITLE: Portal Api -->
<!-- SUBTITLE: A quick summary of Portal Api -->

# The Portal API backend
The portal API backend is written in Java. The design described here is also reflected in the code

The backend API is under <serverURL>/5ginfireportal/services/api/repo/* and <serverURL>/5ginfireportal/services/api/repo/repo/admin/* for authorized requests. For example, since our portal will be under https://portal.5ginfire.eu you can request towards: https://portal.5ginfire.eu/5ginfireportal/services/api/repo/* 
The API, Produces("application/json") and Consumes("application/json") except some POSTs that Consume("multipart/form-data") All requests should be to the /repo of the webservice. 

> The API endpoint is at:
https://portal.5ginfire.eu/5ginfireportal/services/api/repo/*
A complete API documentation can be found at:
https://5ginfire.github.io/eu.5ginfire.portal.api/doc/html2-client/ 
The API has an OpenAPI [^1] specification under: 
https://portal.5ginfire.eu/5ginfireportal/services/api/swagger.json


Here is a login example: 


```sh
curl -v -H "Content-Type: application/json" -X POST --data '{"username":"admin", "password":"changeme"}' https://portal.5ginfire.eu/5ginfireportal/services/api/repo/sessions
```
example response :

```json
{
	"username": "admin",
	"password": "",
	"portalUser": {
		"id": 1,
		"organization": "5GinFIRE",
		"name": "Portal Administrator",
		"email": "tranoris@ece.upatras.gr",
		"username": "admin",
		"password": "",
		"active": true,
		"currentSessionID": "5ec34075-1a12-46d8-97ec-b9e1ab064666",
		"roles": [
			"PORTALADMIN"
		]
	}
}
```








[^1]: https://www.openapis.org/.