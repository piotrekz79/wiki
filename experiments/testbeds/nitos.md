<!-- TITLE: NITOS VNF examples-->
<!-- SUBTITLE: How to run the 5G-VINO provided VNFs in NITOS -->

# Overview
5G-VINO deals with the integration of the NITOS testbed with the rest of the 5GinFIRE facilities. In this section, we detail the provided VNFs and NSDs that can be deployed in NITOS and take advantage of the wireless technologies that exist in the testbed.


# VNFs with LTE connectivity (using the Commercial Off-The-Shelf Equipment)

For the LTE case, provisioning a VNF with such capabilities equals to providing a VNF with an extra networking interface that is bridged on the compute node with the physical interface connected to the LTE network of NITOS. The VNF that is deployed in the testbed, is using two different interfaces: one bridged to the management Ethernet network, used for accessing the VNF, and a second one equalling to an LTE link. Services running inside the VNFs, can take advantage of this link, to communicate with other VNFs connected to the LTE network, or run in a completely isolated manner from other LTE clients, through the slicing schemes that are applied in the network .


## VNFD for COTS LTE connection

The provided VNF has one network connection as a management connection running over the Ethernet network of NITOS, and a second connection to the NITOS LTE infrastructure. Some parameters are needed for the connection to the LTE network, including the LTE subscriber group which the VNF will belong to, the Access Point Name (APN) that the subscriber group will use, and parameters about the maximum Uplink and Downlink traffic that the VNF will use. Tools invoked from the NITOS VIM side automatically retrieve lower level parameters that are required for connecting the LTE network, such as the International Mobile Subscriber Identifier (IMSI). 
Upon receiving such a VNF Description, the VIM of the NITOS side turns on the LTE base station (if it is powered off), and registers the LTE UE of the compute node that will be used to the LTE EPC. Along with these parameters, the APN that is passed from the experimenter and the subscriber group are also registered to the NITOS EPC, whereas tools running on the compute node facilitate the connection of the UE to the LTE network, by issuing AT commands over the USB interface of the UE. Once the connection is established, the LTE interface of the compute node is attached to a bridge which is offering the connectivity to the VNF. The extra fields are currently passed through the description of the VNF.  

```text
 vnfd:vnfd-catalog:
  vnfd:
  - connection-point:
    - id: eth0
      name: eth0
      short-name: eth0
      type: VPORT
    - id: eth1
      name: eth1
      short-name: eth1
      type: VPORT
    description: A VNF consisting of 1 VDUs connected to an LTE VL
    id: lteUE-vnf
    logo: osm.png
    mgmt-interface:
      cp: eth0
    name: lteUE-vnf
    short-name: lteUE-vnf
    vdu:
    - cloud-init-file: cloud-config.txt
      count: '1'
**      description: type:Lte,virtual-apn:TEST_SS,dlambr:50000000,ulambr:50000000,qci:5,cluster-client:lte_client1,virtual-cluster:TEST_SS**
			id: lteUEVM
      image: ubuntu1404_cloud
      interface:
      - external-connection-point-ref: eth0
        name: eth0
        position: '1'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      - external-connection-point-ref: eth1
        name: eth1
        position: '2'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      name: lteUEVM
      vm-flavor:
        memory-mb: '4096'
        storage-gb: '5'
        vcpu-count: '4'
    version: '1.0'
```


The image that is loaded for this VNF is a generic Ubuntu 14.04 image, but can be configured to anything else from the experimenter. Please notice the bold line in the description field that allows the NITOS VIM take care of all the low level configuration settings for the LTE equipment in the testbed.

The respective NSD is the following:


```text

 nsd:nsd-catalog:
  nsd:
  - constituent-vnfd:
    - member-vnf-index: '1'
      vnfd-id-ref: lteUE-vnf
    description: NS with 1 VNFs connected by datanet and mgmtnet VLs
    id: lte-ns
    logo: osm.png
    name: lte-ns
    short-name: lte-ns
    version: '1.0'
    vld:
    - id: mgmtnet
      mgmt-network: 'true'
      name: mgmtnet
      short-name: mgmtnet
      type: ELAN
      vim-network-name: provider1
      vnfd-connection-point-ref:
      - member-vnf-index-ref: '1'
        vnfd-connection-point-ref: eth0
        vnfd-id-ref: lteUE-vnf
    - id: datanet
      name: datanet
      short-name: datanet
      type: ELAN
      vnfd-connection-point-ref:
      - member-vnf-index-ref: '1'
        vnfd-connection-point-ref: eth1
        vnfd-id-ref: lteUE-vnf
```



## VNFDs for WiFi connection

For the WiFi case, each node of the testbed is using a highly configurable WiFi card, can supports all of the modes of the IEEE 802.11 suite of protocols (Access Point, Station, Mesh, Ad-hoc, Monitor). For the needs of 5GinFIRE, only the modes of Access Point and Station are exposed through the NITOS VIM. This means that experimenters may use the NITOS nodes in order to set them up as WiFi Access Points (APs), and use the respective nodes configured as clients and associated with them. For the needs of 5GinFIRE, the experimenters may deploy VNFs to the NITOS nodes that are using the WiFi interface.

