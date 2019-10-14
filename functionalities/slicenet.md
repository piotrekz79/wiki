<!-- TITLE: Slicenet -->
<!-- SUBTITLE: Slicenet-5G -->

# Slicenet-5G 

Slicenet-5G offers to experimenters an SDN-managed network slice, which allows them to flexibly deploy their service infrastructures. The SDN solution offered by the functionality facilitates the dynamic connectivity in the slice of the application software components in a flexible and scalable way.

More specifically, an experimenter may want to dynamically establish service chains among different applications service components. The Slicenet-5G functionality offers him an automated and programmable way to configure and control the SDN capabilities within the network slice (i.e., data plane forwarding rules of SDN switches).

Our reference use case consists of multiple Vertical Applications (VAs) (e.g., video transcoder, face detection, face recognition) and/or Virtual Network Functions (VNFs) (e.g., firewall, NAT, DPI, load balancer) deployed and connected to each others through a SDN-based network. 





In the following, as an example, we will consider two VAs connected through a SDN network. To do so, we build a NSD and two different VNFDs that allow for a network slice to be deployed with: (i) one VNF running SDN components (i.e., an SDN controller connected to one or more OpenFlow switches) connecting (ii) other two VNFs supposed to run different application software modules.

We rely on cloud-init for the configuration of the VNFs by directly bringing the configuration scripts within the VNFDs. 

## Running an experiment

The experiment starts by requiring the NS set-up by sending a request to OSM for onboarding the VNFD and NSD descriptors. Once the descriptors are validated, the NS deployment request is submitted to the target VIM. The VIM creates the necessary VMs (three in this example) according to the requirements specified in the descriptors. Once the VMs are instantiated, through cloud-init, the configuration scripts are executed and the configurations carried out. 
 
Figure. 2 Slicenet-5G Network Service graph example

Initially, the three VMs are based on a simple Ubuntu image with three network interfaces as specified in the NSD (1 for management and 2 for data plane). Then, the following software is installed to create the slice:
-	VM1 and VM3: iperf package to be able to send/receive traffic once the configuration is done
-	VM2: SDN controller (i.e., ONOS), emulated topology (set of OvS switches created using the Mininet tool)

Once the 3 VMs are completely configured, we need a further step to connect VM1 and VM2 to the OvS switches of VM3. This step is carried out by hand (using VXLANs) since it necessitates the knowledge of the VMs IP addresses which are assigned dynamically by the VIM and cannot be known a priori.

After this configuration step, the traffic can flow from VM1 to VM3 through the SDN network established in VM2. 

A possible experiment using our functionality might consist in the following steps: 
(i)	Deploy the slice using the VNFDs/NSD provided on the portal
(ii)	automatically install different application software modules in a set of VNFs (by only modifying the cloud-init scripts in the VNFDs). This step is not mandatory and if the experimenter wishes, he/she can use the provided VNFDs without any modification.
(iii)	connect the VNFs to the SDN network: this step is performed after connecting to the VNFs machines over SSH by establishing VXLAN tunnels between the OvS switches in the VM hosting the SDN components and one data plane interface of the VNF that he/she wants to connect.
(iv)	compose different service chaining paths (e.g., by creating a set of intents between the VNFs ids using the SDN controller already running)
(v)	assess the performance of the service chains or the applications running on the different VNFs according to the specific scenario of the experiment.
