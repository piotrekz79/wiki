<!-- TITLE: NSD Validation -->
<!-- SUBTITLE: Internal process for a NSD Validation -->

# NSD Validation (Manual process)

This page describes the process for validating a NSD. This manual process will be replaced in near future by an automated process.

## Portal submission
The NSD archive is submitted to the portal. This automatically creates a ticket in  Product: **5GinFIRE Operations**, Component: **Validation**   see: https://portal.5ginfire.eu/bugzilla/buglist.cgi?component=Validation&list_id=186&product=5GinFIRE%20Operations&resolution=---
This first step triggers that at least the portal has correctly parsed the descriptor.
## NSD Onboard by portal administrator

### OSM2
The NSD is then onboarded by the portal administrator to the 5GinFIRE OSM component at 5TONIC. 
The issue changes assignee to a person in 5TONIC/UC3M/OSM team (Ivan?)
In nominal situation the NSD will get a status ONBOARDED. The Bugzilla ticket status is changed to RESOLVED-FIXED and the NSD is marked as Valid (in order for the NSD to appear in the list for Deployment Requests).
**Exception:** if there is no way to onboard it due to errors, the ticket status is changed to VERIFIED the NSD should be marked as NOT-VALID and the 5TONIC team needs to manually identify why this is not possible

### OSM4
**VLD setup**
The experimenter should name the Management and Data VLDs in the yaml file appropriately for automatic network definition during automatic instantiation of the NS.
	-The VLD which will be used for the **Management plane** should have a name ending in **"_mgmt"**.
	-The VLD which will be used for the **Data plane** should have a name ending in **"_data"**.

The NSD is then onboarded automatically to the 5GinFIRE OSM component at 5TONIC. 
In nominal situation the NSD will get a status ONBOARDED. The Bugzilla ticket status is changed to RESOLVED-FIXED and the NSD is marked as Valid (in order for the NSD to appear in the list for Deployment Requests).
**Exception:** if there is no way to onboard it due to errors, the ticket status is changed to RESOLVED-INVALID the NSD should be marked as NOT-VALID and the 5TONIC team needs to manually identify why this is not possible

## OSM verification
The 5TONIC/UC3M/OSM team will try to check the NSD (* this could also involve the Mentor of the experiment*)
If the team claims that the NSD is valid or invalid, changes the issue in Bugzilla accordingly, so that portal administrators and NSD creator are notified.

## NSD is VALID
If everything is ok, the NSD should be available for usage in experiments.