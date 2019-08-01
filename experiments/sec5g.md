<!-- TITLE: Sec5G: Securing 5G for Mission Critical Services  -->
<!-- SUBTITLE: A quick tutorial on how to run Sec5G experiments -->

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

From the AF, ping NEF and check if you are able to access its API at port 5002:

```text
ping 192.168.100.18
```

If so, you can test the API at:

```text
 curl 192.168.100.18:5002
```

If you get an answer, then NEF is working and you are not blocked by IDPS.

# Experimenting

In machine "AF" exec:

```text
python ~/NEF-develop_v2/af/af.py 1
```



# Troubleshooting
Access each VM and kill the python process.





