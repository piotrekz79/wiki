# Tutorial: Create OpenCV Transcoder NS

This tutorial shows the process of creation of an example Network Service that makes use of the OpenCV Transcoder VNF, allowing to launch it via OSM.

You can find the complete NS [here](https://github.com/5GinFIRE/opencv_transcoder_vnf/tree/master/ns).

## Folder Structure

In order to create the NS, lets create our root folder:

~~~~bash
mkdir ~/opencv_transcoder_ns
cd ~/opencv_transcoder_ns
~~~~

Inside our root folder, lets create a few folders and files that might be useful:

~~~~bash
mkdir icons ns_config scripts vnf_config
touch README opencv_transcoder_nsd.yaml
~~~~

You should have the following folder structure:

~~~~bash
.
├── icons/
├── ns_config/
├── scripts/
├── vnf_config/
├── README
└── opencv_transcoder_nsd.yaml
~~~~

## Network Service Metadata

Lets start by adding the metadata of the NS to **opencv_transcoder_nsd.yaml**:

~~~~yaml
nsd:nsd-catalog:
  nsd:
  - id: "opencv_transcoder_ns"
    name: "opencv_transcoder_ns"
    short-name: "opencv_transcoder_ns"
    description: "OpenCV Transcoder NS"
    vendor: "5GinFIRE"
    logo: "5GinFIRE.png"
    version: "1.0"
~~~~

So lets break down what these metadata fields mean:

+ **id:** NS identifier (must be unique)
+ **name:** Name of the NS
+ **short-name:** Short name of the NS
+ **logo:** Name of the icon image file (image file must be inside of the icons folder)
+ **vendor:** Person/Organization that created the NS
+ **version:** Version of the NS
+ **description:** Brief description of the NS

## Constituent VNFDs

The constituent VNFDs is list that contains all the VNFDs that will be used to make the netowrk service.

~~~~yaml
    constituent-vnfd:
    - member-vnf-index: 1
      vnfd-id-ref: "opencv_transcoder_vnf"
      start-by-default: "true"
~~~~

Each element in this list is composed by the following fields:

+ **member-vnf-index**: Index to be referenced by
+ **vnfd-id-ref**: VNFD identifier by which the VNF is known in OSM (must be unique)
+ **start-by-default**: If the VNF will be run when the NS instatiation moment

## Virtual Link Descriptors

The Virtual Link Descriptors define the Virtual Link requirements for connecting VNFs inside the Network Service. So it is represented using a list that is composed by multiple Virtual Link Descriptors.

~~~~yaml
    vld:
    - id: "mgmt_vl"
      name: "mgmt_vl"
      short-name: "mgmt_vl"
      vendor: "5GinFIRE"
      description: "Management Network"
      version: "1.0"
      type: "ELAN"
      mgmt-network: "true"
      vnfd-connection-point-ref:
      - member-vnf-index-ref: 1
        vnfd-id-ref: "opencv_transcoder_vnf"
        vnfd-connection-point-ref: "transcoder_vnfd/cp0"
    - id: "data_vl"
      name: "data_vl"
      short-name: "data_vl"
      vendor: "5GinFIRE"
      description: "Data Network"
      version: "1.0"
      type: "ELAN"
      mgmt-network: "false"
      vnfd-connection-point-ref:
      - member-vnf-index-ref: 1
        vnfd-id-ref: "opencv_transcoder_vnf"
        vnfd-connection-point-ref: "transcoder_vnfd/cp1"
~~~~

Each element in this list is composed by the following fields:

+ **id**: VLD identifier (must be unique)
+ **name**: VLD name
+ **short-name**: VLD short name
+ **vendor**: VLD identifier (must be unique)
+ **description**: VLD description
+ **version**: VLD version
+ **type**: VLD type (ELAN is the only value supported)
+ **mgmt-network**: indicates if the network is a VIM management network
+ **vnfd-connection-point-ref**: list of references to VNF connection points
++ **member-vnf-index-ref**: reference index defined in the constituent-vnfd
++ **vnfd-id-ref**: VNFD identifier defined in the constituent-vnfd
++ **vnfd-connection-point-ref**: Connection point defined in the VNFD

VLD setup
The experimenter should name the Management and Data VLDs in the yaml file appropriately for automatic network definition during automatic instantiation of the NS.
-The VLD which will be used for the Management plane should have a name ending in "_mgmt".
-The VLD which will be used for the Data plane should have a name ending in "_data".

## Packaging the Network Service

### Compute the checksums

Lets compute the checksums and insert into checksums.txt:

~~~~bash
cd ~/opencv_transcoder_ns
find * -type f -print | while read line; do md5sum $line >> checksums.txt; done
~~~~

### Create an archive

Lets create the archive in **tar.gz** format:

~~~~bash
cd ~
tar -zcvf opencv_transcoder_ns.tar.gz opencv_transcoder_ns
~~~~
