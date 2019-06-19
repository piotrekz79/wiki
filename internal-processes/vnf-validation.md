<!-- TITLE: VNF Validation -->
<!-- SUBTITLE: Internal process for a VNF Validation -->

# VNF Validation (Manual process)

This page describes the process for validating a VNF. This manual process will be replaced in near future by an automated process

## Portal submission
The VNF archive is submitted to the portal. This automatically creates a ticket in  Product: **5GinFIRE Operations**, Component: **Validation**   see: https://portal.5ginfire.eu/bugzilla/buglist.cgi?component=Validation&list_id=186&product=5GinFIRE%20Operations&resolution=---
This first step triggers that at least the portal has correctly parsed the descriptor.

## VNF Validation
The VNF submition triggers a Validation mechanism and a related message appears to the Bugzilla ticket. If the submitted VNF passes successfully the Validation, the ticket status is changed to RESOLVED-FIXED automatically in the portal.

## VNF Onboarding
### OSM2
Once the VNF is Certified the Onboarding is completed by portal administrator
The VNF which is marked as Certified is onboarded by the portal administrator to the 5GinFIRE OSM component at 5TONIC. 
The issue changes assignee to a person in 5TONIC/UC3M/OSM team (Ivan?)
In nominal situation the VNF will get a status ONBOARDED.
In case the VNF is ONBOARDED SUCCESSFULLY the VNFD is marked as Certified and the status of the Bugzilla ticket status should be RESOLVED-FIXED.
**Exception:** if there is no way to onboard it due to errors, the Bugzilla ticket status is changed to CONFIRMED, the VNF is marked as NOT-CERTIFIED and the 5TONIC team needs to manually identify why this is not possible.

### OSM4
The VNF is automatically onboarded to the 5GinFIRE OSM component at 5TONIC. 
In case the VNF is ONBOARDED SUCCESSFULLY the VNFD is marked as Certified and the status of the Bugzilla ticket status should be RESOLVED-FIXED.
**Exception:** if there is no way to onboard it due to errors, the Bugzilla ticket status is changed to RESOLVED/INVALID, the VNF is marked as NOT-CERTIFIED 

## OSM verification
The 5TONIC/UC3M/OSM team will try to check the VNF (* this could also involve the Mentor for the experiment*)
If the team claims that the VNF is invalid, changes the issue in Bugzilla accordingly, so that portal administrators and VNF creator are notified. In this case the VNF needs to be marked as NOT-CERTIFIED to allow changes in the VNF.

## VNF is VALID
If everything is ok, the VNF is presented as Certified in the portal.should be available for usage in NSDs.

## VNF is Published
After VNF owner's permission the VNF can be published for the VNF to be usable from other users besides the VNF owner.
