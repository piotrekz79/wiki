<!-- TITLE: Sec5G: Securing 5G for Mission Critical Services  -->
<!-- SUBTITLE: A quick tutorial on how to run basic Sec5G experiments -->

# Download Sec5G Images
AF: https://cloud.onesource.pt/s/Wx8SL7R43RxMF9K
NEF: https://cloud.onesource.pt/s/Q3rJeXPHr5Rycmg
PCF: https://cloud.onesource.pt/s/NeYtGcBt64WrNzb
IDPS: https://cloud.onesource.pt/s/AWyTQs5dDQQZnPe

# Download Sec5G VNFs and NSD
https://cloud.onesource.pt/s/SR9CMHR6KAMaota

# Components Directory 

Inside the compressed file containing VNFs and NSD, you may find the following directory structure:

AF – VNF
├── af_onesource_vnf_vnfd
│   ├── af_onesource_vnf_vnfd.yaml
│   ├── charms
│   ├── checksums.txt
│   ├── cloud_init
│   │   └── af_onesource_vnf.cfg
│   ├── icons
│   │   └── OS_2.png
│   ├── images
│   └── scripts

NEF – VNF
	├── nef_onesource_vnf_vnfd
│   ├── charms
│   ├── checksums.txt
│   ├── cloud_init
│   │   └── nef_onesource_vnf.cfg
│   ├── icons
│   │   └── OS_2.png
│   ├── images
│   ├── nef_onesource_vnf_vnfd.yaml
│   └── scripts

PCF – VNF
	├── pcf_onesource_vnf_vnfd
│   ├── charms
│   ├── checksums.txt
│   ├── cloud_init
│   │   └── pcf_onesource_vnf.cfg
│   ├── icons
│   │   └── OS_2.png
│   ├── images
│   ├── pcf_onesource_vnf_vnfd.yaml
│   └── scripts

IDPS – VNF
	├── idps_onesource_vnf_vnfd
│   ├── charms
│   ├── checksums.txt
│   ├── cloud_init
│   │   └── idps_onesource_vnf.cfg
│   ├── icons
│   │   └── OS_2.png
│   ├── 	idps_onesource_vnf_vnfd.yaml
│   ├── images
│   └── scripts

NSD
	├── onesource_nsd
│   ├── checksums.txt
│   ├── icons
│   │   └── OS_2.png
│   ├── ns_config
│   ├── 	onesource_nsd.yaml
│   ├── scripts
│   └── vnf_config

# NSD

The default NSD included in the package has the following architecture:

![NSD](https://cloud.onesource.pt/s/MStB5r5oWKe2c9j/preview "Basic NSD")

# Testing

From the AF, ping NEF and check if you are able to access the machine:

```text
ping 192.168.100.18
```

If so, you can test the API with:

```text
 curl 192.168.100.18:5002
```

If you get an answer, then NEF is working and you are not blocked by IDPS.

# Basic Experimenting

In machine "AF 1" exec:

```text
python ~/NEF-develop_v2/af/af.py 1
```

In machine "AF 2", edit the following file:

```text
~/NEF-develop_v2/af/af.py

- afSubscribeOnNEF()
- triggerRequest()
- time.sleep(1)
+ #afSubscribeOnNEF()
+ #triggerRequest()
+ time.sleep(60)
```

Finally, in "AF 2" run:

```text
python ~/NEF-develop_v2/af/af.py 1
```

Outcome: AF 1 will get blocked by IDPS, while AF 2 will remain unblocked and getting responses as expected.
# Troubleshooting
Access each VM and kill all Python processes. Services will relaunch automatically.

```text
killall python
```

If one machine is not able to access the other, check the IP addresses of the target machine. Sometimes the interface used by Sec5G components fails to come up in OpenStack instances.

List all interfaces and view interface name:

```text
ifconfig -a
```

Bring interface up:

```text
ifconfig <iface_name> up
```