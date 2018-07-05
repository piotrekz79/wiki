<!-- TITLE: The 5GinFIRE Healthcheck service (HCS) -->
<!-- SUBTITLE: Introduction and Usage of the 5GinFIRE Healthcheck service -->

# Introduction and Usage of the 5GinFIRE Healthcheck service (HCS)

The Healthcheck Service (HCS) is a simple service that displays the status of various services, components and processes of the 5GinFIRE infrastructure.

## How it works

**Components** are polled (**ACTIVE** mode) or report their status (**PASSIVE** mode). 
If the HCS fails to learn the status of a **Component** within a defined  **Threshold** then the component is marked as FAIL/DOWN.

## Modes
There are two modes ACTIVE and PASSIVE.

### ACTIVE mode

During active mode the HCS polls the **Component** via a URL. If the URL returns 200 OK then the **Component** is UP. A constraint here is that the HCS must have a connectivity with the target component.

example:
"name": "PORTAL"
mode": "ACTIVE",
checkURL": "https://5ginfire.portal.eu",
failoverThreshold: 600

In this example the HCS will check regularly the URL https://5ginfire.portal.eu. If it fails to get a 200 OK will try again in a few minutes. If within 10 minutes (600 seconds) fails to get a 200OK then the service will be marked as DOWN. An Issue will be raised automatically.


### PASSIVE mode

The PASSIVE mode can be used by components that cannot accept connections from the HCS but have internet connection (e.g. a VIM). 
The component reports that is alive through a GET request to the HCS 



### Component status
				
 UP,
	DOWN,
	PASS,
	FAIL
				