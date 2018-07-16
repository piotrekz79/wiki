<!-- TITLE: The 5GinFIRE Mirror Platform -->
<!-- SUBTITLE: The 5Ginfire Mirror Platform -->

# The 5GinFIRE Mirror Platform
To enable experimenters and developers to carry out a first validation of their Network Services (NS) and Virtualized Network & Vertical Functions (VxFs), 5GinFIRE provides a functional replica of the MANO platform currently in production state. This replica, referred to as the *mirror platform* in this page, provides platform users with access to an OSM installation that supports the following functionalities:

1) Onboarding of VxFs.
2) Onbloarding of NSes.
3) Access to OSM logs, to get information on any onboarding errors.

This way, the mirror platfom allows platform users to verify if a NS or VxF can be onboarded to OSM, before formally requesting onboarding of the component to the production MANO platform through the [5GinFIRE Portal](https://portal.5ginfire.eu). The mirror platform does not attach any VIM tenant, hence it cannot be used to test the deployment of a NS. Its main purpose is to enable platform users to agilely detect errors in their NS/VxF package specifications early in the experimentation process. This way, users can autonomously do a first validation test of their NS/VxF packages, making sure that they are free of sintax errors and can effectively be onboarded to the production platform. This allows reducing the required interaction cycles and potential delays that would otherwise be neccesary to start an experiment witn new NS/VxFs, helping to optimize the experimentation process.

Future versions of the mirror platform will consider the provision of functionalities related to the deployment of NSes, using a [VIM emulator solution](https://osm.etsi.org/wikipub/index.php/VIM_emulator).


