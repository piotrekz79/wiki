<!-- TITLE: Example: deployment of VoD service at 5TONIC -->

# Overview of the experiment
As an example of an experiment that can be carried out over the 5TONIC infrastructure, in the following we the describe the process followeed to deploy a Video-on-Demand (VoD) service, and we validate is appropriate operation. The Network Service (NS) of the experiment is illustrated in the figure below.

![Vod Ns](/uploads/5-tonic/vod-ns.png "Vod Ns")

The NS includes an HTTP server function (HTTP server VNF), which maintains a number of video files that can be requested on-demand by interested users using the HTTP protocol (i.e., a common approach used by existing video-on-demand services such as YouTube). A router function (Router VNF) supports the exchange of HTTP traffic between the server and remote network locations where video requests are originated. One of such locations is represented by a residential gateway function (Residential GW VNF), allowing a user terminal to: 

1) Obtain IP access connectivity; 
2) Request a video file from the HTTP server, which is then streamed to the user terminal. 

Additionally, the residential gateway hosts a DHCP server that supports the automatic network configuration of the user equipment. 

The NS and the VNFs have been made available in the 5GinFIRE portal, under an open source license.

# Deployment of the experiment
Regarding the deployment of the NS, the diverse VNFs that conformy it can be deployed at 5TONIC, or the deployment can be distributed across different sites. In particular, in [1] we presented the results of a distributed deployment of this NS, where the HTTP server and the router function were deployed at 5TONIC, while the residential gateway function was deployed at a site made available at UC3M. In the experiment, day-1 configuration of VNFs (configuration of static IP addresses, activation of  IP forwarding in the router and the residential gateway, and start of HTTP and DHCP services) was executed with Ansible playbooks, using a base charm layer developed within 5GinFIRE that has been contributed to the OSM community. The configuration operations per VNF, and the virtual resources allocated to each virtual machine, are summarized in the figure, and are specified in the corresponding VND descriptors.

# Collection of results
In the experiment, after the deployment and configuration of the VNFs, a user device (a commodity laptop) was connected to the NFV infrastructure where the residential gateway was instantiated, obtaining access connectivity to the deployment. After the laptop’s interaction with the DHCP server, and completion of its network configuration, we used GStreamer to request and play a specific video file from the HTTP server. The figure below represents the TCP throughput of the video delivery corresponding to the experiment, measured at the user equipment. 

![Vodthroughput](/uploads/5-tonic/vodthroughput.png "Vodthroughput")

The video file was received with an average rate of 4.44 Mbits/s, being uninterruptedly played out as it was received from the HTTP server. An analogous execution of the service, using a physical machine to deploy the HTTP server, and connected to the user equipment through a switch, provided similar throughput (also shown in the figure).
