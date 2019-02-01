<!-- TITLE: 5GinFire Experimentation Tutorial -->

# Experimenting with 5GinFIRE infrastructure 
The following is a list of steps that experimenters can follow to deploy experiments on top of 5GinFIRE Infrastructure.
The whole experimentation process is described in http://wiki.5ginfire.eu/5-gin-fire-terminology-experimentation-workflow-and-architecture

## 1. Select your target testbed(s)

Select your target testbeds to deploy ypour experiment. Please consult the link http://wiki.5ginfire.eu/5GinFIREtestbeds
There is also the solution called Unifier Gateway http://wiki.5ginfire.eu/unifiergateway

### Apply for experiment

Currently this can be done through Open Calls or by expressing your interest to Contact https://5ginfire.eu/contact/

## 2. Describe and upload your VNFs

Your VNF is described in terms of a Virtual Network Function Descriptor. Please see: http://wiki.5ginfire.eu/packagingvxfnsd

### Select or Create your VNFs

Either you browse the public VNF catalog at https://portal.5ginfire.eu/#!/vxf_marketplace or you create your own VNFs.
For creating VNFs  see our tutorials in main page: http://wiki.5ginfire.eu/
**Note**: Currently 5GinFIRE support VNFs packaged with archive format for OSM FOUR

IMPORTANT TIP: in 5GinFIRE, management and data planes are decoupled. Therefore, if you wish to be able to remotely access your VNFs while executing experiments, you need to incorporate an interface in the managament plane to your VMs. The process described in http://wiki.5ginfire.eu/tutorials/guide-external-access-experimenters makes use of such interfaces.

### Pre validation 

The VNF developer verifies that the VNF can be onboarded to [The 5GinFIRE "mirror platform"](guide/5ginfire-mirror-platform). If so, the developer can proceed with submitting the VNF. Otherwise, the developer should fix any error regarding the VNF packages or descriptors, until on-boarding is successful. VNF developers can request support from 5GinFIRE partners to address any issues regarding VNFs, e.g., through the mailing list, bugzilla, or the slack channel. The request will be visible to all partners working on infrastructures and services, such that anyone can provide support to the questions.

### Portal uploading

When you have prepared your VNFs you need to upload them to the portal. You need first to open an account to the portal. https://portal.5ginfire.eu 
By default when you open an account you will have the roles of "EXPERIMENTER" and "VXF_DEVELOPER".
Please check the portal user guide: http://wiki.5ginfire.eu/5-gin-fire-portal-user-guide
For VNF uploading: http://wiki.5ginfire.eu/5-gin-fire-portal-user-guide#vx-f-developer-user-interface-description

### VNF Image

The image of your VNF can be either a public URL (hosted for example on a public server, or you ftp server, etc ) or can be uploaded to the portal to Admin->Registered Images.
**Note:**The image that you use the it must be uploaded to your Experimentation Testbeds! You need to contact and coordinate with your Mentor for this action!


### VNF validation 

After you have submitted your VNF(s) they will be validated by the 5GinFIRE operations.
You will be notified if your VNF is valid in terms of:
- VNF Packaging for target OSM version (Currently TWO but we are moving to FOUR)
- Onboarding capability
- Deployment capability

### VNF onboarding

If your VNF is valid, it will be onboarded to OSM. 

**At this stage your VNF is available to be included in experiments described as NSDs**

## 3.  Describe and upload your NSD Experiment

### Select or Create your NSDs

Your experiment is described in terms of a Network Service Descriptor. Please see: http://wiki.5ginfire.eu/packagingvxfnsd

Either you browse the public NSD catalog at https://portal.5ginfire.eu/#!/experiments_marketplace or you create your own NSD.
For creating NSD compliant with OSM  see our tutorials in main page: http://wiki.5ginfire.eu/
**Note**: Currently 5GinFIRE support NSDs packaged with archive format for OSM FOUR

### Pre validation 

