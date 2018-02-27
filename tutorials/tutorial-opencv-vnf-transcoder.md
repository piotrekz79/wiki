# Tutorial: Create OpenCV Transcoder VNF

This tutorial shows the process to replicate the construction of the OpenCV Transcoder VNF.
To create a VNF, you need to have three things:
- VM Image
- VNF Descriptor
- Charm

## VM Image

To create the base image, follow this [article](https://docs.openstack.org/image-guide/ubuntu-image.html).

After creating the base image and installing all the required software, try to shrink the VM image using:

~~~~
qemu-img convert -O qcow2 -c <original_vm_image> <shrunk_vm_image>
~~~~

**Note:** Shrinking the VM image may corrupt the image, so you should test using both images.

## VNF Descriptor

Lets start by creating the base folder for the VNF descriptor:

~~~~
mkdir ~/transcoder_vnf
cd ~/transcoder_vnf
~~~~

Then, we need to create the folder structure where the VNF Descriptor files will be stored:

~~~~
mkdir charms cloud_init icons images scripts
~~~~

After the folder structure has been created, we need to create some files:

~~~~
touch README opencv_transcoder_vnfd.yaml
~~~~

The folder and file structure should look like this:

~~~~
.
├── charms/
├── cloud_init/
├── icons/
├── images/
├── opencv_transcoder_vnfd.yaml
├── README
└── scripts/
~~~~

Lets start by creating the cloud-init configuration file:

~~~~
touch cloud_init/transcoder_cloud_init.cfg
~~~~

And inside this file lets put some basic configurations.

~~~~
#cloud-config
password: 5ginfire
chpasswd: { expire: False }
ssh_pwauth: True
~~~~

Lets insert into **opencv_transcoder_vnfd.yaml** the basic metadata of the VNF descriptor:

~~~~
vnfd:vnfd-catalog:
    vnfd:vnfd:
     -  id: opencv_transcoder_vnf
        name: opencv_transcoder_vnf
        short-name: opencv_vnf
        logo:
        vendor: 5GinFIRE
        version: '1.0'
        description: OpenCV Transcoder VNF
~~~~

So lets break down what these metadata fields mean:
- **id:** VNF identifier (must be unique)
- **name:** Name of the VNF
- **short-name:** Short name of the VNF
- **logo:** Name of the icon image file (image file must be inside of the icons folder)
- **vendor:** Person/Organization that created the VNF
- **version:** Version of the VNF
- **description:** Brief description of the VNF

The VNF will have two connection points. The first connection point will be used by Juju Charms to configure the VDU; the second connection will be used to access the data plane, or in simpler terms, it is the connection that allows the VDU to get the video stream and to publish the transcoded version.

~~~~
		connection-point:
        -   name: transcoder_vnfd/cp0
            type: VPORT
        -   name: transcoder_vnfd/cp1
            type: VPORT
~~~~

Each connection point is composed by the following fields:
- **name:** Name that represents the connection point (must be unique)
- **type:** Type of the connection point port (normally VPORT)

Now we need to define the VDU (Virtualization Deployment Unit), that will run the transcoding service.

~~~~
        vdu:
        -   cloud-init-file: transcoder_cloud_init.cfg
            count: '1'
            external-interface:
            -   name: eth0
                virtual-interface:
                    type: VIRTIO
                vnfd-connection-point-ref: transcoder_vnfd/cp0
            -   name: eth1
                virtual-interface:
                    type: VIRTIO
                vnfd-connection-point-ref: transcoder_vnfd/cp1
            id: transcoder_vdu
            image: opencv_transcoder_image
            name: transcoder_vdu
            vm-flavor:
                memory-mb: '8192'
                storage-gb: '20'
                vcpu-count: '8'
~~~~

Each VDU will the above mentioned fields and we will provide a brief explanation for them.

- **cloud-init-file:** Name of the file that contains the cloud-init configurations for the VM (cloud-init file must be inside of the cloud-init folder)
- **count:** Number of VDUs to create
- **external-interface:** Mapping between the VNF connection points and interfaces provided to the VDU
-- **name:** Name of the interface
-- **virtual-interface:** Choice of interface driver type (ex.: VIRTIO, OM-MGMT)
-- **vnfd-connection-point-ref:** Mapping between the defined interface and VNF connection point
- **id:** VDU identifier (must be unique)
- **image:** Name of the image to be used by the VDU
- **name:** Name of the VDU
- **vm-flavor:** Data structure that holds what computational resources the VDU needs
-- **memory-mb:** Amount of RAM in MBytes
-- **storage-gb:** Amount of disk in GBytes
-- **vcpu-count:** Amount of vCPUs

After defining the VNF metadata, its connection points and the needed VDUs, we need to specify the service primitives that will be provided by the Juju Charm.
There is one service premitive that is mandatory: config. The **config** service primitive will be responsible by setting up the interfaces and the initial configurations (if need be).
Then we can create other service primitives that we might need. In this case, we will need a service primitive that will configure and run our transcoder code inside the VDU. This service primitive shall be called **start-transcoder** and will take as parameters the IP where it should get the video stream and the port where it will output the transcoded stream.
Lets now have a look at the VNF configuration.

~~~~
		vnf-configuration:
            config-attributes:
                config-delay: 10
            service-primitive:
            -   name: config
                parameter:
                -   data-type: STRING
                    default-value: <rw_mgmt_ip>
                    name: ssh-hostname
                -   data-type: STRING
                    default-value: ubuntu
                    name: ssh-username
                -   data-type: STRING
                    default-value: 5ginfire
                    name: ssh-password
                -   data-type: STRING
                    name: ssh-private-key
            -   name: start-transcoder
                parameter:
                -   data-type: STRING
                    name: stream-ip
                -   data-type: INTEGER
                    name: output-port
            initial-config-primitive:
            -   name: config
                parameter:
                -   name: ssh-hostname
                    value: <rw_mgmt_ip>
                -   name: ssh-username
                    value: ubuntu
                -   name: ssh-password
                    value: 5ginfire
                seq: '1'
            juju:
                charm: transcoder
~~~~

In the **config-attributes**, we only configure the **config-delay** so that the configuration doesn't start right after the instantiation process.

Lets analyze the **config** service primitive:
- **name:** Name of the service primitive (must match with the name defined in the charm)
- **parameter:** Definition of the parameter that should be passed
-- **data-type:** Type of the parameter (ex.: STRING, INTEGER)
-- **default-value:** Default value of the parameter
-- **name:** Name of the parameter

In the special case of the **config** service primitive, we can see that in the **default-value** for ssh-hostname there is a strange value: **&lt;rw_mgmt_ip&gt;**. This strange value will be replaced by Juju automatically, because we can't know in advance which IP the VDU will be assigned.

After defining all our service primitives, we need to define which service primitives need to be run to configure the VDU and in which order. In our case we just need to run the **config** service primitive, but lets verify **initial-config-primitive** (not all service primitives need to be in **initial-config-primitive**).
- **name:** Name of the service primitive
- **seq:** Position in the sequence
- **parameter:** Data structure that holds the parameters and values
-- **name:** Name of the parameter
-- **value:** Value that should be passed

The **juju** option defines which charms are used. In this case, we are going to use the **transcoder** charm that will be placed in the charm folder.

The final descriptor can be found [here]().

For more information about VNF Descriptors, read this [article](https://osm.etsi.org/wikipub/index.php/Creating_your_own_VNF_package_\(Release_TWO\)).

## Juju Charm

Let's start by talking about the Charm. A JuJu Charm is script/program that will control the configuration and management processes.
In this case, the Charm will be run in a container that will configure the VDUs (this is called a Proxy Charm).
For more information about the Juju configuration, check this [article](https://osm.etsi.org/wikipub/index.php/Creating_your_own_VNF_charm_\(Release_TWO\)).

To create charms, you will need to install the JuJu tools:

~~~~
sudo add-apt-repository ppa:juju/stable
sudo apt update
sudo apt install juju
~~~~

Then you need to setup your folder structure and coding environment:

~~~~
mkdir -p ~/charms/layers
export JUJU_REPOSITORY=~/charms
export LAYER_PATH=$JUJU_REPOSITORY/layers
cd $LAYER_PATH
~~~~

Now lets create our Charm:

~~~~
charm create transcoder
cd transcoder
~~~~

Lets modify layers.yaml in order to provide new functionality to this charm:

~~~~
includes:
  - layer:basic
  - layer:vnfproxy
~~~~

There are two layers: **basic** and **vnfproxy**. The **basic** layer is responsible by providing the basic hooks and life cycle events that Juju uses. The **vnfproxy** layer is responsible for a new set of hooks and life cycle events necessary for VDU configuration and management and provides ssh connectivity to the VDUs.

A Charm is a piece of code like any other, that can be reused, so lets add some metadata about authorship and where it can run. To this, lets modify metadata.yaml:

~~~~
name: transcoder
summary: Transcoder charm
maintainer: Eduardo Sousa <eduardosousa@av.it.pt>
description: |
  The transcoder charm initializes the transcoder VNF.
subordinate: false
tags:
  - misc
  - osm
  - vnf
  - nfv
series:
  - trusty
  - xenial
~~~~

Modify actions.yaml:

~~~~
start-transcoder:
  description: Start transcoding
  params:
    stream-ip:
      description: IP to get the video stream from
      type: string
    output-port:
      description: Port on which the transcoder is outputing the result
      type: integer
  required:
  	- stream-ip
  	- output-port

~~~~

Create a directory for actions:

~~~~
mkdir actions
~~~~

For each action, create a script to invoke the reactive framework with the action to be performed. In this case, we only need one file because we only have one action: **start-transcoder**.

~~~~
cat << 'EOF' >> actions/start-transcoder
#!/usr/bin/env python3

import sys
sys.path.append('lib')

from charms.reactive import main
from charms.reactive import set_state
from charmhelpers.core.hookenv import action_fail

set_state('actions.start-transcoder')

try:
    main()
except Exception as e:
    action_fail(repr(e))

EOF
~~~~

And make this file executable:

~~~~
chmod +x actions/start-transcoder
~~~~

Now that the action is mapped, we need to create the file where the code for the actions is going to be:

~~~~
rm reactive/transcoder.py
touch reactive/transcoder.py
~~~~

After all this, we need to code the interaction mapped by the action, but first lets do the initial VDU configuration:

~~~~
from charmhelpers.core.hookenv import (
    action_fail,
    action_get,
    action_set,
    config,
    status_set,
)
from charms.reactive import (
	when,
    set_state,
    remove_state,
)
import charms.sshproxy

cfg = config()


@when('config.changed')
def config_changed():
    err = ''
    try:
        cmd = "echo '' | sudo tee -a /etc/network/interfaces.d/50-cloud-init.cfg > /dev/null && "
        cmd += "echo 'auto ens4' | sudo tee -a /etc/network/interfaces.d/50-cloud-init.cfg > /dev/null && "
        cmd += "echo 'iface ens4 inet dhcp' | sudo tee -a /etc/network/interfaces.d/50-cloud-init.cfg > /dev/null && "
        cmd += "sudo timeout 5 ifup ens4"
        result, err = charms.sshproxy._run(cmd)
    except:
        action_fail('command failed: ' + err)
    else:
        set_state('transcoder.configured')
        status_set('active', 'ready!')
~~~~

In this configuration function we are just creating a new interface inside the VDU, setting it to get its IP via DHCP and bringing the network interface up. All this needs to be done through linux command since we are using SSH.

Lets now write the code that will activate the transcoding inside the VDU:

~~~~
@when('transcoder.configured')
@when('actions.start-transcoder')
def start_transcoder():
    stream_ip = action_get('stream-ip')
    output_port = action_get('output-port')

    err = ''
    try:
        cmd = "sudo rm /etc/systemd/system/opencv.service >/dev/null 2>&1; "
        cmd += "sudo systemctl stop opencv.service >/dev/null 2>&1; "
        cmd += "sudo systemctl daemon-reload"
        result, err = charms.sshproxy._run(cmd)
    except:
        action_fail('command failed: ' + err)
        remove_state('actions.start-transcoder')
        return

    err = ''
    try:
        cmd = "echo '[Unit]' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'Description=OpenCV' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo '' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo '[Service]' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'Type=simple' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'User=ubuntu' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'WorkingDirectory=/home/ubuntu' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'ExecStart=/usr/bin/python live_server.py {0} {1}' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && ".format(stream_ip, output_port)
        cmd += "echo 'Restart=always' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'RestartSec=5' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo '' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo '[Install]' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "echo 'WantedBy=multi-user.target' | sudo tee -a /etc/systemd/system/opencv.service > /dev/null && "
        cmd += "sudo systemctl daemon-reload && "
        cmd += "sudo systemctl start opencv.service"
        result, err = charms.sshproxy._run(cmd)
    except:
        action_fail('command failed: ' + err)
    else:
        action_set({'output': result, 'errors': err})
    finally:
        remove_state('actions.start-transcoder')
~~~~

This function can only be run after configuration because only the configuration function will set the state **'transcoder.configured'**. To activate the transcoding script **live_server.py**, we need to run it as systemd service, so we create a systemd service file that indicates how to run the transcoding script and then start using **systemctl**. In the beginning of the function you can see how parameters are passed to the function.

**Note:** we recommend the usage of **SystemD** to launch services inside the VDU because it's much easier to configure and debug. **SystemD** also provides interesting functions like restart in case of failure and restart scheduling.

The final **transcoder.py** can be found [here]().

After all this, we need to build this charm (this process will download all the libraries needed to run it):

~~~~
charm build
~~~~

## Packaging the VNF Descriptor

There are a few steps to package a VNF descriptor:
1. Copy the built charm into the VNF Descriptor charms folder
2. Compute the checksums for all the files and put it in checksums.txt
3. Create an archive of the VNF Descriptor folder

### Copy the charm

Lets copy the built charm folder:

~~~~
cp -R ~/charms/builds/transcoder ~/transcoder_vnf/charms
~~~~

### Compute the checksums

Lets compute the checksums and insert into checksums.txt:

~~~~
cd ~/transcoder_vnf/charms
find * -type f -print | while read line; do md5sum $line >> checksums.txt; done
~~~~

### Create an archive

Lets create the archive in **tar.gz** format:

~~~~
cd ~
tar -zcvf opencv_transcoder_vnf.tar.gz transcoder_vnf
~~~~