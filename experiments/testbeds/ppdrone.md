<!-- TITLE: PPDR ONE Experiment example  -->
<!-- SUBTITLE: Network performance testing for PPDR-ready network architectures -->

# PPDR ONE Experiment example
## Experiment Overview

The example scenario utilizes qMON Monitoring solution implemented as VxFs and NSD to enable client-server network performance measurements between different VIM hosts or VIM providers.

![Ppdrone Experiment Example Small](/uploads/ppdrone/ppdrone-experiment-example-small.png "Ppdrone Experiment Example Small")
**Figure 1: PPDRONE Experiment Example**

## qMON Monitoring Solution

qMON Intervention Monitoring solution is a telco-grade 5G-ready measurement automation system for mobile, fixed and cloud environments (TRL9). It provides:
* Probes, management backend and analytics tools
* Live network and service tests/troubleshooting 
* Real-time performance and SLS/SLA monitoring
* Drive and benchmark testing for broadband PPDR networks (LTE/4G and 5G)
* PPDR network coverage and mission critical application performance assessment
* QoE/QoS prediction in live BB PPDR networks

![Qmon System Architecture](/uploads/ppdrone/qmon-system-architecture-small.png "Qmon System Architecture")
**Figure 2: qMON System Architecture**

The qMON system comprises 4 main parts based either on cloud VMs, containers or dedicated consumer and industrial HW:
* **qMON NetworkSensor** – Autonomous distributed agent for emulating user (mobile/fixed) activities and active services/applications
* **qMON Manage** – cloud-based back-end agent management
* **qMON Collector**– centralized data and KPI collection infrastructure;
* **qMON Insight** – Advanced KPI analysis and visualizations using professional real-time and offline BI analytics tools (Kibana, Grafana and Tableau).

![Qmon](/uploads/ppdrone/qmon.png "Qmon")
**Figure 3: qMON System Components**

Various network KPIs are measured and saved during the measurements, among them but not limited to, are the following KPIs:

* RTT (round trip time)
* DNS
* IPERF Download
* IPERF Upload
* HTTP/FTP Download
* WEB MOS
* FTP UPLOAD

If the qMON NetworkSensor runs on phsyical device with a modem (Linux-based PC or Android) the radio KPIs are also collected (e.g. RSRP, RSRQ, CA State…)

## Components description

qMON NetworkSensor is provided to experimenters as a VxF in client and server mode. 

### VxF

**qMON NetworkSensor Client VxF**

* Acts as a measurement client
* Emulates end user
* Can be deployed as as simple service (client only) or in client-server mode.

Example template for qMON NetworkSensor Client VxF:


```text
vnfd:vnfd-catalog:
    vnfd:
    -   connection-point:
        -   name: ens3
            type: VPORT
        -   name: ens4
            type: VPORT
        description: qMON Cloud Agent VNF with 2 nic
        id: qmon_vnfd_2net
        logo: inin-64.png
        mgmt-interface:
            cp: ens3
        monitoring-param:
        -   aggregation-type: AVERAGE
            id: metric_vim_client_load
            name: metric_vim_client_load
            vnf-metric:
                vnf-metric-name-ref: load
        -   aggregation-type: AVERAGE
            id: metric_vim_client_loadpct
            name: metric_vim_client_loadpct
            vnf-metric:
                vnf-metric-name-ref: load_pct
        -   aggregation-type: AVERAGE
            id: metric_vim_client_users
            name: metric_vim_client_users
            vnf-metric:
                vnf-metric-name-ref: users
        -   aggregation-type: AVERAGE
            id: metric_vim_client_mempct
            name: metric_vim_client_mempct
            vnf-metric:
                vnf-metric-name-ref: mem_pct
        -   aggregation-type: AVERAGE
            id: metric_vim_client_qmonrtt
            name: metric_vim_client_qmonrtt
            vnf-metric:
                vnf-metric-name-ref: qmon_rtt
        name: qmon_vnf_2net
        short-name: qmon_vnf_2net
        vdu:
        -   cloud-init-file: qmon_cloud_init.cfg
            count: 1
            description: qmon_vnfd_2net-VM
            id: qmon_vnfd_2net-VM
            image: qoe_vnf
            interface:
            -   external-connection-point-ref: ens3
                name: ens3
                type: EXTERNAL
                virtual-interface:
                    bandwidth: '0'
                    type: VIRTIO
                    vpci: 0000:00:0a.0
            -   external-connection-point-ref: ens4
                name: ens4
                type: EXTERNAL
                virtual-interface:
                    bandwidth: '0'
                    type: VIRTIO
                    vpci: 0000:00:0a.0
            name: qmon_vnfd_2net-VM
            vm-flavor:
                memory-mb: 2048
                storage-gb: 20
                vcpu-count: 2
        vendor: ININ
        version: '1.0'
        vnf-configuration:
            config-primitive:
            -   name: set-work-order
                parameter:
                -   data-type: STRING
                    default-value: ''
                    name: woid
                -   data-type: STRING
                    default-value: mndev.iinstitute.eu
                    name: mn
                -   data-type: STRING
                    default-value: xxxx
                    name: apikey
            -   name: set-mn-url
                parameter:
                -   data-type: STRING
                    default-value: ''
                    name: mn
            -   name: set-server-key
                parameter:
                -   data-type: STRING
                    default-value: ''
                    name: apikey
            -   name: set-server-ip
                parameter:
                -   data-type: STRING
                    default-value: ''
                    name: ip
            initial-config-primitive:
            -   name: config
                parameter:
                -   name: ssh-hostname
                    value: <rw_mgmt_ip>
                -   name: ssh-username
                    value: ubuntu
                -   name: ssh-password
                    value: qoe
                -   name: mode
                    value: client
                seq: '1'
            -   name: set-second-net
                seq: '2'
            -   name: set-second-net-dhcp
                seq: '3'
            -   name: set-work-order
                parameter:
                -   name: woid
                    value: '257'
                -   name: mn
                    value: mndev.iinstitute.eu
                -   name: apikey
                    value: xxxxx
                seq: '4'
            -   name: set-server-ip
                parameter:
                -   name: ip
                    value: 10.154.98.10
                seq: '6'
            -   name: set-qmon-monitoring
                seq: '7'
            juju:
                charm: qmon-2net
            metrics:
            -   name: load
            -   name: load_pct
            -   name: users
            -   name: mem_pct
            -   name: qmon_rtt

```

