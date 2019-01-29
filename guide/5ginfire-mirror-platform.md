<!-- TITLE: Tools for validation, prototyping, and testing -->
<!-- SUBTITLE: The Mirror Platform & the Local Toolset-->

# The 5GinFIRE Mirror Platform
To enable experimenters and developers to carry out a first validation of their Network Services (NS) and Virtualized Network & Vertical Functions (VxFs), 5GinFIRE provides a functional replica of the MANO platform currently in production state. This replica, referred to as the *mirror platform* in this page, provides platform users with access to an OSM installation that supports the following functionalities:

1) Onboarding of VxFs.
2) Onboarding of NSes.
3) Access to OSM logs, to get information on any onboarding errors.

This way, the mirror platform allows platform users to verify if a NS or VxF can be onboarded to OSM, before formally requesting the onboarding of the component to the production MANO platform through the [5GinFIRE Portal](https://portal.5ginfire.eu). Its main purpose is to agilely detect errors in NS/VxF package specifications early in the experimentation process. This way, users can autonomously do a preliminary validation of their NS/VxF packages, making sure that they are compliant with the OSM software and can effectively be onboarded to the production OSM platform. This allows reducing potential interaction cycles and delays that would otherwise be necessary to set up an experiment with new NS/VxFs, optimizing the experimentation process.

When using the mirror platform, please take into account the following considerations:

1) The mirror platform does not attach any VIM tenant, hence it cannot be used to test the deployment of a NS.
2) The mirror platform may be restarted with certain periodicity, and data may be deleted for maintenance purposes. Users are encouraged to not consider this as a stable platform to keep copies of their NS/VxFs.

## Preliminary steps
To access the mirror platform, you need to connect to the 5GinFIRE VPN. You can request VPN credentials to access the 5GinFIRE network infrastructure by creating a ticket to [5GinFIRE Operations] (https://portal.5ginfire.eu/bugzilla/).

## Accessing the mirror platform
After obtaining VPN credentials and connecting to the VPN (a tutorial to connect to the 5GinFIRE VPN can be found [here](http://wiki.5ginfire.eu/tutorials/guide-external-access-experimenters)), you can access the Graphical User Interface (GUI) of the mirror platform through this link:

- https://10.4.48.15:8443 (using *Chrome*  is recommended)
- User and password details to be provided on demand.

![Osm Lwb Ui Login](/uploads/5-tonic/osm-lwb-ui-login.png "Osm Lwb Ui Login"){.align-left}
Image extracted from the [ETSI OSM Wiki](https://osm.etsi.org/wikipub/index.php/OSM_Release_FOUR)

## Onboarding a NS/VxF
The process to onboard a VNF is detailed in the [ETSI OSM Wiki](https://osm.etsi.org/wikipub/index.php/OSM_Release_FOUR#Deploying_your_first_Network_Service). You just need to click on the *Onboard VNFD* button of the *VNF Packages* open list, and drag & drop the VNF package file.

![800 Px Vnfd Onboard R 4](/uploads/5-tonic/800-px-vnfd-onboard-r-4.png "800 Px Vnfd Onboard R 4")
Image extracted from the [ETSI OSM Wiki](https://osm.etsi.org/wikipub/index.php/OSM_Release_FOUR)

A similar approach can be followed to import a NS package, selecting *Onboard NSD* instead of *Onboard VNFD*.

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

``> lxc file pull SO-ub/var/log/rift/rift.log .``

The RO logs can be found at the RO container, in the file */var/log/osm/openmano.log*. You can get this file from the host with the following command:

``> lxc file pull RO/var/log/osm/openmano.log .``



# The local toolset
In addition to the mirror platform, 5GinFIRE partners have also prepared a local toolset that provides a complete and functional orchestration environment to support prototyping and testing. This toolset includes:

*	An installation of OSM Release FOUR
*	A VIM emulator solution, [Vim-emu](https://osm.etsi.org/wikipub/index.php/VIM_emulator).

The local toolset is provided as a single virtual machine, which can be downloaded by experimenters and other interested users from the 5GinFIRE website. With this toolset, experimenters may also test if a NS or VxF can be onboarded to OSM (and hence to the 5GinFIRE MANO system). 

On the other hand, Vim-emu is capable of emulating the functionality of a VIM and an NFVI, providing a network emulation framework and supporting the deployment of VNFs as Docker containers. This way, the local toolset also complements the functionalities of the 5GinFIRE Portal, providing a mechanism to assist experimenters in the prototyping and testing of NSes.