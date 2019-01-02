<!-- TITLE: Internal Process -->
<!-- SUBTITLE: Handling Deployment Request -->

# Internal Process: Handling Deployment Request
## An experimenter creates a Deployment request through the portal
### OSM2
1) An experimenter creates a Deployment request through the portal. 
2) This triggers an automated New Issue in Bugzilla, Under 5GinFIRE Operations, Operations Support. 
3) By default the responsible Assignee is The component owner of **5GinFIRE Operations->Operations Support** (https://portal.5ginfire.eu/bugzilla/buglist.cgi?component=Operations%20Support&list_id=159&product=5GinFIRE%20Operations&resolution=---). 
4) 5GinFIRE team is also get notified via the tickets@ mailing list.R
5) The Experimenter is added also in the CC list of the issue.

#### Change the Assignee to the Mentor of the experiment

1) At this stage we  change the Assignee to the **Mentor** of the experiment by checking the "Experiment Name" field in the Bugzilla ticket.
2) The ticket status is changed to IN PROGRESS

Currently the **Mentors** of the experiments are the following
• SURROGATES (using Aveiro testbed) – Mentors: Miguel Luis <nmal@av.it.pt>
• CAVICO (using Aveiro testbed) – Mentors: Miguel Luis <nmal@av.it.pt>
• SFCLola (multisite experiment) – Mentors: Diogo Gomes <dgomes@av.it.pt>
• RobotView5G (using Bristol testbed) – Mentors: Aloizio Pereira da Silva <aloizio.eisenmann.dasilva@bristol.ac.uk>
• VRU-Safe (using Aveiro testbed) – Mentors: Miguel Luis <nmal@av.it.pt>

**Note: Changing Assignee is currently done only through Bugzilla** A suggestion is to manage the Deployment Request only through the portal. The portal automatically notifies and creates issues in Bugzilla. However, due to restrictions, Bugzilla could be used for more fine-grained control until the portal has all the features.

### OSM4
1) An experimenter creates a Deployment request through the portal. 
2) The experimenter selects the appropriate Mentor for the Deployment from the list
3) This triggers an automated New Issue in Bugzilla, Under 5GinFIRE Operations, Operations Support. 
4) 5GinFIRE team is also get notified via the tickets@ mailing list.R
5) The Experimenter is added also in the CC list of the issue.
6) The Mentor logs into the portal and inspects the Deployment Details

## The Mentor drives discussions

**The Mentor drives discussions**  between Mentor+5TONIC + Internal with VIM owners.
Also needs to:
+ Verifying that the requested experiment is deployable. This implies, at least: checking that all the components are onboarded; and checking that the VNFs can be executed in the involved testbeds (e.g.,  a VNF for an EPC should be executed in a testbed with radio equipment).
+ Coordinating with the testbed providers a specific time slot for the execution of the experiment. This time slot may be different from the time slot requested by the experimenter. In case that the time slot requested by the experimenter is not feasible, I would suggest that the experiment request should be rejected, with an indication of a valid time slot(s) and the possibility to resubmit the experiment request in case that the alternative time slot(s) is adequate for the experimenter.
+ Currently in the portal there are Two admins that can manage deployments Christos and Ivan but there could be also the mentors (we can have also a new Role in portal=MENTOR). An admin can respond through the portal and change the status of the Deployment Request. Whatever change you do in the portal is reflected in Bugzilla. Of course you can go directly to Bugzilla. So for example: 
if it goes in portal= SCHEDULED in Bugzilla will go IN_PROGRESS. If goes in portal= REJECTED in Bugzilla will go to RESOLVED INVALID, , etc

## The Mentor gives green or red light
### OSM2
1) After discussions with ((Mentor+5TONIC + Internal with VIM owners )) The Mentor gives green (ACCEPT) or red light (REJECT) to admins, to change the status (e.g. SCHEDULED) and the scheduled deployment dates, or simply reject that (REJECTED).
2) The Mentor could optionally change Assignee (e.g. an admin) or we can discuss to introduce a new Component (e.g. DeploymentCalendar)
####  Deployment Status
1) If the Experiment Deployment Request has SCHEDULED status then the OSM team should be aware for the date of orchestration,deployment and tear down
2) When it is orchestrated the Experiment Deployment Requestgoes to RUNNING
3) When it is tear down the Experiment Deployment Requestgoes to COMPLETED

At any stage The portal has a Feedback text form to write text that also is copied to the experimenter and the ticket

### OSM4
1) After discussions with ((Mentor+5TONIC + Internal with VIM owners )) The Mentor gives green (ACCEPT) by selecting the SCHEDULED option in the portal or red light (REJECT) by selecting the REJECT option in the portal. The portal administrators, the Mentor and the experimenter are notified for the Deployment Status change through the Bugzilla ticket update and the related email message.
2) The Deployment is automatically Instantiated at the required Initiation Date. 
			-If the instantiation FAILS the status of the Deployment changes to REJECTED. The related Bugzilla ticket is changed and the users are notified through email.
			-If the instantiation is SUCCESSFUL the status of the Deployment changes to RUNNING. The related Bugzilla ticket is changed and the users are notified through email.
3) The Deployment is automatically TERMINATED at the required Termination Date. The status of the Deployment changes to COMPLETED. The related Bugzilla ticket is changed and the users are notified through email.