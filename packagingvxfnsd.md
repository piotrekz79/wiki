<!-- TITLE: YANG models and packaging for VxF/NSD -->
<!-- SUBTITLE: Packaging for VxF/NSD	 -->

# YANG models and packaging for VxF/NSD

A NFV descriptor (VNFD or NSD) must be modelled using the YANG models defined in this specification and then encoded as JSON text using the using the procedures specified in RFC 7951 ^1. 

YANG is a data modelling language for the definition of data sent over the NETCONF network configuration protocol. The YANG data modelling language was developed by the NETMOD working group in the Internet Engineering Task Force (IETF) and was published as RFC6020 in October 2010. 
The data modelling language can be used to model both configuration data as well as state data of network elements. Furthermore, YANG can be used to define the format of event notifications emitted by network elements and it allows data modellers to define the signature of remote procedure calls that can be invoked on network elements via the NETCONF protocol. The language, being protocol independent, can then be converted into any encoding format, e.g. XML or JSON, that the network configuration protocol supports.
You can also find further information and examples on the currently used YANG models on: 
https://open.riftio.com/documentation/riftware/4.4/a/descriptor/yang-models/mano-yang-models.htm 
There is also an ongoing documentation of YANG based NFVD specification by ETSI is available here:
https://docbox.etsi.org/ISG/NFV/Open/Drafts/SOL006_YANG_based_NFV_Descriptors_spec 


## Developer tools for YANG modelling
To help the VxF/NSD developer to validate and use the YANG model, several sets of tools are available for free:
•	Python YANG validator: An extensible YANG validator and converter written in python,
Available on Github under the ISC License https://github.com/mbj4668/pyang 
•	Python YANG model extraction tool: Xym is a simple utility for extracting YANG modules from files.
Available on Github under the BSD License https://github.com/xym-tool/xym 
•	LibYang: is a YANG data modelling language parser and toolkit written (and providing API) in C.
Available on Github under the BSD License https://github.com/CESNET/libyang 


## Functional requirements for VNF & NSD Packaging specification 

In order to be compliant with OSM, the package must strictly follow the requirements precisely defined by ETSI in the following documents: 
•	“NFV, management and orchestration, VNF Packaging Specification” Part. 6. 
ETSI GS NFV-IFA 011 [^2]
•	“NFV, Management and Orchestration; Network Service Templates Specification” Part 5. 
ETSI GS NFV-IFA 014 [^3]
Here are the general and packaging requirements extracted from the above documents. 





[^1]https://tools.ietf.org/html/rfc7951
[^2]http://www.etsi.org/deliver/etsi_gs/NFV-IFA/001_099/011/02.01.01_60/gs_nfv-ifa011v020101p.pdf
[^3]http://www.etsi.org/deliver/etsi_gs/NFV-IFA/001_099/014/02.01.01_60/gs_NFV-IFA014v020101p.pdf