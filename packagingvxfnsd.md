<!-- TITLE: YANG models and packaging for VxF/NSD -->
<!-- SUBTITLE: Packaging for VxF/NSD	 -->

# YANG models and packaging for VxF/NSD

A NFV descriptor (VNFD or NSD) must be modelled using the YANG models defined in this specification and then encoded as JSON text using the using the procedures specified in RFC 7951 [^1]. 

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


**VNF_PACK.GEN.001** The VNF package contents, including the VNF descriptor, VNF binaries, configuration, scripts and software images, as well as manifest file, checksum, etc. as appropriate constitutes a single delivery unit from a distribution perspective. Any changes to the constituency of this unit shall be considered as a change to the whole and therefore shall be versioned, tracked and inventoried as one. 
**VNF_PACK.STRUCT.001** The VNF package shall be assembled in one file.
**VNF_PACK.STRUCT.002**	The VNF package shall be digitally signed by the VNF provider.
**VNF_PACK.STRUCT.003**	The VNF package should contain files for one VNF and its corresponding metadata
**VNF_PACK.STRUCT.004**	The VNF package shall enable including VNF specific files organized according to the design of the VNF, or referencing these files if they are external to the package.
**VNF_PACK.STRUCT.005**	The VNF package shall provide means to address individually the files which it contains and/or which it references.
**VNF_PACK.STRUCT.006**	If an external reference (e.g. URL) is used, file integrity information (such as checksum/signature) shall be specified to guarantee the integrity of the referenced file, so it cannot be substituted with a different file by the same name. 

You can find some examples of VnF/NSD package here: 
https://osm-download.etsi.org/ftp/osm-3.0-three/examples/ 


## Package pre-validation in the 5GinFire portal

Currently, the 5GInFIRE portal is not automatically pre-validating a package with the basic rules defined above. The administrator will be validating each package manually. 
An interesting feature would be to implement an automatic basic validation in the API, preventing users to submit invalid VxF/NSD package, and so, he will get instant feedback on what’s wrong. 
The validation process would be in two steps: 
•	First validate the package with the requirements specified by the ETSI. (Requirements needs to be transposed with code).
•	Validate the Yang model (use available tools to validate the model as listed above). 



[^1]https://tools.ietf.org/html/rfc7951
[^2]http://www.etsi.org/deliver/etsi_gs/NFV-IFA/001_099/011/02.01.01_60/gs_nfv-ifa011v020101p.pdf
[^3]http://www.etsi.org/deliver/etsi_gs/NFV-IFA/001_099/014/02.01.01_60/gs_NFV-IFA014v020101p.pdf