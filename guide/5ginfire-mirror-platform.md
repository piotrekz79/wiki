<!-- TITLE: The 5GinFIRE Mirror Platform -->
<!-- SUBTITLE: The 5Ginfire Mirror Platform -->

# The 5GinFIRE Mirror Platform
To enable experimenters and developers to carry out a first validation of their Network Services (NS) and Virtualized Network & Vertical Functions (VxFs), 5GinFIRE provides a functional replica of the MANO platform currently in production state. This replica, referred to as the *mirror platform* in this page, provides platform users with access to an OSM installation that supports the following functionalities:

1) Onboarding of VxFs.
2) Onboarding of NSes.
3) Access to OSM logs, to get information on any onboarding errors.

This way, the mirror platform allows platform users to verify if a NS or VxF can be onboarded to OSM, before formally requesting the onboarding of the component to the production MANO platform through the [5GinFIRE Portal](https://portal.5ginfire.eu). Its main purpose is to agilely detect errors in NS/VxF package specifications early in the experimentation process. This way, users can autonomously do a preliminary validation of their NS/VxF packages, making sure that they are compliant with the OSM software and can effectively be onboarded to the production OSM platform. This allows reducing potential interaction cycles and delays that would otherwise be necessary to set up an experiment with new NS/VxFs, optimizing the experimentation process.

When using the mirror platform, take into account the following considerations:

1) The mirror platform does not attach any VIM tenant, hence it cannot be used to test the deployment of a NS. Future versions of the platform will consider the provision of functionalities related to the deployment of NSes, using a [VIM emulator solution](https://osm.etsi.org/wikipub/index.php/VIM_emulator).
2) The mirror platform may be restarted with certain periodicity, and data may be deleted for maintenance purposes. Users are encouraged to not consider this as a stable platform to keep copies of their NS/VxFs.

## Preliminary steps
To access the mirror platform, you need to connect to the 5GinFIRE VPN. You can request VPN credentials to access the 5GinFIRE network infrastructure by creating a ticket to [5GinFIRE Operations] (https://portal.5ginfire.eu/bugzilla/enter_bug.cgi?product=5GinFIRE).

## Accessing the mirror platform
After obtaining VPN credentials and connecting to the VPN (a tutorial to connect to the 5GinFIRE VPN can be found [here](http://wiki.5ginfire.eu/tutorials/guide-external-access-experimenters)), you can access the Graphical User Interface (GUI) of the mirror platform through this link:

- https://10.4.48.15:8443 (using *Chrome*  is recommended)
	- User: *admin*
	- Password: *admin*

![Osmloginwindow](/uploads/mirror-site/osmloginwindow.png "Osmloginwindow"){.align-left}

## Onboarding a NS/VxF
The process to onboard a VNF is detailed in the [ETSI OSM Wiki](https://osm.etsi.org/wikipub/index.php/OSM_Release_TWO#Deploying_your_first_Network_Service). You just need to click on the *import* button of the *catalog* tab, select *VNFD*, and indicate the VNF package file.

![Onboardingvnf](/uploads/mirror-site/onboardingvnf.png "Onboardingvnf"){.align-left}

A similar approach can be followed to import a NS package, selecting *NSD* instead of *VNFD*.

## Accessing the logs
If the onboarding fails, you can access the OSM logs to get more information about the error. To do that, access via *ssh* to the mirror platform, i.e., using the IP address *10.4.48.15*. The login and password for the *ssh* are the following:

- Login: 5ginfire
- Password: 5ginfire

``> ssh 5ginfire@10.4.48.15``

OSM Release TWO includes three main components: a Service Orchestrator (SO), a Resource Orchestrator (RO), and VNF Configuration and Abstraction (VCA) module. Each of these components is executed in a Linux container. You can see the information regarding these containers with the following command:

``> lxc list``

![Screen Shot 2018 07 16 At 17 17 55](/uploads/mirror-site/screen-shot-2018-07-16-at-17-17-55.png "Screen Shot 2018 07 16 At 17 17 55")

To get information on the specific failure produced by the onboarding attempt, you will need to access the SO and the RO logs.

The SO logs are available at the SO-ub container, at the following location: */var/log/rift/rift.log*. The file can be obtained from the host using the following command:

``> lxc file pull SO-ub/var/log/rift/rift.log``

The RO logs can be found at the RO container, in the file */var/log/osm/openmano.log*. You can get this file from the host with the following command:

``> lxc file pull RO/var/log/osm/openmano.log .``

