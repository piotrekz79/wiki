<!-- TITLE: NSD Validation -->
<!-- SUBTITLE: Internal process for a NSD Validation -->

# NSD Validation (Manual process)

This page describes the process for validating a NSD. This manual process will be replaced in near future by an automated process.

## Portal submission
The NSD archive is submitted to portal. This automatically creates a ticket in  Product: **5GinFIRE Operations**, Component: **Validation**   see: https://portal.5ginfire.eu/bugzilla/buglist.cgi?component=Validation&list_id=186&product=5GinFIRE%20Operations&resolution=---
This first step triggers that at least the portal has correctly parsed the descriptor.
## NSD Onboard by portal administrator
The NSD is then onboarded by the portal administrator to the 5GinFIRE OSM component at 5TONIC. 
The issue changes assignee to a person in 5TONIC/UC3M/OSM team (Ivan?)
In nominal situation the NSD will get a status ONBOARDED.
**Exception:** if there is no way to onboard it due to errors, the 5TONIC team needs to manually identify why this is not possible

## OSM verification
The 5TONIC/UC3M/OSM team will try to check the NSD (* this could also involve the Mentor of the experiment*)
If the team claims that the NSD is valid or invalid, changes the issue in Bugzilla accordingly, so that portal administrators and NSD creator are notified.

## DVNF is VALID
If everything is ok, the NSD should be available for usage in experiments.