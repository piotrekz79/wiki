<!-- TITLE: The 5GinFIRE Healthcheck service (HCS) -->
<!-- SUBTITLE: Introduction and Usage of the 5GinFIRE Healthcheck service -->

# Introduction and Usage of the 5GinFIRE Healthcheck service (HCS)

The Healthcheck Service (HCS) is a simple service that displays the status of various services, components and processes of the 5GinFIRE infrastructure.

## How it works

**Components** are polled (**ACTIVE** mode) or report their status (**PASSIVE** mode). 
If the HCS fails to learn the status of a **Component** within a defined  **Threshold** then the component is marked as FAIL/DOWN.

## Components

We have defined the following Component Types:
* 	SERVICE : a generic service, e.g. PORTAL,OSM
* 	PROCESS: an automated process that is succesful or not. E.g. PING_PING_INSTANTIATION_TEST executed by jenkins every night
* 	VIM: a facility,e.g. BRISTOL
* 	CONNECTIVITY: a connection between components. eg PORTAL-OSM, OSM-ITAV, OSM-BRISTOL, etc

## Modes
There are two modes ACTIVE and PASSIVE.

### ACTIVE mode

During active mode the HCS polls the **Component** via a URL. If the URL returns 200 OK then the **Component** is UP. 
A constraint here is that **the HCS must have a connectivity with the target component**.

Example the HCS will poll the PORTAL component. 
Component name = PORTAL
mode: ACTIVE,
checkURL": https://5ginfire.portal.eu
failoverThreshold: 600

In this example the HCS will check regularly the URL https://5ginfire.portal.eu. If it fails to get a 200 OK will try again in a few minutes. If within 10 minutes (600 seconds) fails to get a 200OK then the service will be marked as DOWN. An Issue will be raised automatically.


### PASSIVE mode

The PASSIVE mode can be used by components that cannot accept connections from the HCS but have internet connection (e.g. a VIM). 
The component reports that is alive through a GET request to the HCS. The URL format is:

```text
[hcserviceurl]/admin/components/{*componentname*}/{*apikey*}
```

*componentname* is a Unique name of the component, e.g. PORTAL, OSM, BRISTOL
*apikey* is a unique string for each component. (apikeys will be given by the HCS admins)

Example, BRISTOL reports that is alive (e.g. in a cron with a script):

```text
wget   ://HCSURL/hc/services/api/admin/components/BRISTOL/8756118f-66bf-1234-a409-22e37f89b36a
```

Example, OSM reports that can connect to ITAV VIM. OSM will issue (e.g. in a cron with a script):
```text
wget   ://HCSURL/hc/services/api/admin/components/OSM-ITAV/1234568f-9876-1234-a409-5a6e8a89b36a
```


### Component status

A Component can be in the following states:	
* UP: is alive
* DOWN: is not alive
* PASS: used in PROCESS type. The process passes test within threshold
* FAIL: used in PROCESS type. The process failed test within threshold
				


