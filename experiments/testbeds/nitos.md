<!-- TITLE: NITOS VNF examples-->
<!-- SUBTITLE: How to run the 5G-VINO provided VNFs in NITOS -->

# Overview
5G-VINO deals with the integration of the NITOS testbed with the rest of the 5GinFIRE facilities. In this section, we detail the provided VNFs and NSDs that can be deployed in NITOS and take advantage of the wireless technologies that exist in the testbed.


# VNFs with LTE connectivity (using the Commercial Off-The-Shelf Equipment)

For the LTE case, provisioning a VNF with such capabilities equals to providing a VNF with an extra networking interface that is bridged on the compute node with the physical interface connected to the LTE network of NITOS. The VNF that is deployed in the testbed, is using two different interfaces: one bridged to the management Ethernet network, used for accessing the VNF, and a second one equalling to an LTE link. Services running inside the VNFs, can take advantage of this link, to communicate with other VNFs connected to the LTE network, or run in a completely isolated manner from other LTE clients, through the slicing schemes that are applied in the network .


## VNFD for COTS LTE connection

The provided VNF has one network connection as a management connection running over the Ethernet network of NITOS, and a second connection to the NITOS LTE infrastructure. Some parameters are needed for the connection to the LTE network, including the LTE subscriber group which the VNF will belong to, the Access Point Name (APN) that the subscriber group will use, and parameters about the maximum Uplink and Downlink traffic that the VNF will use. Tools invoked from the NITOS VIM side automatically retrieve lower level parameters that are required for connecting the LTE network, such as the International Mobile Subscriber Identifier (IMSI). 
Upon receiving such a VNF Description, the VIM of the NITOS side turns on the LTE base station (if it is powered off), and registers the LTE UE of the compute node that will be used to the LTE EPC. Along with these parameters, the APN that is passed from the experimenter and the subscriber group are also registered to the NITOS EPC, whereas tools running on the compute node facilitate the connection of the UE to the LTE network, by issuing AT commands over the USB interface of the UE. Once the connection is established, the LTE interface of the compute node is attached to a bridge which is offering the connectivity to the VNF. The extra fields are currently passed through the description of the VNF.  

`
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
      **description: type:Lte,virtual-apn:TEST_SS,dlambr:50000000,ulambr:50000000,qci:5,cluster-client:lte_client1,virtual-cluster:TEST_SS**
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
    version: '1.0'`

The image that is loaded for this VNF is a generic Ubuntu 14.04 image, but can be configured to anything else from the experimenter. Please notice the bold line in the description field that allows the NITOS VIM take care of all the low level configuration settings for the LTE equipment in the testbed.

The respective NSD is the following:
`
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
		`