Since for establishing a WiFi link at least two compute nodes need to be configured, one as an Access Point and at least one as a Station attached to it, the respective example NSD is making use of two VNFs. Similar to the LTE case, some parameters need to be passed to the VNF so that the NITOS tools setup the WiFi equipment on the compute node. These parameters are passed through the description field, and include settings for the following: 1) the physical interface on the compute node, as the NITOS nodes usually have two WiFi interfaces each, 2) the ESSID name that will be used, and the for WiFi AP side 3) the WiFi mode (a/b/g/n/ac) and 4) the operating channel. 
Whenever the NITOS VIM is receiving such a request, the description field is parsed and the respective tools in NITOS are called in order to setup this functionality over all the different compute nodes that will be used. In all the cases of VNFs that are submitted, the first priority for being deployed is the VNF that will run over the AP connection; this happens in order to configure the AP before all the clients that will attach to it.

The following is a VNF with WiFi connectivity, running over an Access Point.

```text
 vnfd:vnfd-catalog:
  vnfd:
  - connection-point:
    - id: eth0
      name: eth0
      short-name: eth0
      type: VPORT
    - id: eth1
      name: eth1
      short-name: eth1
      type: VPORT
    description: A VNF consisting of 1 VDU connected to a control ethernet VL and to a wifi VL
    id: wifiAP-vnf
    logo: osm.png
    mgmt-interface:
      cp: eth0
    name: wifiAP-vnf
    short-name: wifiAP-vnf
    vdu:
    - cloud-init-file: cloud-config.txt
      count: '1'
**      description: type:WifiAP,interface:wlan0,essid:test,mode:g,channel:1**
			id: wifApVM
      image: ubuntu1404_cloud
      interface:
      - external-connection-point-ref: eth0
        name: eth0
        position: '1'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      - external-connection-point-ref: eth1
        name: eth1
        position: '2'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      name: wifiApVM
      vm-flavor:
        memory-mb: '4096'
        storage-gb: '5'
        vcpu-count: '4'
    version: '1.0'
```


Similarly, for a VNF running over a Station interface, associated with the WiFi AP described earlier is the following:


```text
 
 
 vnfd:vnfd-catalog:
  vnfd:
  - connection-point:
    - id: eth0
      name: eth0
      short-name: eth0
      type: VPORT
    - id: eth1
      name: eth1
      short-name: eth1
      type: VPORT
    description: A VNF consisting of 1 VDUs connected to an wifi VL
    id: wifiClient-vnf
    logo: osm.png
    mgmt-interface:
      cp: eth0
    name: wifiClient-vnf
    short-name: wifiClient-vnf
    vdu:
    - cloud-init-file: cloud-config.txt
      count: '1'
      **description: type:WifiClient,interface:wlan0,essid:test**
      id: wifiClientVM
      image: ubuntu1404_cloud
      interface:
      - external-connection-point-ref: eth0
        name: eth0
        position: '1'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      - external-connection-point-ref: eth1
        name: eth1
        position: '2'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      name: wifiClientVM
      vm-flavor:
        memory-mb: '4096'
        storage-gb: '5'
        vcpu-count: '4'
    version: '1.0'
```

And the respective NSD is the following:


```text
 nsd:nsd-catalog:
  nsd:
  - constituent-vnfd:
    - member-vnf-index: '1'
      vnfd-id-ref: wifiAP-vnf
    - member-vnf-index: '2'
      vnfd-id-ref: wifiClient-vnf
    description: NS with 2 VNFs connected by datanet and mgmtnet VLs
    id: wifi-ns
    logo: osm.png
    name: wifi-ns
    short-name: wifi-ns
    version: '1.0'
    vld:
    - id: mgmtnet
      mgmt-network: 'true'
      name: mgmtnet
      short-name: mgmtnet
      type: ELAN
      vim-network-name: provider1
      vnfd-connection-point-ref:
      - member-vnf-index-ref: '1'
        vnfd-connection-point-ref: eth0
        vnfd-id-ref: wifiAP-vnf
      - member-vnf-index-ref: '2'
        vnfd-connection-point-ref: eth0
        vnfd-id-ref: wifiClient-vnf
    - id: datanet
      name: datanet
      short-name: datanet
      type: ELAN
      vnfd-connection-point-ref:
      - member-vnf-index-ref: '1'
        vnfd-connection-point-ref: eth1
        vnfd-id-ref: wifiAP-vnf
      - member-vnf-index-ref: '2'
        vnfd-connection-point-ref: eth1
        vnfd-id-ref: wifiClient-vnf
```


## VNFDs for mmWave connection