The NSD developer verifies that the NSD can be onboarded to [The 5GinFIRE "mirror platform"](guide/5ginfire-mirror-platform). If so, the developer can proceed with submitting the NSD. Otherwsie, the developer should fix any error regarding the NSD packages or descriptors, until on-boarding is successful. NSD developers can request support from 5GinFIRE partners to address any issues regarding NSD, e.g., through the mailing list, bugzilla, or the slack channel. The request will be visible to all partners working on infrastructures and services, such that anyone can provide support to the questions.

### Portal uploading

When you have prepared your NSD you need to upload them to the portal. You need first to open an account to the portal. https://portal.5ginfire.eu 
By default when you open an account you will have the roles of "EXPERIMENTER" and "VXF_DEVELOPER".
Please check the portal user guide: http://wiki.5ginfire.eu/5-gin-fire-portal-user-guide
For NSD uploading: http://wiki.5ginfire.eu/5-gin-fire-portal-user-guide#experimenter-user-interface-description

### NSD  validation 

After you have submitted your NSD it will be validated by the 5GinFIRE operations.
You will be notified if your NSD is valid in terms of:
- NSD Packaging for target OSM version (Currently TWO but we are moving to FOUR)
- Onboarding capability
- Deployment capability

### NSD onboarding

If your NSD is valid, it will be onboarded to OSM. 

**At this stage your NSD is available to be deployed as an experiment**


## 4. Make a deployment request

When everything is in place, through the portal make a Deployment request for your experiment. 
**The experimenter MUST select the appropriate Mentor (http://wiki.5ginfire.eu/internal-process/mentors) for the Deployment Request from the available list. Usually your Mentor is assigned by 5GinFIRE and is usually a testbed owner.**
See Request New Deployment : http://wiki.5ginfire.eu/5-gin-fire-portal-user-guide#experimenter-user-interface-description

When you make the request this triggers an automated New Issue in Bugzilla, Under 5GinFIRE Operations, Operations Support.
* 5GinFIRE team is also get notified via the tickets@ mailing list.
* The Experimenter is added also in the CC list of the issue.
* The Mentor logs into the portal and inspects the Deployment Details

###  Automated Deployment

If your Mentor accepts your experiment then it is marked as **SCHEDULED** or can be **REJECTED**
The experiment will be automatically deployed at the  date/time as defined by the Mentor and will be terminated at the end date.
The portal administrators, the Mentor and the experimenter are notified for the Deployment Status change through the Bugzilla ticket update and the related email message.

-If the instantiation FAILS the status of the Deployment changes to **REJECTED**. The related Bugzilla ticket is changed and the users are notified through email.
-If the instantiation is SUCCESSFUL the status of the Deployment changes to **RUNNING**. The related Bugzilla ticket is changed and the users are notified through email.
-The Deployment is automatically TERMINATED at the required Termination Date. The status of the Deployment changes to **COMPLETED**. The related Bugzilla ticket is changed and the users are notified through email.

###  Accessing deployed experiment: Request VPN Credentials

Report at 5GinFIRE Operations: https://portal.5ginfire.eu/bugzilla/enter_bug.cgi?product=5GinFIRE%20Operations that you want VPN credentials. 

###  Accessing deployed experiment: OpenVPN operations

Once you have your own credentials and OpenVPN config file, please follow instructions as included in http://wiki.5ginfire.eu/tutorials/guide-external-access-experimenters.

## Support

### Experiment Support

We use Bugzilla for reporting issues regarding your experiment. Please see: https://portal.5ginfire.eu/bugzilla/describecomponents.cgi?product=Experiments 
Prerequisite:  You need to open an account in Bugzilla. If your experiment is accepted there will be a separate component for your experiment.

### Generic Operations support

For generic support issues please report at 5GinFIRE Operations: https://portal.5ginfire.eu/bugzilla/enter_bug.cgi?product=5GinFIRE%20Operations
5GinFIRE Slack channel - Contact us to invite you at https://5ginfire.slack.com/
