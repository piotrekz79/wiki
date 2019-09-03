<!-- TITLE: FB5G experiment -->
<!-- SUBTITLE: Three different Network Functions on top of Flowblaze: a programmable software switch based on DPDK -->

The aim of FB5G is to test, validate and assess in the 5GinFIRE testbed the performance of FlowBlaze, a novel stateful programmable dataplane engine that can simplify network functions (NF) design and implementation, while providing high performance packet forwarding, and support for future hardware offloading to SmartNICs. FlowBlaze is an abstraction that can be implemented in an efficient DPDK-accelerated software engine, conceived to rapidly design and deploy complex network functions hiding the complexity of software optimizations associated to the development of network functions. 

In the following, we will give a brief example on how to run three network function on top of FlowBlaze.

# Prepare and access the VNFs

Download the required VNFs (dpdkhost_vnf, dpdkhost2_vnf, flowblaze_vnf) and NS (flowblaze_ns) from the public 5GinFIRE public repository and deploy the experiment as the usual 5GinFIRE procedure. 
Once the experiment is run, access the deployed VMs with the following credentials:
	user: axbryd
	pass: axbryd


NOTE: Since the descriptors use the PCI-passthrough EPA feature of OSM and the NIC PCI addresses are hardcoded, a modification to the descriptor may be required.

# Run the experiments

The image contains installed and ready-to-use required software to run the experiments. 
If needed, to compile and build the FlowBlaze DPDK software application, simply run:

```text
cd flowblaze
make clean && make
```

# Load Balancer

In this use case, we implement a load balancer function that assigns TCP connections to a set of web servers in a private LAN, in a round-robin fashion. 

To setup the Load Balancing network function the steps are the following:
1.	Compile the load_balancing.xl file by issuing the command
```text
java -jar xlc.jar -i load_balancing.xl -o 
load_balancer.json
```
2.	Launch the FlowBlaze binary in the FlowBlaze VM, for example:
```text
./build/flowblaze -m 128 -l 1 -w 03:00.0 -w 03:00.1 -- -f 
load_balancer.json
```

3.	On the DPDK host 1, that we use as traffic generator, start replaying a trace with moongen:
```text
./moongen/build/MoonGen replay_pcap.lua 0 [trace.pcap] -l
```
4.	On the DPDK host 2, used as receiving host, start a packet counter, for example:
```text
./moongen/build/MoonGen rx_packet_distribution.lua 0
```

# Traffic Policer

This use case implements a single rate token bucket with burst size B and token rate 1/Q, where Q is the token inter arrival time.

In a similar way to the Load Balancing network function, the setup process is the following:
1.	Compile the load_balancing.xl file by issuing the command
```text
$ java -jar xlc.jar -i traffic_policer.xl -o policer.json
```
2.	Launch the FlowBlaze binary in the FlowBlaze VM:
```text
$ ./build/flowblaze -m 128 -l 1 -w 03:00.0 -w 03:00.1 -- -f policer.json
```
3.	On the DPDK host 1, that we use as traffic generator, start replaying a trace with moongen:
```text
$ ./moongen/build/MoonGen replay_pcap.lua 0 [trace.pcap] -l
```
4.	On the DPDK host 2, used as receiving host, start a packet counter, for example:
```text
$ ./moongen/build/MoonGen rx_packet_distribution.lua 0
```

# Traffic Offloading Function

The proposed application is set into the context of a generic mobile metro network, in particular it handles the traffic between User Equipment (UE) and Service Gateway (SGW). The FlowBlaze stateful switch, which is running the application, can dynamically offload the traffic between UE and SGW redirecting it to a node closer to the user known as Mobile Edge Computing (MEC) cloud. The main issue for this solution is that the traffic in the core mobile network is usually encapsulated and in most deployments the encapsulation protocol is the GPRS Tunneling Protocol (GTP). GTP identifies a UE flow in a field of 32 bits named Tunnel Endpoint IDentifier (TEID) and in the mobile core network this field has a different value for each direction of the tunnel: UE to SGW and SGW to UE. This feature results in a challenging situation in which a middlebox in between UE and SGW cannot know a priori the return identifier (the tunnel from SGW to UE) associated to a connection initiated by a user. To overcome this issue, the proposed application generates an ICMP echo request directed to a generic node in the core for each new connection seen. When the reply is received, the FlowBlaze node can recognize the back and forth association of the specific UE connection. Once the connection state is stored, the application can dynamically decide to export some user traffic to the MEC, based on programmed policies, e.g. a given destination port or IP address. Moreover, FlowBlaze can perform NAT functionalities as required by the MEC networking configuration.

## Setup

1.	Compile the tof.xl file by issuing the command
```text
$ java -jar xlc.jar -i tof.xl -o tof.json
```
2.	Launch the FlowBlaze binary in the FlowBlaze VM:
```text
$ ./build/flowblaze -m 128 -l 1 -w 03:00.0 -w 03:00.1 --vdev=net_tap0 -- -f tof.json
```
		In this case, it is required to add the option –vdev=net_tap0 to create a DPDK enabled tap 
        Interface. It will be required to launch the python application emulating the ping responder.

3.	On the DPDK host 2, used as receiving host, start the ping responder (SGW):
```text
$ python3 echo_reply.py dtap0
```
4.	On the DPDK host 1, that we use as traffic generator, start the python program emulating the first packets of the flows that we would send to FlowBlaze. The program takes in input the interface from which the traffic has to be sent, and the number of flows to generate:
```text
$ python3 ue_req_gen.py ens9 10000
```
5.	As the python generator terminate the execution, we can bind the physical interfaces to the DPDK driver on both hosts:
```text
$ dpdk-devbind -u 00:09.0 && dpdk-devbind -b igb_uio 00:09.0
```
6.	On the DPDK host 1, that we use as traffic generator, start replaying a trace containing the same number of flows of step 4 with moongen:
```text
./moongen/build/MoonGen replay_pcap.lua 0 gtp10000flows.pcap -l
```
7.	On the DPDK host 2, used as receiving host (MEC), start a packet counter, for example:
```text
./moongen/build/MoonGen rx_packet_distribution.lua 0
```