**qMON NetworkSensor Server VxF**

* acts as a measurement server,
* support multiple measurement clients,
* can be deployed as as simple service (server only) or in client-server mode.

Example template for qMON NetworkSensor Server VxF:

```text
vnfd:vnfd-catalog:
    vnfd:
    -   connection-point:
        -   name: ens3
            type: VPORT
        -   name: ens4
            type: VPORT
        description: qMON Cloud Reference Server VNF with 2 nic
        id: qmon_server_vnfd_2net
        logo: inin-64.png
        mgmt-interface:
            cp: ens3
        monitoring-param:
        -   aggregation-type: AVERAGE
            id: metric_vim_server_load
            name: metric_vim_server_load
            vnf-metric:
                vnf-metric-name-ref: load
        -   aggregation-type: AVERAGE
            id: metric_vim_server_loadpct
            name: metric_vim_server_loadpct
            vnf-metric:
                vnf-metric-name-ref: load_pct
        -   aggregation-type: AVERAGE
            id: metric_vim_server_users
            name: metric_vim_server_users
            vnf-metric:
                vnf-metric-name-ref: users
        -   aggregation-type: AVERAGE
            id: metric_vim_server_mempct
            name: metric_vim_server_mempct
            vnf-metric:
                vnf-metric-name-ref: mem_pct
        name: qmon_server_vnf_2net
        short-name: qmon_server_vnf_2net
        vdu:
        -   cloud-init-file: qmon_cloud_init.cfg
            count: 1
            description: qmon_server_vnfd_2net-VM
            id: qmon_server_vnfd_2net-VM
            image: qoe_server_vnf
            interface:
            -   external-connection-point-ref: ens3
                name: ens3
                type: EXTERNAL
                virtual-interface:
                    bandwidth: '0'
                    type: VIRTIO
                    vpci: 0000:00:0a.0
            -   external-connection-point-ref: ens4
                name: ens4
                type: EXTERNAL
                virtual-interface:
                    bandwidth: '0'
                    type: VIRTIO
                    vpci: 0000:00:0a.0
            name: qmon_server_vnfd_2net-VM
            vm-flavor:
                memory-mb: 2048
                storage-gb: 20
                vcpu-count: 2
        vendor: ININ
        version: '1.0'
        vnf-configuration:
            initial-config-primitive:
            -   name: config
                parameter:
                -   name: ssh-hostname
                    value: <rw_mgmt_ip>
                -   name: ssh-username
                    value: ubuntu
                -   name: ssh-password
                    value: qoe
                -   name: mode
                    value: server
                seq: '1'
            -   name: set-second-net
                seq: '2'
            -   name: set-second-net-dhcp
                seq: '3'
            juju:
                charm: qmon-2net
            metrics:
            -   name: load
            -   name: load_pct
            -   name: users
            -   name: mem_pct

```

