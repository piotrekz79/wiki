<!-- TITLE: PPDR ONE -->
<!-- SUBTITLE: A quick summary of PPDR ONE -->

# PPDR ONE testbed, Internet Institute
## PPDR ONE Overview

Public Protection and Disaster Relief facility for Outdoor and iNdoor 5G Experiments (PPDR ONE) is an extension of the 5GINFIRE ecosystem with a 5G enabled telco-grade development, testing and verification facility for experimentation with 5G network architectures and services for Public Protection and Disaster Relief (PPDR). With PPDR ONE, 5GINFIRE covers the public safety sector and incorporates capabilities to conduct laboratory and field 5G experiments designed for the needs of emergency response, disaster relief, and critical infrastructure protection. Located at INTERNET INSTITUTE premises in Ljubljana, Slovenia, the facility comprises indoor and outdoor experimentation sites as well as a compact portable node for field experiments, ready to be shipped to any location in the EU.

## Features
PPDR ONE represents an all-in-one experimentation facility that delivers all components of a virtualised 5G-enabled PPDR environment – SDR-based radio and core mobile system with flexible configuration options powered by NFV, cloud backend infrastructure, a set of reference PPDR services and apps, a PPDR IoT kit, industrial and ruggedized end user devices as well as a test and validation toolkit.

The PPDR ONE facility offers:
* Indoor experimentation site, covering laboratory-based testing in all operational frequencies from 70 MHz up to 6 GHz,
* Outdoor experimentation site, supporting field operation in the 700 MHz and 4500 MHz bands
* PPDR ONE portable node, a portable compact mobile system ready to be shipped and deployed on the experimenter’s test site anywhere in the EU, covering indoor scenarios (bands from 70 MHz and up to 6.0 GHz) and field operation (based on the available frequencies at the experimenter’s location).

The PPDR ONE test bed features:
* an SDR-based mobile system (Rel.14) providing 5G-enabled PPDR infrastructure, 
* an OpenStack-based backend infrastructure incorporating NFV-ready orchestration to manage experimental instances using IaaS model,
* commercial and ruggedized user terminals and IoT devices to conduct the experiments, 
* iMON Intervention Monitoring System (www.imon.si) designed for a public safety use, providing a set of PPDR ONE services and apps available for demonstration and evaluation, 
* qMON Quality Monitoring System (www.qmon.eu), a telco-grade toolset for continuous network and service testing, verification and benchmarking.

## Architecture

The PPDR ONE facility acts as a VIM and NFVI provider, connected through a secure VPN connection with the 5TONIC core site. MANO is connected to PPDR ONE VIM via the OpenStack APIs. The EPC/eNB provisioning is realized through predefined mobile profiles (e.g. different frequency bands, bandwidth, QoS profiles etc.). Selected mobile profiles will be provisioned manually on demand via e-mail, Slack or some other tool such as Bugzilla. Compute monitoring (e.g. CPU/RAM) and network monitoring (e.g. RTT, DL/UL speed) is offered as a cloud-based service in Grafana/Kibana.

