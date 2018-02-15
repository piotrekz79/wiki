<!-- TITLE: 1st 5GinFIRE Open Call FAQs -->
<!-- SUBTITLE: FAQs -->

# 1st 5GinFIRE Open Call FAQs

* **Is there any Available documentation?**

Please have a look at Deliverables at https://5ginfire.eu/deliverables/ and at this wiki http://wiki.5ginfire.eu

* **Is there any Testbed/Tools documentation?**

Please have a look at the following links:
1. The 5GinFIRE orchestration service and the NFV infrastructure at 5TONIC testbed (https://5ginfire.eu/5tonic/)
2. Experimenter Tools (https://5ginfire.eu/facilities-2/)
3. IT-Av automotive testbed (https://5ginfire.eu/it-av-automotive-testbed/)
4. Smart city safety testbed: https://5ginfire.eu/smart-city-safety/
 

* **Is the core network (i.e. Unified GW) provided as a functionality of the system and deployable through OSM?**

***[WP5 TBC]***

* **Is it a hard limitation "Before  awarding any grants to a third party, it will  be  checked whether the  third party is a legal entity with a history of at least three years of commercial operations, and has not been declared insolvent." ?**

YES

* **Which OSM version should be considered, TWO or THREE?**
Current infrastructure is based on OSM Release TWO, and the team is working on migrating to OSM Release THREE. We foresee two possible scenarios:
1) OSM Release TWO as production orchestrator and OSM Release THREE as an experimental one
2) Only OSM Release THREE as production and experimental orchestrator
In general, we think it is advisable to assume OSM Release TWO for experiments under item (1) in the open call, as they would be migrated to OSM Release THREE as required, and OSM Release THREE for items (2a) and (2b) in the open call, as new features will be incorporated for further 5GINFIRE releases.


* **How is the experiment lifecycle working? Will the experimenter be allowed to access directly the OSM launchpad/APIs, or the only interaction allowed is via the 5GinFIRE portal?**

Please check the wiki http://wiki.5ginfire.eu/#the-5-gin-fire-architecture-technologies-services-and-testbeds. Normally the access will be only through the portal.

* **Considering that we would like to instantiate multiple slices, are we allowed to execute them in parallel?**

***[WP4/WP5 TBC]*** This depends on resources, but normally you should be able to do that

* **Is there a multi-site federated infrastructure, or the different testbeds are seen as individual sites? In the last case, where should be specified the site for deployment?**



***[WP4 TBC]*** 5GinFIRE has available interconnected multiple VIMs under OSM. Any site or multi-sites can be selected for deployment 

* **Is inter-VNF communication based on classical virtual networking like in OpenStack?**

***[WP4 TBC]***

* **Is OpenStack the VIM/NFVI used in the sites? Which version specifically?**

***[WP4 TBC]*** YES. Openstack Mitaca 

* **Are we allowed to upload specific images on the VIM/NFVI while implementing VNFs?**

***[WP4 TBC]*** YES

* **Will the experimenter get access (i.e. SSH) to the deployed instances? If yes, how? Via VPN or public IPs?** 

***[WP4 TBC]***  Yes via SSH and VPN

* **In case of VPN, are there some firewall rules?**

***[WP4 TBC]***

* **Will you accept proposals with potential modifications to the OSM tool? If yes, which version should be considered, TWO or THREE?**

***[WP4 TBC]*** YES this falls under category 2a. for version see answer above

* **Will you accept proposals with potential modifications/extensions to the 5GinFIRE portal?**

YES this falls under category 2a

* **How are those extensions supposed to be integrated? Should we consider potential modifications to the components, or should we only use APIs (hopefully with SDKs you may provide)?** 

They can be either services or APIs usage, APIs extensions or modifications. Proposers are free to define

* **In case of extensions based on APIs, are you providing an API description which we could consider for our initial solution design? Please let us know also about any restrictions due to any RBAC mechanism you utilise.** 

    * Regarding the Portal there is an API. Please check the http://wiki.5ginfire.eu/portalarchitecturedesign/portal-api section
    * Regarding OSM there are the ETSI NFV APIs specified and the correspponding OSM version to support


* **Currently we have only noticed that the experiment lifecycle mainly deals with category 1 types of experiment, therefore it is not clear how those potential extensions could be realised and be deployed on demand on top of your platform.**

The extensions can be deployed as services or they can reuse existing APIs (Portal, OSM). Proposers, though, are free to define the deployment they need

* **Will some support be provided about the description files definition?**

Please check this Wiki. The descriptors are standardized in format and packaging by ETSI specifications