For the mmWave case, each NITOS node is able to use one the six mmWave nodes that are available in the testbed. The mmWave nodes support only point-to-point communication, and up to three pairs can be configured for simultaneous transmissions. Each of the six nodes is addressed through a VLAN interface; traffic sent over VLAN 692 is reaching the first node, VLAN 693 the second, etc. For the provisioning of VNFs using a mmWave link, a similar process is followed like for the previous technologies. A VLAN interface is created on the compute node that is attached to a bridge communicating with a second network interface of the VNF. Traffic sent over this interface gets subsequently transmitted over the VLAN, reaching the mmWave node and then over the air. At the receiving mmWave node, the traffic is encapsulated in the respective VLAN addressing the mmWave node. Traffic is transmitted over the VLAN and can be delivered at the VNF that has this VLAN configured at the compute node.

![12](/uploads/nitos/12.png "12")

As the mmWave equipment in NITOS is only supporting point-to-point connectivity, the provisioned VNFs should take place in pairs. Each of the pairs get access over the physical equipment by using separate VLAN identifiers for addressing each node. Regardless of the compute node that the VNFs are deployed, the connection to the mmWave takes place by creating and bridging the VLANs with the deployed VNFs on the compute node. It is possible that two VNFs are deployed over the same compute node, but their interfaces communicate over the mmWave infrastructure. 
Similar to the previous cases, some parameters are being passed through the description field; this is happening for identifying the pair of the physical nodes that will be used. Example VNFs using two of the deployed mmWave nodes are provided below.


```text
 vnfd:vnfd-catalog:
  vnfd:
  - connection-point:
    - id: eth0
      name: eth0
      short-name: eth0
      type: VPORT
    - id: eth1
      name: eth1
      short-name: eth1
      type: VPORT
    description: A VNF consisting of 1 VDUs connected with two VLs. One is the controller network and the othes is for mmwave network
    id: mmwaveOne-vnf
    logo: osm.png
    mgmt-interface:
      cp: eth0
    name: mmwaveOne-vnf
    short-name: mmwaveOne-vnf
    vdu:
    - cloud-init-file: cloud-config.txt
      count: '1'
      **description: type:mmWave,physical-node-id:1**
      id: mmwaveOneVM
      image: ubuntu1404_cloud
      interface:
      - external-connection-point-ref: eth0
        name: eth0
        position: '1'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      - external-connection-point-ref: eth1
        name: eth1
        position: '2'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      name: mmwaveOneVM
      vm-flavor:
        memory-mb: '4096'
        storage-gb: '5'
        vcpu-count: '4'
    version: '1.0'
```

And for using the second mmWave node:


```text
vnfd:vnfd-catalog:
  vnfd:
  - connection-point:
    - id: eth0
      name: eth0
      short-name: eth0
      type: VPORT
    - id: eth1
      name: eth1
      short-name: eth1
      type: VPORT
    description: A VNF consisting of 1 VDUs connected with two VLs. One is the controller network and the othes is for mmwave network
    id: mmwaveTwo-vnf
    logo: osm.png
    mgmt-interface:
      cp: eth0
    name: mmwaveTwo-vnf
    short-name: mmwaveTwo-vnf
    vdu:
    - cloud-init-file: cloud-config.txt
      count: '1'
      **description: type:mmWave,physical-node-id:2**
      id: mmwaveTwoVM
      image: ubuntu1404_cloud
      interface:
      - external-connection-point-ref: eth0
        name: eth0
        position: '1'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      - external-connection-point-ref: eth1
        name: eth1
        position: '2'
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
      name: mmwaveTwoVM
      vm-flavor:
        memory-mb: '4096'
        storage-gb: '5'
        vcpu-count: '4'
    version: '1.0'
```


The respective NSD is the following:


```text
nsd:nsd-catalog:
  nsd:
  - constituent-vnfd:
    - member-vnf-index: '1'
      vnfd-id-ref: mmwaveOne-vnf
    - member-vnf-index: '2'
      vnfd-id-ref: mmwaveTwo-vnf
    description: NS with 2 VNFs connected by datanet and mgmtnet VLs
    id: mmwave-ns
    logo: osm.png
    name: mmwave-ns
    short-name: mmwave-ns
    version: '1.0'
    vld:
    - id: mgmtnet
      mgmt-network: 'true'
      name: mgmtnet
      short-name: mgmtnet
      type: ELAN
      vim-network-name: provider1
      vnfd-connection-point-ref:
      - member-vnf-index-ref: '1'
        vnfd-connection-point-ref: eth0
        vnfd-id-ref: mmwaveOne-vnf
      - member-vnf-index-ref: '2'
        vnfd-connection-point-ref: eth0
        vnfd-id-ref: mmwaveTwo-vnf
    - id: datanet
      name: datanet
      short-name: datanet
      type: ELAN
      vnfd-connection-point-ref:
      - member-vnf-index-ref: '1'
        vnfd-connection-point-ref: eth1
        vnfd-id-ref: mmwaveOne-vnf
      - member-vnf-index-ref: '2'
        vnfd-connection-point-ref: eth1
        vnfd-id-ref: mmwaveTwo-vnf
```


All the aforementioned VNFs can be deployed at any other testbed; however, in such a case they will use only the available provider networks that exist at the testbed. For the NITOS case, the VIM retrieves these parameters from the VNFDs and prepares the wireless networks and compute nodes of the testbed prior to deploying them.



