<!-- Example: Software Defined Radio Slices with HyDRA Experiment -->
<!-- SUBTITLE: Software Defined Radio Slices with HyDRA Experiment -->

# Overview
WINS_5G, the reconfigurable radio testbed at Trinity College Dublin, provides virtualized radio hardware, software virtualisation, Cloud-RAN, Network Functions Virtualisation (NFV), and Software Defined Networking technologies to support the experimental investigation of the interplay between 5G radio and future networks. This 5GINFIRE testbed adds the capability to instantiate network function virtualisation (NFV) experimental vertical instances (EVIs) to the radio access network supported by the radio slicing and virtualisation layer called Hypervisor for Software Defined Radios (HyDRA), developed by Trinity College Dublin researchers. This experiment, which can be carried out using the WINS_5G infrastructure supported by deployed HyDRA As A Service (HyDRA-AAS) Network Service Descriptor (NSD) and Virtual Network Function Descriptor (VNFD), will describe the process of deploying and experimenting with 5G radio slices. The HyDRA-AAS NSD and VNFD used in this experiment are available from the 5GINFIRE Market place. WINS_5G is ideally equipped to investigate the combination of network slicing, virtualisation functions, and physical layer approaches into coexisting and coherent next-generation commercial networks, including, but not limited to, 5G.



# System Architecture – The Baseline WINS_5G Radio Slicing EVI
The baseline WINS_5G EVI contains the following elements: 
1. two radio access technologies sharing the same physical device, 
2. HyDRA-AAS to slice the physical radio device into the two radios, and 
3. two receiver devices (one for each radio slice).

To this end, we have built the baseline WINS_5G EVI comprising a total of 4 VNFs, as follows:
* 1 x VNF that implements the two radio access technologies in two independent GNURadio processes (named EVI1 and EVI2);
* 1 x  VNF implementing HyDRA-AAS; 
* 1 x  VNF to receive signal from EVI1;
* 1 x  VNF to receive signal from EVI2.

The four VNF and their interaction are shown in Figure 1. The Client VNF implements the baseband processing for EVI1 and EVI2. This VNF is connected to the HyDRA VNF, which runs the HyDRA-AAS Server as described earlier in Section 1. HyDRA VNF interacts directly with a USRP device to transmit the multiplexed signal of EVI1 and EVI2. Finally, the two VNFs, named EVI1 RX and EVI2 RX, receive the data for their corresponding EVI. Each one of these VNF is connected to a USRP for signal reception. 


![Hydra Experiment](/uploads/hydra-experiment.png "Hydra Experiment")
### Figure 1 5G Radio Slicing EVI Experiment supported by HyDRA - four VNFs and their interaction



# System Architecture
