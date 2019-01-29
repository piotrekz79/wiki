<!-- TITLE: Example: a Hello World Network Service -->

# Overview of the experiment
This experiment provides an example of a simple Network Service (NS) that can be deployed over any NFV infrastructure(s) of 5GinFIRE, using the OSM stack available at 5TONIC. The Network Service (NS) of the experiment is illustrated in the figure below.

![Hello World](/uploads/5-tonic/hello-world.png "Hello World")

The NS is composed of two VNFs that are interconnected through a data link. Each VNF has a control and a data interface (the latter provides data connectivity with the correspondant VNF), and is assumed to obtain an IP network address for each of its interfaces through DHCP. The VNFs do not provide any specific network functionality (they have been developed only for testing purposes), and do not require additional configuration through the Juju interface of the OSM stack. The NS and the VNFs (images and NFV descriptors) have been made available in the 5GinFIRE portal, under an open source license.

# Deployment of the experiment
The aforementioned NS can be deployed using the 5GinFIRE portal, and each of its constituent VNFs can be allocated to any site of 5GinFIRE. Hence, the Hello World NS can be a multi/single-site NS. The virtual resources allocated to each virtual machine are summarized in the figure, and are specified in the corresponding VND descriptors.

# Testing the NS
After the succesful deployment of the NS, the experimenter can access any of the VNFs, following the procedures and policies defined by 5GinFIREE (see [here](http://wiki.5ginfire.eu/tutorials/guide-external-access-experimenters). From the VNF, the experimenter can verify the availability of network connectivity with the other VNF:

``> ping -I <source-IP-address> <destination-IP-address>``

Where ``<source-IP-address>`` is the Ip address of the local VNF on its data interface; while ``<destination-IP-address>`` is the IP address of the other VNF on its data interface.

