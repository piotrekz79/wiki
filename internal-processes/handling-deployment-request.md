<!-- TITLE: Internal Process -->
<!-- SUBTITLE: Handling Deployment Request -->

# Internal Process: Handling Deployment Request
## An experimenter creates a Deployment request through the portal

1) An experimenter creates a Deployment request through the portal. This (as you saw) triggers an automated New Issue in Bugzilla, Under 5GinFIRE Operations, Operations Support. By default the responsible Assignee is myself. But you also get notified via the tickets@ mailing list.
The Experimenter is added also in the CC list of the issue.
1.1) At this stage we can change the Assignee to the Mentor of the experiment.
For me is an open question if we like this or we assign it by default to another component (e.g. a new component called Deployments?)

## The Mentor drives discussions

2) The Mentor drives discussions (Mentor+5TONIC + Internal with VIM owners ). Currently in the portal there are Two admins that can manage deployments myself and Ivan but there could be also the mentors (we can have also a new Role in portal=MENTOR). An admin can respond through the portal and change the status of the Deployment Request. Whatever change you do in the portal is reflected in Bugzilla. Of course you can go directly to Bugzilla. So for example: 
if it goes in portal= SCHEDULED in Bugzilla will go IN_PROGRESS. If goes in portal= REJECTED in Bugzilla will go to RESOLVED INVALID, , etc

## The Mentor gives green or red light

3) After discussions with ((Mentor+5TONIC + Internal with VIM owners )) The Mentor gives green or red light to admins, to change the status (e.g. SCHEDULED or REJECTED) and the scheduled deployment dates, or simply reject that.
3.1) The Mentor could optionally change Assignee (e.g. an admin) or we can discuss to introduce a new Component (e.g. DeploymentCalendar)

##  Deployment Status

If it goes to portal=SCHEDULED then the guys responsible for OSM should be aware for the date of orchestration,deployment and tear down
When it is orchestrated the experiment goes to RUNNING
When it is tear down the experiment goes to COMPLETED

At any stage The portal has a Feedback text form to write text that also is copied to the experimenter and the ticket
