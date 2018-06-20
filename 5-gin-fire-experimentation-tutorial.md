<!-- TITLE: 5GinFire Experimentation Tutorial -->

# Experimenting with 5GinFIRE infrastructure 
The following is a list of steps that experimenters can follow to deploy experiments on top of 5GinFIRE Infrastructure.
The whole experimentation process is described in http://wiki.5ginfire.eu/5-gin-fire-terminology-experimentation-workflow-and-architecture

## 1. Select your target testbed(s)
Select your target testbeds to deploy ypour experiment. Please consult the link http://wiki.5ginfire.eu/5GinFIREtestbeds
There is also the solution called Unifier Gateway http://wiki.5ginfire.eu/unifiergateway

### Apply for experiment
Currently this can be done through Open Calls or by expressing your interest to Contact https://5ginfire.eu/contact/


## 2. Select or Create your VNFs
Either you browse the puvlic VNF catalog at https://portal.5ginfire.eu/#!/vxf_marketplace or you create your own VNFs.
For creating VNFs compliant with OSM TWO see our tutorials in main page: http://wiki.5ginfire.eu/

## 3. Deploy your VNFs

### Portal uploading
When you have prepared your VNFs you need to upload them to the portal. You need first to open an account to the portal. https://portal.5ginfire.eu 
By default when you open an account you will have the roles of "EXPERIMENTER" and "VXF_DEVELOPER".
Please check the portal user guide: http://wiki.5ginfire.eu/5-gin-fire-portal-user-guide
For VNF uploading: http://wiki.5ginfire.eu/5-gin-fire-portal-user-guide#vx-f-developer-user-interface-description

### VNF validation 

After you have submitted your VNF(s) they will be validated by the 5GinFIRE operations.
You will be notified if your VNF is valid in terms of:
- VNF Packaging for target OSM version (Currently TWO but we are moving to FOUR)
- Onboarding capability
- Deployment capability

### VNF onboarding

If your VNF is valid, it will be onboarded to OSM. 

**At this stage your VNF is available to be included in experiments described as NSDs**

## 4.  Select or Create your NSDs


NSD  validation 
NSD onboarding

## 5. Request VPN Credentials

Report at 5GinFIRE Operations: https://portal.5ginfire.eu/bugzilla/enter_bug.cgi?product=5GinFIRE%20Operations that you want VPN credentials

## 6. Make a deployment request

## Support

### Experiment Support
We use Bugzilla for reporting issues regarding your experiment. Please see: https://portal.5ginfire.eu/bugzilla/describecomponents.cgi?product=Experiments 
Prerequisite:  You need to open an account in Bugzilla. If your experiment is accepted there will be a separate component for your experiment.

### Generic Operations support
For generic support issues please report at 5GinFIRE Operations: https://portal.5ginfire.eu/bugzilla/enter_bug.cgi?product=5GinFIRE%20Operations
5GinFIRE Slack channel - Contact us to invite you at https://5ginfire.slack.com/
