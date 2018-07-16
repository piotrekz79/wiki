<!-- TITLE: The 5GinFIRE Mirror Platform -->
<!-- SUBTITLE: The 5Ginfire Mirror Platform -->

# The 5GinFIRE Mirror Platform
To enable experimenters and developers to carry out a first validation of their Network Services (NS) and Virtualized Network & Vertical Functions (VxFs), 5GinFIRE provides a functional replica of the MANO platform currently in production state. This replica, referred to as the *mirror platform* in this page, provides platform users with access to an OSM installation that supports the following functionalities:

1) Onboarding of VxFs.
2) Onbloarding of NSes.
3) Access to OSM logs, to get information on any onboarding errors.

This way, the mirror platfom allows platform users to verify if a NS or VxF can be onboarded to OSM, before formally requesting onboarding of the component to the production MANO platform through the [5GinFIRE Portal](https://portal.5ginfire.eu). Its main purpose is to agilely detect errors in NS/VxF package specifications early in the experimentation process. This way, users can autonomously do a first validation test of their NS/VxF packages, making sure that they are compliant with OSM and can effectively be onboarded to the production OSM platform. This allows reducing potential interaction cycles and delays that would otherwise be necessary to set up an experiment witn new NS/VxFs, optimizing the experimentation process.

Please, when using the mirror platform, take into account the following considerations:

1) The mirror platform does not attach any VIM tenant, hence it cannot be used to test the deployment of a NS. Future versions of the mirror platform will consider the provision of functionalities related to the deployment of NSes, using a [VIM emulator solution](https://osm.etsi.org/wikipub/index.php/VIM_emulator).
2) The mirror platform may be restarted with certain periodicity, and data may be deleted for maintance purposes. Users are encouraged to not consider this as a stable platform to keep copies their of NS/VxFs.

## Preliminary steps

To access the mirror platform, you need to connect to the 5GinFIRE VPN. You can request VPN credentials to access the 5GinFIRE network infrastructure by creating a ticket to [5GinFIRE Operations] (https://portal.5ginfire.eu/bugzilla/enter_bug.cgi?product=5GinFIRE).

## Accesing the mirror platform
After obtaining VPN credentials and connecting to the VPN (a tutorial to connect to the 5GinFIRE VPN can be found [here](http://wiki.5ginfire.eu/tutorials/guide-external-access-experimenters)), you can access the Graphical User Interface of the mirror platform through this link:

- https://10.4.48.15:8443 (use of *Chrome*  is recommended)
	- User: *admin*
	- Password: *admin*

![Osmloginwindow](/uploads/mirror-site/osmloginwindow.png "Osmloginwindow"){.align-left}

## Onboarding a NS/VxF
The process to onboard a VNF is detailed in the [ETSI OSM Wiki](https://osm.etsi.org/wikipub/index.php/OSM_Release_TWO#Deploying_your_first_Network_Service). You just need to click on the *import* button of the *catalog* tab, select *VNFD* and indicate the VNF package file.

![Onboardingvnf](/uploads/mirror-site/onboardingvnf.png "Onboardingvnf"){.align-left}

A similar approach can be followed to import a NS package, selectgin *NSD* instead of VNFD.

## Accessing the logs
If the onboarding fails, you can access the OSM logs to get more information about the error. To do that, access via *ssh* to the mirror platform, i.e., using the IP address *10.4.48.15*. The login and password for the *ssh* are the following:

- Login: 5ginfire
- Password: 5ginfire

After connecting to the machine...

OSM Release TWO includes  Service Orchestrator (SO), a Resource Orchestrator (RO) and NFV Configuration and Abstraction (VCA) module. Each of these components is execTo get information on the specific failure produced by the onboarding attemp, you will need to access the SO and the RO logs.

The SO logs are available at the SO-ub contained, at the followinf location:

``/var/log/rift/rift.log``

The RO logs can be found at the RO container, in the file :

``lxc file pull RO/var/log/osm/openmano.log .``

``lxc file pull RO/var/log/osm/openmano.log .``
