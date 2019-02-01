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

# Recreating the Experiment
By launching the HyDRA-AAS NSD and VNFD services, the experiment will automatically be setup, configured, and started.
# HyDRA-AAS: The Client for Radio Resource Management Functions
We implemented a Radio Resource Management Functions (RRMF) in HyDRA-AAS to support EVI assess to available physical radio resources and to request the creation of new vRF front-ends. Descriptions and examples of HyDRA RRMF are shown below. Experimenters can send a JSON request to the HyDRA-AAS server on port 5000 (default). 

**RRMF name**: **check_connection**
**Description**: Check if the HyDRA-AAS server is up and running. If yes, HyDRA-AAS will reply, otherwise the message will timeout.	

```text
Example JSON
{"xvl_syn":""}
```

**RRMF name**: **query_resources**
**Description**: Returns a list of tuples in the form (CF, BW) of all portions of radio spectrum available to use by HyDRA. Note: this portions can be in use by external radio access technologies.	
```text
Example JSON
{"xvl_que":""}
```

**RRMF name**: **free_resources	**	
**Description: **Free all radio resources used by the client. 
```text
Example JSON
{"xvl_fre": {
   "id": + u_id
   }
}

```


**RRMF name**: **request_tx_resources	**
**Description**: Creates a new vRF front-end and virtual network interface. This slices the physical USRP with a new vRF front-end with TX only capabilities. The virtual network interface is used to provide HyDRA-AAS functionalities.	
```text
Example JSON
{"xvl_rtx":
  {"id": + u_id,
   "centre_freq:" + d_centre_freq,
   "padding:" + bpad,
   "bandwidth:" + d_bandwidth
   }
}
```

**RRMF name**: **request_rx_resources		**
**Description**: Creates a new vRF front-end and virtual network interface. This slices the physical USRP with a new vRF front-end with TX only capabilities. The virtual network interface is used to provide HyDRA-AAS functionalities.	
```text
Example JSON
{"xvl_rrx":
  {"id": + u_id,
   "centre_freq:" + d_centre_freq,
   "padding:" + bpad,
   "bandwidth:" + d_bandwidth
   }
}
```

The type of data presented in the JSON column is as follows:

* u_id: integer. Identifies the ID of the client. Each client connected to a HyDRA-AAS has a unique ID starting from 1.
* d_centre_freq: double. The centre frequency in which the virtual RF front-end will operate. Valid values should be in the list of tuples obtained from query_resources. For each tuple, a valid value is between CF-BW/2 and CF+BW/2.
* d_bandwidth: The bandwidth in which the virtual RF front-end will operate. Valid values should be in the list of tuples obtained from query_resources. For each tuple, a valid value is equal or less than BW.
* bpad: boolean. If HyDRA-AAS should add padding samples for the TX buffers. Advanced configuration. The default is False.

Operations to change the resources in real time, such as changing the center frequency or the bandwidth, can be accomplished simply the performing a request_tx_resources or request_rx_resources with the new configuration wanted and the same id. 

# HyDRA Client Library 
We developed a client library that implements all the RRMF with the objective of facilitating the development of SDR radios by the EVIs. This library abstracts the client-server communication as a set of functions calls that generate the JSON request, send it to the HyDRA-AAS server. The client library is installed in all HyDRA-AAS VM's as a C/C++ library.

To use the library, experiments can use any of the HyDRA-AAS VNFs or VMs available in the WINS_5G testbed or install it manually.  Given that HyDRA-AAS is installed, developers can have access to the client library API by adding the following include to their C/C++ code:

#include "hydra/hydra_client.h"

## Implementation of Radio Resource Management Functions
This include gives access to the hydra_client class, which implements all the RRMF described previously. The definition of the class is as follows: 

```text

hydra_client(/* IP of the client VM connecting to HyDRA server */
             std::string client_ip = "localhost",     
             /* IP of the HyDRA server */
             std::string server_ip = "localhost",
             /* Port HyDRA server is running. 5000 by default */
             unsigned int u_port = 5000,
             /* Client ID. Must be unique */
             unsigned int u_client_id = 10,
             /* Print debug messages */
             bool b_debug = false);
```


This class implements the RRM functions as follows. The reader can refer to Table 1 for a description of the RRMFs.


```text
int request_rx_resources(/* Central frequency */
                         double d_centre_freq,
                         /* Bandwidth */
                         double d_bandwidth,
                         /* Advanced option. */
                         bool bpad = false);
												 
int request_tx_resources(/* Central frequency */
                         double d_centre_freq,
                         /* Bandwidth */
                         double d_bandwidth,
                         /* Advanced option */
                         bool bpad = false);
												 
/* Check if HyDRA-AAS is running */
std::string check_connection();
/* Query the available resources */
std::string query_resources();
/* Free resources */
std::string free_resources();
```

## 	Example Application
Below we provide a C++ example application that uses all the RRMF resource functions. This source code is located in all HyDRA-AAS VMs/VNFs in the directory /home/ubuntu/gr-hydra/app/client.cc, whereas the executable (binary) version can be found in /home/ubuntu/gr-hydra/build/app/client.

```text

#include "hydra/hydra_client.h"
#include <iostream>
int main()
{
  double cf_tx = 1.1e9; // Central frequency for transmission
  double cf_rx = 1.2e9; // Central frequency for reception


  /* Instantiate the HyDRA client */
  hydra::hydra_client s1 = hydra::hydra_client("127.0.0.1", "127.0.0.1", 5000, 90, true);
  
  /* Check connection */
  std::cout << s1.check_connection() << std::endl;

  /* Query TX and RX resources */
  std::cout << s1.query_resources() << std::endl;

  /* Request RX resources. Parameters are: cf, bandwidth, bpad */
  std::cout << s1.request_tx_resources(cf_tx + 200e3, 200e3, false) << std::endl;
  std::cout << s1.request_rx_resources(cf_rx + 200e3, 200e3, false) << std::endl;


  /* Free resources from a given service */
  std::cout <<  s1.free_resources() << std::endl;

  std::cout << "Press CTRL-C to quit" << std::endl;
  while (1) usleep(1000);

  return 0;
}
```


To compile the example above, you should use the following command in a terminal:

g++ filename.cpp -lhydra -o client

where filename.cpp is the name of the file with the code shown above. This will create a binary file named client. To execute it type:

./client

The output of executing the client should look as follows if HyDRA-AAS is running (in this example in the localhost, otherwise you need to change the server_ip parameter when creating the hydra_client instance). For the sake of simplicity, we included only the first lines. Moreover, only the first line is shown if HyDRA-AAS is not running.

```text
Connecting to XVL server...
Sending:	{"xvl_syn":""}
{
    "xvl_ack": {
        "status": "true",
        "message": {
            "condition": "Enabled",
            "name": "XVL Hypervisor Server",
            "version": "0.1"
        }
    }
}
```



