<!-- TITLE: Vrusafe -->
<!-- SUBTITLE:  Vrusafe experiment-->

# TCC & HINS & NSD Description

**TCC VxF Description**
The TCC VxF main component is the VRU Safe VDU, in an UBUNTU Cloud Image format.
Inside the image, 2 network interfaces have been configured. Each interface will receive an
IP address, after the validation procedure from the IT-AV cloud mentor. The second
component is a python module, namely the TCC python module. TCC is a -ready to usepython
server/client module developed for IT-AV testbed. The server is configured to receive
contextual information from the RSUs (GPS, Latitude, Longitude, Speed, Heading) towards
OBUs’ potential collision events. TCC processes the acquired contextual information and
generates position prediction matrices based on OBUs velocity, direction, etc. The matrices
are then being forwarded to the HINS for further calculations via the python client.

**HINS VxF Description**
The HINS VxF primary component is the VRU Safe VDU, in an UBUNTU Cloud Image
format. Inside the image, 2 network interfaces have been configured. Each interface will
receive an IP address, after the validation procedure from the IT-AV cloud mentor. The
second component is a python module, namely the HINS python module. HINS is a -ready to
use- python server/client module. The server receives the collision prediction matrices from
the TCC module, processes the information and detects any potential collisions. Those
collisions will be reported to the relevant OBUs via HINS client, towards the Edge, which
forwards the information to them via the RSUs.

**VRU SAFE NSD Description**
The VRU Safe NSD consists of the HINS and TCC VxFs. The intercommunication of VxFs
is achieved via Virtual Links. Two Virtual Links are created and bind the corresponding
network interfaces.

**Experiment Deployment**
After the validation status, the NSD can be deployed in the IT-AV testbed for further
experimentation.

**Access Experiment**
The last step to access the VRU_Safe experiment is to clone the VRU_Safe Repository:
VRU_Safe cloud repo contains the TCC, as well as sHINS moduless. The user should only
provide in both modules the Machine’s IP and a destination for the TCC.

Prerequisites are:
● git
● Python 2.7 (compatible also with Python 3)
● Pickle

**Git link: git clone https://git.scanlab.gr/georget/vru_safe_cloud.git**

**Example commands:**

```text
git clone https://git.scanlab.gr/georget/vru_safe_cloud.git
cd vru_safe/
python tcc.py machines_IP Hins_IP
python edge.py machines_IP
```
