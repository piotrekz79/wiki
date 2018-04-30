# Guide: Advanced Hardware Requirements

This tutorial shows the process of modeling and creating VNFs that require advanced capabilities such as specific hardware configurations or SDN capabilities.

Note: this guide is only applicable from OSM Release THREE onwards.

## Brief explanation

VNF descriptors define what resources are needed. Sometimes the functions that a VNF implements need specific hardware configurations or have a certain type of connectivity constraint that will need to make use of SDN capabilities in order to fulfill those constraints. OSM will make use of EPA (Enhanced Platform Awareness) capabilities and SDN assist to provide the adequate response for these constraints.

### EPA: Enhanced Platform Awareness

EPA is an aggregate of features that VIMs adopted in order to provide near native (non-virtualized) performance. These features provide the VNFs hardware capabilities that before were performed by software, increasing their performance.

As an example, here is a short list of the most used capabilities in terms of EPA features:

+ Memory page allocation size
+ CPU pinning policy
+ CPU thread pinning policy
+ PCIe passthrough devices
+ NUMA policy
+ CPU Feature
+ Hypervisor type

### SDN Assist

SDN Assist makes use of EPA and SDN to orchestrate both the VIM and the SDN controller to provide high performance networking. To make this possible OSM will use SDN Assist, which uses PCIe Passthrough and/or SR-IOV interfaces and provides rules to the SDN controller to interconnect them making an underlay connection that will have higher performance than a virtualized one.

## How to make use of these features

### EPA features

EPA features are provided in the definitions of the VDUs that compose each VNF.

The next example provides a sample of a simple VDU. This VDU requires 2 CPU cores, 4096 MB of RAM and 5 GB of disk. It also requires 2 virtual interfaces: vdu_eth0 and vdu_eth1.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    interface:
      - name: vdu_eth0
        position: 1
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
        external-connection-point-ref: mgmt_cp
      - name: vdu_eth1
        position: 2
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
        external-connection-point-ref: data_cp
~~~~

#### Memory page allocation

Lets suppose that the nature of this VDU changed and now it requires that the memory pages are higher than 4 KB. Lets say that the VDU now requires 1 GB memory pages.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    guest-epa:
      mempage-size: SIZE_1GB
    ...
~~~~

The example shown above represents how memory page allocation can be changed and how it doesn't affect the VM Flavor section.

#### CPU pinning policy

Lets suppose now that the VNF cannot share the CPU with other VNFs.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    guest-epa:
      cpu-pinning-policy: DEDICATED
    ...
~~~~

#### CPU Thread pinning policy

This policy referes to CPUs that support SMT (Simultaneous Multithreading). Lets say the VDU cannot have two vCPUs running on two threads that run in the same CPU core.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    guest-epa:
      cpu-thread-pinning-policy: SEPARATE
    ...
~~~~

The above example shows how this scenario can be described in the VNF descriptor.

#### NUMA policy

Lets say now that the VDU requires that certain NUMA constraints should be followed. In these NUMA constraints, the VNF creator can for example define that the memory allocated for the VDU should be directly attached to the CPU that is being used, reducing the memory access hops when a cache miss occurs.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    guest-epa:
      numa-node-policy:
        mem-policy: STRICT
        node-cnt: 1
        node:
          - id: 1
    ...
~~~~

The example above shows how the VDU is only running on 1 NUMA node and that node should be the node with the identifier 1. It also specifies that the memory should be allocated from the memory banks that are directçy connected to that NUMA node.

#### Hypervisor type

Lets say this VDU now requires to be run on a Xen hypervisor.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    hypervisor-epa:
      type: XEN
    ...
~~~~

#### PCIe Passthrough

Now the VNF requires a specific PCIe connected device to accelarate data processing.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    guest-epa:
      pcie-device:
        - device-id: '0000:14:00.0'
          count: 1
    ...
~~~~

#### CPU capabilities

Lets say the VNF requires AVX2 and prefers POPCNT features to be present in the CPU that the VDU will use.

Note: when specifying these capabilities, it is better to specify the capability and not the CPU generation or family.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    host-epa:
      cpu-feature:
        - feature: REQUIRE_AVX2
        - feature: PREFER_POPCNT
    ...
~~~~

#### SR-IOV interfaces

The VDU now requires SR-IOV interfaces. SR-IOV interfaces will be faster than VIRTIO interfaces because they are using an hardware implementation instead of a software one.

~~~~yaml
vdu:
  - id: vdu
    name: vdu
    image: vdu_image
    count: 1
    cloud-init-file: cloud_init.cfg
    vm-flavor:
      vcpu-count: 2
      memory-mb: 4096
      storage-gb: 5
    interface:
      - name: vdu_eth0
        position: 1
        type: EXTERNAL
        virtual-interface:
          type: VIRTIO
        external-connection-point-ref: mgmt_cp
      - name: vdu_eth1
        position: 2
        type: EXTERNAL
        virtual-interface:
          type: SR-IOV
        external-connection-point-ref: data_cp
~~~~

### SDN Assist

To make use of SDN Assist, the VNF/NS creator just needs to interconnect SR-IOV or PCIe Passthrough network interfaces with VLDs. If SDN capabilities are provided to OSM, the software will take care of creating the rules to interconnect these interfaces using an underlay connection that is directly mapped on the switching dataplane.
